import os, glob
from io import StringIO
import pandas as pd
from datetime import datetime


df_final = pd.DataFrame(columns=['Environment', 'Release', 'Tenant', 'Process', 'Status', 'Comment','Date'])
for filename in glob.glob('data/*.csv'):

   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       test_data = StringIO(f.read())
       df = pd.read_csv(test_data, sep=",")

       i = 0
       while i< len(df):
           environment_variable = ""
           release = f.name.split("_")[2]
           date_execution = f.name.split("_")[1]
           date_format = '%d%m%Y'
           date_obj = datetime.strptime(date_execution, date_format)

           if "prod" in f.name:
               environment_variable = "YT1"
           else:
               environment_variable = "YTS1"
           tmp_tenant = " ".join(str(df.loc[[i]]['TENANT']).split())
           tmp_reason = " ".join(str(df.loc[[i]]['REASON']).split())

           tmp_soh = " ".join(str(df.loc[[i]]['SOH']).split())
           the_dict = {'Environment': environment_variable, 'Release': release,'Tenant':tmp_tenant.split()[1],'Process':'SOH','Status':tmp_soh.split()[1],'Comment':'','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)


           tmp_encode = " ".join(str(df.loc[[i]]['ENCODE']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'ENCODE', 'Status': tmp_encode.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           tmp_identify = " ".join(str(df.loc[[i]]['IDENTIFY']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'IDENTIFY', 'Status': tmp_identify.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           tmp_lookup = " ".join(str(df.loc[[i]]['LOOKUP']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'LOOKUP', 'Status': tmp_lookup.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)


           tmp_sp = " ".join(str(df.loc[[i]]['SEARCHANDPICK']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'SEARCHANDPICK', 'Status': tmp_sp.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           tmp_inventory = " ".join(str(df.loc[[i]]['INVENTORY']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'INVENTORY', 'Status': tmp_inventory.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           tmp_ui = " ".join(str(df.loc[[i]]['UPDATE_INVENTORY']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'UPDATE_INVENTORY', 'Status': tmp_ui.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)


           tmp_receiving = " ".join(str(df.loc[[i]]['RECEIVING']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'RECEIVING', 'Status': tmp_receiving.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           tmp_shiping = " ".join(str(df.loc[[i]]['SHIPPING']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'SHIPPING', 'Status': tmp_shiping.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           tmp_packing = " ".join(str(df.loc[[i]]['PACKING']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'PACKING', 'Status': tmp_packing.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           tmp_api = " ".join(str(df.loc[[i]]['API_CALLS']).split())
           the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'API_CALLS', 'Status': tmp_api.split()[1], 'Comment': '','Date':str(date_obj)}
           df_the_dict = pd.DataFrame([the_dict])
           df_final = pd.concat([df_final, df_the_dict], ignore_index=True)

           try:
               tmp_xml = " ".join(str(df.loc[[i]]['XML_PROCESS']).split())
               the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'XML_PROCESS', 'Status': tmp_xml.split()[1], 'Comment': '','Date':str(date_obj)}
               df_the_dict = pd.DataFrame([the_dict])
               df_final = pd.concat([df_final, df_the_dict], ignore_index=True)
           except:
               print('xml')
           try:
               tmp_rt = " ".join(str(df.loc[[i]]['RECEIVING_TAGMANAGMENT']).split())
               the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'RECEIVING_TAGMANAGMENT', 'Status': tmp_rt.split()[1], 'Comment': '','Date':str(date_obj)}
               df_the_dict = pd.DataFrame([the_dict])
               df_final = pd.concat([df_final, df_the_dict], ignore_index=True)
           except:
               print('RECEIVING_TAGMANAGMENT')

           try:
               tmp_st = " ".join(str(df.loc[[i]]['SENDING_TAGMANAGMENT']).split())
               the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'SENDING_TAGMANAGMENT', 'Status': tmp_st.split()[1], 'Comment': '','Date':str(date_obj)}
               df_the_dict = pd.DataFrame([the_dict])
               df_final = pd.concat([df_final, df_the_dict], ignore_index=True)
           except:
               print('SENDING_TAGMANAGMENT')

           try:
               tmp_pa = " ".join(str(df.loc[[i]]['PREMISE_AUTO_CREATION']).split())
               the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'PREMISE_AUTO_CREATION', 'Status':tmp_pa.split()[1] , 'Comment': '','Date':str(date_obj)}
               df_the_dict = pd.DataFrame([the_dict])
               df_final = pd.concat([df_final, df_the_dict], ignore_index=True)
           except:
               print('PREMISE_AUTO_CREATION')


           try:
               tmp_es = " ".join(str(df.loc[[i]]['ENCODE_SUPPLYCHAIN']).split())
               the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'ENCODE_SUPPLYCHAIN', 'Status': tmp_es.split()[1], 'Comment': '','Date':str(date_obj)}
               df_the_dict = pd.DataFrame([the_dict])
               df_final = pd.concat([df_final, df_the_dict], ignore_index=True)
           except:
               print('ENCODE_SUPPLYCHAIN')
           try:
               tmp_inspecting = " ".join(str(df.loc[[i]]['INSPECTING']).split())
               the_dict = {'Environment': environment_variable, 'Release': release, 'Tenant': tmp_tenant.split()[1],
                       'Process': 'INSPECTING', 'Status': tmp_inspecting.split()[1],
                       'Comment': '','Date':str(date_obj)}
               df_the_dict = pd.DataFrame([the_dict])
               df_final = pd.concat([df_final, df_the_dict], ignore_index=True)
           except:
               print('INSPECTING')
           i = i +1

       df_final.to_csv('final_fila.csv', encoding='utf-8', index=False)
       print(df)