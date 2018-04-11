def printBoard(TB):
    print(TB['TL']+'|'+TB['TM']+'|'+TB['TR'])
    print('-+-+-')
    print(TB['ML']+'|'+TB['MM']+'|'+TB['MR'])
    print('-+-+-')
    print(TB['LL']+'|'+TB['LM']+'|'+TB['LR'])
    
def check(TB,P):
    f=0
    if P=='X':
        P='O'
    else:
        P='X'
    if TB['TL']==P and TB['TM']==P and TB['TR']==P or TB['LL']==P and TB['LM']==P and TB['LR']==P or TB['ML']==P and TB['MM']==P and TB['MR']==P or TB['TL']==P and TB['ML']==P and TB['LL']==P or TB['TM']==P and TB['MM']==P and TB['LM']==P or TB['TR']==P and TB['MR']==P and TB['LR']==P or TB['TL']==P and TB['MM']==P and TB['LR']==P or TB['TR']==P and TB['MM']==P and TB['LL']==P:
        print('player',P,' won')
        printBoard(TB)
        f+=1
    return f
       
TB= {'TL': ' ', 'TM': ' ', 'TR': ' ','ML': ' ', 'MM': ' ', 'MR': ' ','LL': ' ', 'LM': ' ', 'LR': ' '}
TBp= {'TL': 'TL', 'TM': 'TM', 'TR': 'TR','ML': 'ML', 'MM': 'MM', 'MR': 'MR','LL': 'LL', 'LM': 'LM', 'LR': 'LR'}
turn='X'
i=0
printBoard(TBp)

while True:
    printBoard(TB)
    print('Player',turn,'turn, What is your move?')
    move=input().upper()
    if(move not in TB.keys())==True:
        print('invaild')
    elif TB[move]==' ':
        if turn=='X':
            TB[move]='X'
            turn='O'
            i+=1
        else:
            TB[move]='O'
            turn='X'
            i+=1
        if i>3:
           y=check(TB,turn)
           if y!=0:
                break
        if i==9:
            printBoard(TB)
            print('Draw')
            break
