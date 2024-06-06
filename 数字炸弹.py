##数字炸弹

from random import randint

correct_num = randint(1,100)##随机生成一个数
is_quit = 'n'##判断是否退出游戏
print('请输入一个1—100的整数（输入x/X/0可直接退出游戏）：')
while is_quit !='y':
    try:
        guess_num = input()##用户输入值

        if guess_num.upper() == 'X':
            guess_num = 0##退出条件
        guess_num = int(guess_num)

        if guess_num == correct_num:
            print('砰！！！恭喜你猜对了*_*')
            is_quit = input('请问是否退出游戏？y/n：')
            while is_quit != 'y' and is_quit != 'n':
                is_quit = input('只能输入y/n，请重新输入：')
            if is_quit == 'n':
                correct_num = randint(1,100)
                print('请输入一个1—100的整数（输入x/X/0可直接退出游戏）：')
        elif 1 <= guess_num < correct_num:
            print('猜小了，请重新输入：')
        elif correct_num < guess_num <=100:
            print('猜大了，请重新输入：')
        elif guess_num == 0:
            is_quit = 'y'##退出循环，结束游戏
        else:
            print('您输入的数字不在1—100范围内，请重新输入：')
    except ValueError:
        ('您输入的不是一个整数，请重新输入：')

print('游戏结束！！！')

        
