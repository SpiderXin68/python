from random import*
def check(list0,c):
    if c not in list0 :
        print('非常遗憾，您输入的数字不是幸运数字！')
        print('*'*35)
        return 0
    else:
        print('Congratulations！')
        print('*'*16)
        return 1
def mobu(a0,list0):
    for j in range(eval(a0)):
        print('请%d号玩家%s开始：'%(j+1,list1[j]))
        q=int(input('请输入一个数字：'))
        if check(list0,q)==1:
            return 1

print('*'*30,'幸运星争霸赛','*'*30)
print('*游戏规则：首先输入幸运数字的起始点和终止点，系统会从这个范围内自动生成一个幸运数字。接着输入所参与玩家数，并依次输入你们的名字。最后就是各位玩家依次输入一个数字，直到我们的幸运星玩家产生，让我们看看最后花落谁家。')
print('快和你们的小伙伴一起来挑战吧！\n')
print('*温馨提示：抵制不良游戏，拒绝盗版游戏；注意自我保护，谨防受骗上当；适度游戏益脑，沉迷游戏伤身；合理安排时间，享受健康生活\n')
print('*出版单位：阿鑫工作室    著作人：阿鑫')
print('*'*30,'幸运星争霸赛','*'*30,'\n')
list1=[]
list2=[]
x=int(input('请输入幸运数字的起始点：'))
y=int(input('请输入幸运数字的终止点：'))
print('幸运数字已生成！')
if x>=y:
    print('输入错误，请重新输入！')
    x=int(input('请输入幸运数字的起始点：'))
    y=int(input('请输入幸运数字的终止点：'))
b=randint(x,y)
list2.append(b)

a1=input('请输入玩家位数：')
for j in range(eval(a1)):
    print('请输入%d号玩家的姓名：'%(j+1))
    k=input('')
    list1.append(k)
m=0
while m==0:
    if mobu(a1,list2)==1:
        m=1
        print('本次游戏的幸运数字是%d,嗨嗨嗨！'%(b))
print('******GAME OVER!******')
