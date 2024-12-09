import pandas as pd
import os
#import the library pandas and os for read and edit the archives

arquivos = os.listdir('plani') #this line read the folder 'plani'

df_consolidado = pd.DataFrame() #create a data frame inside the variable

for excel in arquivos: #create a repetion in 'arquivos' 
    segmento, pais = excel.replace('.Xlsx', '').split('-') #removes '.Xlsx' and split the filename by '-' 
    df = pd.read_excel(f'plani/{excel}') #read the contents of the Excel file
    df.insert(0, 'segmento', segmento) #add in index '0'
    df.insert(1, 'pais', pais) #add in index '1'
    #these two 'df.insert' add the 'segmento' and 'pais' values as new columnsn to the DataFrame 'df'
    

    df_consolidado = pd.concat([df_consolidado, df]) #append the 'df' to 'df_consolidado'


df_consolidado.to_excel('report-consolidado.xlsx', index=False, sheet_name='report consolidado') #save the file to your local folder
