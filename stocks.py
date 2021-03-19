import stockquotes as s
import matplotlib.pyplot as plt 
import numpy as np
st=input("Stock:")
re=s.Stock(st).historical
for k in range(len(re)):
 print(re[k]["date"].date(), "Open: {}".format(re[k]["open"]) + " Close: {}".format(re[k]["close"]) + " High: {}".format(re[k]["high"])+ " Low: {}".format(re[k]["low"]))

uiu=[]
uiu1=[]

for uu in range(len(re)):
 uiu.append(int(re[-uu]["close"]))
 uiu1.append(uu)
plt.plot(  uiu1,uiu)
plt.title(st)
plt.xlabel("Days")
plt.ylabel("Dollars")
plt.show()

