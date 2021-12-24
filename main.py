#欢迎使用！[by link]
import random
import time
print('欢迎进入模拟试验！')
time.sleep(0.8)
print('说明：本程序仿照八下人教版生物书P41页模拟试验,如有条件，建议动手操作体验')
time.sleep(2.2)
print('数据说明：A指XY，B指XX，建议结合12月综合练习生物卷P6 T31理解')
time.sleep(2.5)
print('即将进行随机')
time.sleep(0.5)
in1=int(input('请输入抓取次数：\n'))
in2=int(input('请输入重复试验次数：\n'))
A = 0
B = 0
A1 = 'A'
B1 = 'B'
l1=[]
print('随机过程:')
for i in range(in2):
    print('----------第{}次重复试验----------'.format(i+1))
    for i in range(in1):
        rand_int = random.randint(1，100)
        if rand_int <= 50:
            A = A+1
            print('<{}>'.format(A1), end='')
        elif rand_int >50:
            B = B+1
            print('<{}>'.format(B1), end='')
    print()
    print('----------结束----------')
    print('结果：A{}次,B{}次'.format(A, B))
    l1.append([A,B])
    A=0
    B=0
print(l1)
A=0
B=0
print('处理数据中，请稍后......')
for i in range(len(l1)):
    A=A+l1[i][0]
    B=B+l1[i][1]
time.sleep(2.4)
print('最终结果：\nA共{}次，B共{}次\n由数据可知，A:B基本为1:1，故生男生女概率相同'.format(A,B))
input('按Enter键关闭')
