import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import chi2

obs1 =[[ 9.55,11.59,15.87,5.79,6.81,5.73],
[10.15,14.88,16.57,5.89,7.19,5.8],
[11.48,14.98,18.70,6.10,7.18,5.87]]

obs2 =[[9.19,10.50,14.80,5.78,6.74,5.64],
[9.43,14.76,16.35,5.72,7.00,5.70],
[10.52,14.62,18.32,6.00,7.13,5.80]]

obs3 =[[13.87,15.00,19.67,6.17,7.10,5.69],
[14.77,15.98,20.01,6.10,6.83,5.66],
[15.83,16.03,20.57,5.91,7.20,5.89]]

obs4 =[[12.86,15.38,19.45,6.10,7.08,5.60],
[14.75,15.87,19.78,6.01,6.80,5.60],
[15.77,15.91,20.40,5.90,7.13,5.86]]

'''
（1）假设检验重要知识
H0:A与B相互独立  H1：A与B不相互独立
若卡方值大于临界值，拒绝原假设，表示A与B不相互独立，A与B相关
函数中re返回为1表示拒绝原假设，0表示接受原假设

（2）参数说明
输入：
alpha --- 置信度，用来确定临界值
data  --- 数据，请使用numpy.array数组
输出：
g     --- 卡方值，也就是统计量
p     --- P值（统计学名词），与置信度对比，也可进行假设检验，P值小于置信度，即可拒绝原假设
dof   --- 自由度
re    --- 判读变量，1表示拒绝原假设，0表示接受原假设
expctd--- 原数据数组同维度的对应理论值

（3）应用场景
要求样本含量应大于40且每个格子中的理论频数不应小于5

理论知识详见博客：
'''
def chi2_independence(alpha, data):
    g, p, dof, expctd = chi2_contingency(data)
    if dof == 0:
        print('自由度应该大于等于1')
    elif dof == 1:
        cv = chi2.isf(alpha * 0.5, dof)
    else:
        cv = chi2.isf(alpha * 0.5, dof-1)
    if g > cv:
        re = 1  # 表示拒绝原假设
    else:
        re = 0  # 表示接受原假设
    return g, p, dof, re, expctd

def run(obs):
    print(np.array(obs))
    alpha1_1 = 0.01  # 置信度，常用0.01，0.05，用于确定拒绝域的临界值
    alpha1_2 = 0.05  # 置信度，常用0.01，0.05，用于确定拒绝域的临界值
    data = np.array(obs)
    g, p, dof, re, expctd = chi2_independence(alpha1_1, data)
    print("置信度为%s时:卡方值=%s,P值=%s,自由度=%s,判读变量=%s." % (alpha1_1, g, p, dof, re))
    g, p, dof, re, expctd = chi2_independence(alpha1_2, data)
    print("置信度为%s时:卡方值=%s,P值=%s,自由度=%s,判读变量=%s." % (alpha1_2, g, p, dof, re))
    print("**************************************************************************")

run(obs1)
run(obs2)
run(obs3)
run(obs4)