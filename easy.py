#accurate#
#deta#
countt = 0
count = 100000
all = []
time = 0
p1w = 0
p2w = 0
persent0 = 0.00
persent1 = 0.00
#programe#
temp = input("\n\n输入模拟次数:")
count = int(temp)
input("按下 enter 键后开始模拟:")
load = count
while count > 0:
    count = count - 1
    countt = countt + 1
    #model#
    import random
    #deta#
    allcard = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
    table = []
    player1 = []
    player2 = []
    end = len(allcard)
    #progran#
    while end > 0:
        catch = random.randint(0,end-1)
        temp = [allcard[catch]]
        player1 = temp + player1
        del allcard[catch]
        end = len(allcard)
        catch = random.randint(0,end-1)
        temp = [allcard[catch]]
        player2 = temp + player2
        del allcard[catch]
        end = len(allcard)
    #program
    loop1 = 0
    loop2 = 1
    chack = 1
    turn = 0
    while len(player1) > 0 and len(player2) > 0 :
        if loop1 == 0 and loop2 == 1:
            loop1 = 1
            while len(player1) > 0 and len(player2) > 0 and loop1 == 1 and loop2 == 1:
                out1 = 1
                out2 = 1
                while out1 == 1:
                    temp = [player1[0]]
                    table = table + temp
                    del player1[0]
                    turn = turn + 1
                    while loop1 == 1 and len(table) > chack:
                        if table[-1] == table[-1 - chack]:
                            temp = table[(-1 - chack):-1] + [table[-1]]
                            del table[(-1 - chack):-1]
                            del table[-1]
                            temp.reverse()
                            player1 = player1 + temp
                            loop1 = 0
                            out2 = 0
                        else :
                            chack = chack + 1
                    chack = 1
                    out1 = 0
                while out2 == 1:
                    temp = [player2[0]]
                    table = table + temp
                    del player2[0]
                    turn = turn + 1
                    while loop2 == 1 and len(table) > chack:
                        if table[-1] == table[-1 - chack]:
                            temp = table[(-1 - chack):-1] + [table[-1]]
                            del table[(-1 - chack):-1]
                            del table[-1]
                            temp.reverse()
                            player2 = player2 + temp
                            loop2 = 0
                            out1 = 0
                        else :
                            chack = chack + 1
                    chack = 1
                    out2 = 0
        else :
            loop2 = 1
            while len(player1) > 0 and len(player2) > 0 and loop1 == 1 and loop2 == 1:
                out1 = 1
                out2 = 1
                while out1 == 1:
                    temp = [player2[0]]
                    table = table + temp
                    del player2[0]
                    turn = turn + 1
                    while loop2 == 1 and len(table) > chack:
                        if table[-1] == table[-1 - chack]:
                            temp = table[(-1 - chack):-1] + [table[-1]]
                            del table[(-1 - chack):-1]
                            del table[-1]
                            temp.reverse()
                            player2 = player2 + temp
                            loop2 = 0
                            out2 = 0
                        else :
                            chack = chack + 1
                    chack = 1
                    out1 = 0
                while out2 == 1:
                    temp = [player1[0]]
                    table = table + temp
                    del player1[0]
                    turn = turn + 1
                    while loop1 == 1 and len(table) > chack:
                        if table[-1] == table[-1 - chack]:
                            temp = table[(-1 - chack):-1] + [table[-1]]
                            del table[(-1 - chack):-1]
                            del table[-1]
                            temp.reverse()
                            player1 = player1 + temp
                            loop1 = 0
                            out1 = 0
                        else :
                            chack = chack + 1
                    chack = 1
                    out2 = 0
    all = all + [turn]
    if len(player1) == 0:
        p2w = p2w + 1
    else :
        p1w = p1w + 1
    persent0 = 1 - (count / load)
    persent0 = "{:.3f}".format(persent0)
    persent0 = float(persent0)
    if persent1 != persent0:
        temp = persent0 * 1000
        temp = int(temp)
        temp = temp / 10
        print("    loading.....    ","已完成",(temp),"%")
        persent1 = persent0
maxturn = max(all)
minturn = min(all)
while len(all) > 0:
    time = time + all[0]
    del all[0]
everange = time // countt
print("模拟次数",countt)
print("平均回合数",everange)
print("最多回合数",maxturn)
print("最少回合数",minturn)
print("玩家1获胜次数",p1w)
print("玩家2获胜次数",p2w)
input("按下 enter 键后退出:")