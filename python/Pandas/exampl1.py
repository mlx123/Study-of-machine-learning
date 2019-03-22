#csv读取  有很多的参数可供选择 常用的见下面  pd.read_csv
#数据清洗 1.利用bool索引去掉不满足条件的样本   result[result['Region'].str.contains('Region')]  s2 = s[(s>0) & (s<1)]


2.对某些特殊样本的处理，如字符串'-nan'

#数据分离：将字符串和数字混合的数据保留数字

#利用某种函数对全部的样本批量处理



lines=15  
#skiprows表示要跳过几行   error_bad_lines坏行是删除还是引发错误  names列标签  sep读取时的分隔符
result = pd.read_csv('1.csv', skiprows=[x for x in range(lines)] ,error_bad_lines=False, names=['Region','AvgIOU','class','obj', 'no obj', '0.5R', '0.75R', 'images'],sep= ':')
result=result[result['Region'].str.contains('Region')]#利用bool索引排除不满足条件的样本（不包含region字符串则认为不满足条件）
renew = result

#获得某一列数据中的数字
renew['AvgIOU'] = renew['AvgIOU'].str.split(',')
renew['AvgIOU'].dropna()#去掉NaN
def f12(x):
    try:
        return x[0]
    except:
        return x
renew['AvgIOU']  = renew['AvgIOU'].apply(f12)

#对特殊字符串-nan的特殊的处理：将其转为np.nan,然后利用上下文填充
def f13(x):
    if x==' -nan':
        return np.nan
    try:
        return float(x)
    except:
        return np.nan
renew['AvgIOU']  = renew['AvgIOU'].apply(f13)
renew['AvgIOU'] = renew['AvgIOU'].fillna(method='bfill')

#将数据类型转为float
renew['AvgIOU'] = renew['AvgIOU'].astype(float)

s = renew['AvgIOU']
s2 = s[(s>0) & (s<1)]#利用bool索引获得指定的数据


#取一定范围内的均值作图，可以减少离群点的影响等
def SerAve(ser,step):
    ser2=pd.Series([])
    for i in range(int(ser.size/step)):
        ser2[i]=ser.iloc[i*step:i*step+step].mean()
    return ser2
s4 = SerAve(s2,1000)

#作图
plt.figure(figsize=(90,50))
plt.plot(s4,'r')
plt.plot(s4+0.1,'b')
plt.show()
plt.savefig('./test4.tif')
