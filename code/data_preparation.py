import pandas as pd
import matplotlib as plt

def currency_to_int(x):
    x = x.replace('$','')
    x = x.replace(',','')
    
    return int(x)

def get_name_bar(x):
    df_top_20_x = df_final_aftergroupby[df_final_aftergroupby.category==x][:20]
    df_top_20_x_name = df_top_20_x.merge(df_final)
    df_top_20_x_name[['primary_name','ROI']].drop_duplicates().plot(kind='bar',x='primary_name',xlabel='Name', title=f'ROI by {x}');
