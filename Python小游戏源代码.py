from random import*
def check(list0,c):
    if c not in list0 :
        print('非常遗憾，您输入的数字不是幸运数字！')
        return 0
    else:
        print('Congratulations！')
        return 1
def mobu(a0,list0):
    for j in range(eval(a0)):
        print('请%d号玩家%s开始：'%(j+1,list1[j]))
        q=int(input('请输入一个数字：'))
        if check(list0,q)==1:
            return 1
list1=[]
list2=[]
b=randint(0,30)
list2.append(b)
a=int(input('请输入幸运数字个数：'))
a1=input('请输入玩家位数：')
for j in range(eval(a1)):
    print('请输入%d号玩家的姓名：'%(j+1))
    k=input('')
    list1.append(k)
print(list2)
m=0
while m==0:
    if mobu(a1,list2)==1:
        m=1
print('GAME OVER!')
