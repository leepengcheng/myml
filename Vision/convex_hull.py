#coding:utf-8
'''
Convex Hull
'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial import ConvexHull



pts=np.random.randint(0,100,20).reshape([-1,2])#创建随机点


#将所有的点顺时针连起来(非凸包)
pts=pts[pts[:,1].argsort()] #按照第2列-Y值排序
p0=pts[0]         #取左下角的点作为起始点
pts1=pts[1:,]     #其余的点
vectors=pts1-p0   #每个节点与p0构成的向量集合
vec_x=np.array([1,0]) #x轴向量
cos_vals=vectors.dot(vec_x)/np.linalg.norm(vectors,axis=1) #每个矢量与X轴的夹角余弦值
pts1=pts1[cos_vals.argsort()] #对pts1按照余弦值从小往大排
pts=np.vstack((p0,pts1,p0))   #顺时针连接节点



#使用scipy中的ConvexHull凸包库
hull = ConvexHull(pts)
for s in hull.simplices:
    plt.plot(pts[s, 0], pts[s, 1], 'k-')



sns.set_style("darkgrid")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(pts[:-1,0],pts[:-1,1])  #散点图vec
plt.plot(pts[:,0],pts[:,1],"k--")        #折线图
plt.show() 



