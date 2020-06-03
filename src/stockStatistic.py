#开发目标
# 1.取每天股票数据，按规则取前30条
# 2.市值递增排序（动态、静态）
# 3.市盈率递增排序
# 4.股价递增排序
# 5.近五个交易日涨幅排序
import tushare as ts
from pandas import DataFrame

#获取当日行情数据
df=ts.get_day_all('2019-04-23')[['code','name','pe','floats','fvalues','industry','change','price','p_change']]

#对股票进行条件排序
dfSort=df.sort_values(by=['pe','fvalues','price'],ascending=[True,True,True])

#取前n行数据，并重置索引,删除原索引
dfData=dfSort[1:100].reset_index(drop=True)



lst=[]#新股列表
listBanstock=[]#st板块列表
listCreate=[]#创业板
#遍历dfsort中数据，获取市值为0的新股数据，并对st与*st股的索引，并对相应数据进行打标签
for index,row in dfData.iterrows():
    if row["fvalues"]==0:
        lst.append(index)
    elif row["name"].find('ST')>=0:
        listBanstock.append(index)
    elif row["code"].startswith('3'):
        listCreate.append(index)


lst.extend(listBanstock)
lst.extend(listCreate)

#删除按列表中索引位置的dataframe数据
for one in lst:
    dfData.drop(one,inplace=True)

#inplace去除空白索引
dfData.reset_index(drop=True,inplace=True)



print(dfData)








#打印结果
#print(dfData[['code','name','pe','floats','fvalues','industry','change','price','p_change']])
#print(df[['code','name','pe','floats','fvalues','industry','change','price','p_change']])



#print(ts.get_hist_data(code='600381',start='2019-04-19'))

