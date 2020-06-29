#model#
import random

#deta#
allcard = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
table = []
player1 = []
player2 = []
end = len(allcard)

#program#
input("按下 enter 键后开始模拟:")
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

#print#
print("player1",player1,len(player1))
print("player2",player2,len(player2))
print("table",table,len(table))

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
                print("player1",player1,len(player1))
                print("player2",player2,len(player2))
                print("table",table,len(table))
                print("turn",turn)
                while loop1 == 1 and len(table) > chack:
                    if table[-1] == table[-1 - chack]:
                        temp = table[(-1 - chack):-1] + [table[-1]]
                        del table[(-1 - chack):-1]
                        del table[-1]
                        temp.reverse()
                        player1 = player1 + temp
                        loop1 = 0
                        out2 = 0
                        print("player1",player1,len(player1))
                        print("player2",player2,len(player2))
                        print("table",table,len(table))
                    else :
                        chack = chack + 1
                chack = 1
                out1 = 0
            while out2 == 1:
                temp = [player2[0]]
                table = table + temp
                del player2[0]
                turn = turn + 1
                print("player1",player1,len(player1))
                print("player2",player2,len(player2))
                print("table",table,len(table))
                print("turn",turn)
                while loop2 == 1 and len(table) > chack:
                    if table[-1] == table[-1 - chack]:
                        temp = table[(-1 - chack):-1] + [table[-1]]
                        del table[(-1 - chack):-1]
                        del table[-1]
                        temp.reverse()
                        player2 = player2 + temp
                        loop2 = 0
                        out1 = 0
                        print("player1",player1,len(player1))
                        print("player2",player2,len(player2))
                        print("table",table,len(table))
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
                print("player1",player1,len(player1))
                print("player2",player2,len(player2))
                print("table",table,len(table))
                print("turn",turn)
                while loop2 == 1 and len(table) > chack:
                    if table[-1] == table[-1 - chack]:
                        temp = table[(-1 - chack):-1] + [table[-1]]
                        del table[(-1 - chack):-1]
                        del table[-1]
                        temp.reverse()
                        player2 = player2 + temp
                        loop2 = 0
                        out2 = 0
                        print("player1",player1,len(player1))
                        print("player2",player2,len(player2))
                        print("table",table,len(table))
                    else :
                        chack = chack + 1
                chack = 1
                out1 = 0
            while out2 == 1:
                temp = [player1[0]]
                table = table + temp
                del player1[0]
                turn = turn + 1
                print("player1",player1,len(player1))
                print("player2",player2,len(player2))
                print("table",table,len(table))
                print("turn",turn)
                while loop1 == 1 and len(table) > chack:
                    if table[-1] == table[-1 - chack]:
                        temp = table[(-1 - chack):-1] + [table[-1]]
                        del table[(-1 - chack):-1]
                        del table[-1]
                        temp.reverse()
                        player1 = player1 + temp
                        loop1 = 0
                        out1 = 0
                        print("player1",player1,len(player1))
                        print("player2",player2,len(player2))
                        print("table",table,len(table))
                    else :
                        chack = chack + 1
                chack = 1
                out2 = 0
print("turn",turn)
input("\n\n按下 enter 键后退出。")