# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import glob
from datetime import datetime
csv_file_list=glob.glob('*.csv') #SOURCE FILE TYPE
total_file=len(csv_file_list)
for i in range(0,total_file):
    df=pd.read_csv(csv_file_list[i],skiprows=1)
    df.rename(columns=lambda x: x.strip(), inplace=True)
    DATE=csv_file_list[i].replace('fao_participant_oi_','') 
    DATE=DATE.replace('.csv','')
    DATE=datetime.strptime(DATE, '%d%m%Y')
    DATE=str(DATE).replace('00:00:00','')
    
    client_fut_index_long=df['Future Index Long'].iloc[0]
    client_fut_index_short=df['Future Index Short'].iloc[0]
    client_index_ceopt_long=df['Option Index Call Long'].iloc[0]
    client_index_ceopt_short=df['Option Index Call Short'].iloc[0]
    client_index_peopt_long=df['Option Index Put Long'].iloc[0]
    client_index_peopt_short=df['Option Index Put Short'].iloc[0]
    client_stk_fut_long=df['Future Stock Long'].iloc[0]
    client_stk_fut_short=df['Future Stock Short'].iloc[0]
    client_stk_ceopt_long=df['Option Stock Call Long'].iloc[0]
    client_stk_ceopt_short=df['Option Stock Call Short'].iloc[0]
    client_stk_peopt_long=df['Option Stock Put Long'].iloc[0]
    client_stk_peopt_short=df['Option Stock Put Short'].iloc[0]
    
    dii_fut_index_long=df['Future Index Long'].iloc[1]
    dii_fut_index_short=df['Future Index Short'].iloc[1]
    dii_index_ceopt_long=df['Option Index Call Long'].iloc[1]
    dii_index_ceopt_short=df['Option Index Call Short'].iloc[1]
    dii_index_peopt_long=df['Option Index Put Long'].iloc[1]
    dii_index_peopt_short=df['Option Index Put Short'].iloc[1]
    dii_stk_fut_long=df['Future Stock Long'].iloc[1]
    dii_stk_fut_short=df['Future Stock Short'].iloc[1]
    dii_stk_ceopt_long=df['Option Stock Call Long'].iloc[1]
    dii_stk_ceopt_short=df['Option Stock Call Short'].iloc[1]
    dii_stk_peopt_long=df['Option Stock Put Long'].iloc[1]
    dii_stk_peopt_short=df['Option Stock Put Short'].iloc[1]
    
    fii_fut_index_long=df['Future Index Long'].iloc[2]
    fii_fut_index_short=df['Future Index Short'].iloc[2]
    fii_index_ceopt_long=df['Option Index Call Long'].iloc[2]
    fii_index_ceopt_short=df['Option Index Call Short'].iloc[2]
    fii_index_peopt_long=df['Option Index Put Long'].iloc[2]
    fii_index_peopt_short=df['Option Index Put Short'].iloc[2]
    fii_stk_fut_long=df['Future Stock Long'].iloc[2]
    fii_stk_fut_short=df['Future Stock Short'].iloc[2]
    fii_stk_ceopt_long=df['Option Stock Call Long'].iloc[2]
    fii_stk_ceopt_short=df['Option Stock Call Short'].iloc[2]
    fii_stk_peopt_long=df['Option Stock Put Long'].iloc[2]
    fii_stk_peopt_short=df['Option Stock Put Short'].iloc[2]
    
    pro_fut_index_long=df['Future Index Long'].iloc[3]
    pro_fut_index_short=df['Future Index Short'].iloc[3]
    pro_index_ceopt_long=df['Option Index Call Long'].iloc[3]
    pro_index_ceopt_short=df['Option Index Call Short'].iloc[3]
    pro_index_peopt_long=df['Option Index Put Long'].iloc[3]
    pro_index_peopt_short=df['Option Index Put Short'].iloc[3]
    pro_stk_fut_long=df['Future Stock Long'].iloc[3]
    pro_stk_fut_short=df['Future Stock Short'].iloc[3]
    pro_stk_ceopt_long=df['Option Stock Call Long'].iloc[3]
    pro_stk_ceopt_short=df['Option Stock Call Short'].iloc[3]
    pro_stk_peopt_long=df['Option Stock Put Long'].iloc[3]
    pro_stk_peopt_short=df['Option Stock Put Short'].iloc[3]
       
    client={'DATE':DATE,'client_fut_index_long':client_fut_index_long,'client_fut_index_short':client_fut_index_short,'client_index_ceopt_long':client_index_ceopt_long,'client_index_ceopt_short':client_index_ceopt_short,
      'client_index_peopt_long':client_index_peopt_long,'client_index_peopt_short':client_index_peopt_short,'client_stk_fut_long':client_stk_fut_long,'client_stk_fut_short':client_stk_fut_short,'client_stk_ceopt_long':client_stk_ceopt_long,
      'client_stk_ceopt_short':client_stk_ceopt_short,'client_stk_peopt_long':client_stk_peopt_long,'client_stk_peopt_short':client_stk_peopt_short}
    
    dii={'DATE':DATE,'dii_fut_index_long':dii_fut_index_long,'dii_fut_index_short':dii_fut_index_short,'dii_index_ceopt_long':dii_index_ceopt_long,'dii_index_ceopt_short':dii_index_ceopt_short,
      'dii_index_peopt_long':dii_index_peopt_long,'dii_index_peopt_short':dii_index_peopt_short,'dii_stk_fut_long':dii_stk_fut_long,'dii_stk_fut_short':dii_stk_fut_short,'dii_stk_ceopt_long':dii_stk_ceopt_long,
      'dii_stk_ceopt_short':dii_stk_ceopt_short,'dii_stk_peopt_long':dii_stk_peopt_long,'dii_stk_peopt_short':dii_stk_peopt_short}
    
    fii={'DATE':DATE,'fii_fut_index_long':fii_fut_index_long,'fii_fut_index_short':fii_fut_index_short,'fii_index_ceopt_long':fii_index_ceopt_long,'fii_index_ceopt_short':fii_index_ceopt_short,
      'fii_index_peopt_long':fii_index_peopt_long,'fii_index_peopt_short':fii_index_peopt_short,'fii_stk_fut_long':fii_stk_fut_long,'fii_stk_fut_short':fii_stk_fut_short,'fii_stk_ceopt_long':fii_stk_ceopt_long,
      'fii_stk_ceopt_short':fii_stk_ceopt_short,'fii_stk_peopt_long':fii_stk_peopt_long,'fii_stk_peopt_short':fii_stk_peopt_short}
    
    pro={'DATE':DATE,'pro_fut_index_long':pro_fut_index_long,'pro_fut_index_short':pro_fut_index_short,'pro_index_ceopt_long':pro_index_ceopt_long,'pro_index_ceopt_short':pro_index_ceopt_short,
      'pro_index_peopt_long':pro_index_peopt_long,'pro_index_peopt_short':pro_index_peopt_short,'pro_stk_fut_long':pro_stk_fut_long,'pro_stk_fut_short':pro_stk_fut_short,'pro_stk_ceopt_long':pro_stk_ceopt_long,
      'pro_stk_ceopt_short':pro_stk_ceopt_short,'pro_stk_peopt_long':pro_stk_peopt_long,'pro_stk_peopt_short':pro_stk_peopt_short}
    
    clientdf=pd.DataFrame([client])
    diidf=pd.DataFrame([dii])
    fiidf=pd.DataFrame([fii])
    prodf=pd.DataFrame([pro])
    
    clientdf=clientdf.head(1)
    diidf=diidf.head(1) 
    fiidf=fiidf.head(1)
    prodf=prodf.head(1)
    
    clientdf.to_csv('RESULT\\CLIENT.csv',index=False,header=False,mode='a')
    diidf.to_csv('RESULT\\DII.csv',index=False,header=False,mode='a')
    fiidf.to_csv('RESULT\\FII.csv',index=False,header=False,mode='a')
    prodf.to_csv('RESULT\\PRO.csv',index=False,header=False,mode='a')
    
    print(csv_file_list[i])

    

