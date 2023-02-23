import numpy
print('hello')

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r'C:\Users\zxy08\PycharmProjects\pythonProject\C_i1.xlsx')
data1=df['综合评价值'].values
data1=data1.tolist()
df2=pd.read_excel(r'C:\Users\zxy08\PycharmProjects\pythonProject\Tsallis.xlsx')
data2=df2['综合评价值'].values
data2=data2.tolist()
#data1.sort(reverse=True)
print(data1)
print(data2)
x=list(range(1,265))
print(x)
plt.title('Line Chart of Data1 and Data2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,data1,marker='o',markersize=3)
plt.plot(x,data2,marker='o',markersize=3)
plt.legend(['Data1','Data2'])
plt.show()
print('modified')