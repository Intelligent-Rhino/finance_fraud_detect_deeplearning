import pandas as pd


error_value =-100
missing_value = -999
missing_label ='missing'


class processing():

	def __init__(self):
		pass


	def fetch_risk_bucket(self,df_agg,col_name):
		df_agg['cls'] =df_agg['Fraud']/(df_agg['Non-Fraud']+0.1)
		df_agg['times'] = pd.cut(df_agg['cls'],
    						bins=[-1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,100000],
    						labels =['no-risk','risk<0.1','risk<0.2','risk<0.3','risk<0.4','risk<0.5','risk<0.6',
    								'risk<0.7','risk<0.8','risk<0.9','risk<1','high-risk'])
		value_map =dict(zip(df_agg[col_name].tolist(),df_agg['times'].tolist()))
		value_map.update({missing_value:missing_label})
		return value_map


	def agg_fn(self,df,y_col,x_col ='FRAUD_NONFRAUD',
				agg_col='ACTN_CD',agg_method ='count'):
		df_count = pd.pivot_table(data=df,
								index=y_col,
								columns=x_col,
                              	values=agg_col,
                              	aggfunc=agg_method,
                              	fill_value=0).reset_index()
		return df_count

	def risk_cls(self,df,col_name):
		df_agg =self.agg_fn(df,col_name)
		value_map =self.fetch_risk_bucket(df_agg,col_name)
		df[f"{col_name}_bin_10_feature"] = df[col_name].apply(lambda x : value_map.get(x))
		return df,value_map


	def bucket_cut(self,df,origin_col,target_col,bins,labels):
		df[target_col] = pd.cut(df[origin_col],bins=bins,labels=labels)
		return df


	def fetch_operation_hour(self,col):

		if col == missing_value:
			return missing_value
		try:
			value = pd.to_datetime(col)
			value =value.hour
		except:
			value = error_value
		return value


	def operate_hour(self,df,
						col,
						bins =[missing_value-1,error_value-1,-1,4,8,11,13,17,19,22,25],
						bin_labels =[missing_label,'bad-case','0-4','5-8','8-11','11-13','13-17','17-19','19-22','22-24']):
		target_col = f"{col}_hour"
		df[target_col] = df[col].apply(self.fetch_operation_hour)
		df = self.bucket_cut(df,target_col,target_col,bins,bin_labels)
		return df




	def timedelta_day(self,date_1,date_2,day_cls_map=[[-100000,-1,'operation_after_transaction'],
					                                   [0,30,'in_30_days'],
					                                   [31,180,'in_half_year'],
					                                   [180,360,'in_one_year'],
					                                   [361,1000000,'over_one_year']]):
	    if date_2 == missing_value:
	        return missing_label
	    
	    try:
	        date_1 =pd.to_datetime(date_1)
	        date_2 =pd.to_datetime(date_2)
	        t_delta = date_1 -date_2
	        res = int(t_delta.days)
	        for gap in day_cls_map:
	            if res >= gap[0] and res <= gap[1]:
	                res = gap[-1]
	                break
	    except:
	        res ='bad-case'
	    return res



