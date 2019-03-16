import pandas as pd

1.DataFrame
#取值
##pandas取一列得到Series结构,取两列得到DataFrame结构，此时将列标签看成key,dataframe是字典结构
#dataframe作为字典时，只能用key获得对应的列，不能用类似numpy的切片索引形式（a:b:c  从a到b以c为间隔）
age = df['Age']#得到Series
age = df[['Age','Name']]#得到DataFrame结构
#将dataframe看作是二维的numpy.array,第一维是行的索引，第二维是列的索引，可以使用切片形式
##取一行
 df.iloc[位置]用该行的位置0 1 2...来指定要取的行
 df.loc[索引值] 用索引值来索引
#取某些行列
 #将dataframe看成二维的numpy.array,通过指定行 列的切片来索引某些行列
 df.iloc[行的位置切片，列的位置切片]或df.loc[行的索引切片，列的标签切片]
如df.loc['Cumings, Mrs. John Bradley (Florence Briggs Thayer)','Survived']

#bool类型的索引
此时将dataframe看作二维数组格式，应用来广播原则
boolDataframe = df['money']>40得到一个与df['money']的shape完全相同的bool类型的二维数组
df[boolDataframe]用boolDataframe中的值作为索引，为true的留下，为false的拿开
#用bool的索引来统计个数 （df['Age'] > 70).sum()  = df[df['Age'] > 70].info()中的信息

#高級的索引isin   query  where
df.isin()返回與df的shape相同的bool掩模，可用該掩模選出符合條件的元素
df.where(條件，條件不滿足的辦法)符合條件的不動，不符合條件的則爲Nan或者xx
df.query('條件') 符合條件的留下


#设置DataFrame的索引
df.set_index('标签名')#索引不是普通的放在第一列的标签，而是整个表格的索引，可用其取出dataframe的样本。设置为索引的标签不能在当作列标签来使用



#属性
df.info()   df.columns
df.values #将df展开为np.array
df.describe() #得到dataframe的基本统计特性 =df.mean()  df.max()  df.min()  df.count()等
.value_counts(ascending     bins) 統計出現的次數
pd.crosstab()計數

df.isnull()判斷NaN  df.fillna()#指定缺失值填充方式
#運算
##增加刪除
s1.append(s2)  df.assign()新增一列  pd.concat([df1,df2],axis= )  pd.merge(df1,df2,on ='數據合並的鍵' ,how = '合並方式')或指定新的列並賦值   如s['j']=50  df.loc[][] =
del s1['A']       s.drop(axis= ,inplace = )  axis指定刪除的是行還是列
df.drop_duplicates(subset = '按照該列去掉重復的值')去掉重復的值
#将多列合并为一列或者将一列拆分
参考https://blog.csdn.net/mingkoukou/article/details/82867218
合并：pd.melt  #将value_vars中指定的多列合并为一列
#排序
df.sort_values(by = [按照哪些列排序]，ascending = [排序方式]，inplace = )

#對每一行或每一列的數據執行相同的操作
df.apply(函數f,axis = 'xxx')

#分組
pd.cut(數據,bins,label = )

2.Series
Series同时可以进行np.array和dict的操作（因为pandas就是基于numpy构建的）

#取数据
  向numpy一样且切片索引(遇见,则换维度，没有填写则使用默认值)：s[:5]
  向字典一样使用Series的索引当作key来取数据：s['Name']

#运算
  向numpy一样运算（numpy的索引是正整数0 1 2..,Series的索引是我们设置的）： 如广播（age = age + 10  age = age *10），数值统计（age.mean()）

3.groupby
groupby的返回的結果是dataframe結構
#第一階段split :groupby()
列名;  ['標籤1'，'標籤2']構造多級索引結構  level=n按照第n個索引來split,n>=1時要求dataframe是多級索引結構
#第二階段 apply  groupby().xx
常規的sum mean等  aggregate()  get_group('該標籤中的某一實例')只顯示某些實例
size()得到索引中每種組合出現的次數   describe  得到表格的統計特性

#取分割後的列，並計算其統計特性等  df.groupby('Sex')['Surived'].mean()

4.統計pandas兩個特徵（兩個列標籤之間的關系）
cow()斜方差 df.corr()特徵間的相關系數

5.數據透視表
df.pivot(index='行索引'，colums = '列標籤',value = '要統計的屬性'，aggfunc= '統計該屬性的什麼值')

6.繪圖
df.plot(kind = '') 默認折線圖，bar繪制條形圖，hist繪制直方圖

7.時間操作
#
把字符串中的字符串轉爲Time格式：pd.to_datetime(Series) ,pd.Timestamp("時間")
把表格中的時間作爲索引 pd.read_csv('xx.csv',index_col=,parse_dates=)
#用時間作爲索引取值

8.對字符串的操作
