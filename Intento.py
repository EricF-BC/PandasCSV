import pandas as pd

datos =pd.read_csv("BA02210713.TCL", header=None, names = ["Pais", "Año", "nose", "53","NUll","Nose", "CLP","Fecha2","a","b","c", "d","e","f","h","i","j","k","l","m","n","o","p"])

df=pd.DataFrame(datos)

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

df = df.drop(df.index[0])
df = df.drop(['nose', '53','NUll','Fecha2','a','e', 'f', 'h', 'i', 'j', 'k','l','m', 'n', 'o'], axis = 1)
# df =df.loc[df['Año']== 20210713.0, 'Año']='2021/07/13'
df.Año= df.Año.replace({20210713.0: "2021/07/13"})

pd.set_option('display.float_format','{:.0f}'.format)

# for i in range(len(df))
print(df) 





# print(df.loc [:, df.notnull().all()]) 
