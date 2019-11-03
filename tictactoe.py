board=[["-" for i in range(3)] for i in range(3)]
def alleq(l,player=False):
        return l[0]==l[1]==l[2]==player
def myinput(x,y):
    return (x,y) if board[x][y]=='-' else myinput(int(input("Enter an x value\n")),int(input("Enter a y value\n")))
def gameplay(player):
    (x,y)=myinput(int(input("Enter an x value\n")),int(input("Enter a y value\n")))
    board[x][y]=player
    [print(i) for i in [j for j in board]]
    return (not alleq( [alleq(w,player) for w in [[board[x][i] for i in range(0,3)],[board[i][y] for i in range(0,3)],
            [board[i][j] for i in range(0,3) for j in range(0,3) if i+j==2]]]    )) or alleq([board[i][i] for i in range(0,3)],player)
def playloop(num,player):
    return (player+' wins!') if gameplay(player) else ( playloop(num+1,'O' if player=='X' else 'X') if num<9 else "It's a draw!")
print(playloop(1,'X'))