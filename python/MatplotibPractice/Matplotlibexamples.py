#使用pandas读取csv文件,并使用matplotlib做图（条形图 饼图）

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pic = pd.read_csv("/media/mlxuan/mlx/darknet_pipeline_inspection/pic.csv",sep = '\ ',names = ['time','size'])#读取csv文件，并指定分隔符和列标签
pic['time']=pd.to_datetime(pic['time'])#将字符串时间转为dataframe的Timestamp格式
pic = pic.set_index('time')      #将time列设为dataframe的索引
pic['size'].max(),pic['size'].min(),pic['size'].mean()#获得统计值，此处是所拍图像的最大值，最小值和平均值

#根据时间，将dataframe切片，划分为多个dataframe，并获得各个子dataframe的统计值
pic1 = pic[pd.to_datetime('02:47:17'):pd.to_datetime('02:48:53')]
pic1.count(),pd.to_datetime('02:48:53')-pd.to_datetime('02:47:17'),pic1['size'].max(),pic1['size'].min(),pic1['size'].mean()
pic2 = pic[pd.to_datetime('02:50:26'):pd.to_datetime('02:51:38')]
pic2.count(),pd.to_datetime('02:51:38')-pd.to_datetime('02:50:26'),pic2['size'].max(),pic2['size'].min(),pic2['size'].mean()
pic3 = pic[pd.to_datetime('05:38:44'):pd.to_datetime('05:41:37')]
pic3.count(),pd.to_datetime('05:41:37')-pd.to_datetime('05:38:44'),pic3['size'].max(),pic3['size'].min(),pic3['size'].mean()
pic4 = pic[pd.to_datetime('05:45:32'):pd.to_datetime('05:48:03')]
pic4.count(),pd.to_datetime('05:48:03')-pd.to_datetime('05:45:32'),pic4['size'].max(),pic4['size'].min(),pic4['size'].mean()

#该函数用来统计各个区间出现的个数[45-55),[55,65)...[85,95)
bins=np.arange(45,99,10)
def filter_fun(x):
    i1,i2,i3,i4,i5=0,0,0,0,0
    for xd in x:
        if bins[0]<=xd<bins[1]:
            i1=i1+1
        if bins[1]<=xd<bins[2]:
            i2=i2+1
        if bins[2]<=xd<bins[3]:
            i3=i3+1
        if bins[3]<=xd<bins[4]:
            i4=i4+1
        if bins[4]<=xd<bins[5]:
            i5=i5+1
    return (i1,i2,i3,i4,i5)
filter_fun(pic1['size'])
pos = [1 - 0.4, 2 - 0.4, 3 - 0.4, 4 - 0.4, 5 - 0.4]


# 作出图像
width = 0.2
data1 = filter_fun(pic1['size'])
plt.bar(pos, data1, width, alpha=0.8, color='g', label='1st area')
plt.bar([p + width for p in pos], filter_fun(pic2['size']), width, alpha=0.8, color='r', label='2nd area')
plt.bar([p + width * 2 for p in pos], filter_fun(pic3['size']), width, alpha=0.8, color='b', label='3rd area')
plt.bar([p + width * 3 for p in pos], filter_fun(pic4['size']), width, alpha=0.8, color='y', label='4th area')
# 加图例
plt.legend(loc='best')
# 设置坐标轴
plt.xticks([p + width * 1.5 for p in pos], ['45-55', '55-65', '65-75', '75-85', '85-95'], fontsize=12)  # 设置坐标的位置和显示值
fig = plt.gca()
fig.spines['top'].set_visible(False)
fig.spines['right'].set_visible(False)

plt.ylabel('Number of images', fontsize=18)
plt.xlabel('Size of the received images(KB)', fontsize=18)

# 打注释
for i in np.arange(0, 5):
    plt.text(pos[i] - 0.1, data1[i] + 0.9, str(data1[i]))
    plt.text(pos[i] - 0.1 + width, filter_fun(pic2['size'])[i] + 0.9, str(filter_fun(pic2['size'])[i]))
    plt.text(pos[i] - 0.1 + width * 2, filter_fun(pic3['size'])[i] + 0.9, str(filter_fun(pic3['size'])[i]))
    plt.text(pos[i] - 0.1 + width * 3, filter_fun(pic4['size'])[i] + 0.9, str(filter_fun(pic4['size'])[i]))
# 保存
plt.savefig('./test3.tif')
# 设置图像大小
plt.figure(figsize=(1000, 2000), dpi=1)


plt.show()


#画pie图，显示各个占比
labels = [u'45KB-55KB',u'56KB-65KB',u'66KB-75KB',u'76KB-85KB',u'86KB-95KB']
sizes = filter_fun(pic['size'])
patches,l_text,p_text = plt.pie(sizes,labels = labels,autopct = '%3.1f%%',pctdistance = 0.6)
plt.axis('equal')
#改变文本的大小
#方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size(13)
for t in p_text:
    t.set_size(10)

plt.savefig('./test4.tif')
# 设置图像大小
plt.figure(figsize=(1000, 2000), dpi=1)
# 保存
plt.show()