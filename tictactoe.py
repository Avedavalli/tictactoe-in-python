bd={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
x=1
#bd[1:10]=[' ']*9
def displayboard(bd):
    print(bd[7],"|",bd[8],"|",bd[9]," reference ",7," | ",8," | ",9)
    print(bd[4],"|",bd[5],"|",bd[6]," reference ",4," | ",5," | ",6)
    print(bd[1],"|",bd[2],"|",bd[3]," reference ",1," | ",2," | ",3)
'''def testboard():
    bd=['#']
    bd[1:10]=[' ']*9
    displayboard(bd)'''
def playerinp():
    markp1=int(input("enteer 1 or 0"))
    if markp1==1:
        markp2=0
        #return (markp1,markp2)
        posinp(markp1,markp2)
    elif markp1==0:
        markp2=1
        #return (markp1,markp2)
        posinp(markp1,markp2)
    elif markp1!=1 or markp2!=0:
        playerinp()
        
    
def posinp(markp1,markp2):
    '''player=playerinp()
    markp1=player[0]
    markp2=player[1]'''
    print("player 1 mark is",markp1,"p2 is",markp2)
    global x ;l=[i for i in range(1,10)]
    while x<=9:
        
        print(x)
        
        def pos1():
            global x
            p1=int(input("enteer p1 position 1 to 9 "))
        
        #bd.remove(bd[p1])
        #bd.insert(p1,markp1)
            if p1 in l:
                bd[p1]=markp1
                l.remove(p1)
                
                displayboard(bd)
                if bd[1]==bd[2]==bd[3]==markp1 or bd[4]==bd[5]==bd[6]==markp1 or bd[7]==bd[8]==bd[9]==markp1:
                     print("p1 winned in straight at",x,"move")
                     exit()
                         
                elif bd[1]==bd[4]==bd[7]==markp1 or bd[2]==bd[5]==bd[8]==markp1 or bd[3]==bd[6]==bd[9]==markp1:
                     print("p1 winned in vertical at",x,"move")
                     exit()
                     
                elif bd[1]==bd[5]==bd[9]==markp1 or bd[7]==bd[5]==bd[3]==markp1:
                    print("p1 winned in diagonal at",x,"move")
                    exit()
                x+=1   
            else:
                displayboard(bd)
                print("already filled")
                pos1()
        pos1()
        
        def pos2():
            global x
            p2=int(input("enteer p2 position 1 to 9 "))
        #bd.remove(bd[p2])
        #bd.insert(p2,markp2)
            if p2 in l:
                bd[p2]=markp2
                displayboard(bd)
                l.remove(p2)
                if bd[1]==bd[2]==bd[3]==markp2 or bd[4]==bd[5]==bd[6]==markp2 or bd[7]==bd[8]==bd[9]==markp2:
                    print("p2 winned in straight at",x,"move")
                    exit()
                    
                elif bd[1]==bd[4]==bd[7]==markp2 or bd[2]==bd[5]==bd[8]==markp2 or bd[3]==bd[6]==bd[9]==markp2:
                     print("p2 winned in vertical at",x,"move")
                     exit()
                elif bd[1]==bd[5]==bd[9]==markp2 or bd[7]==bd[5]==bd[3]==markp2:
                    print("p2 winned in diagonal at",x,"move")
                    exit()
                x+=1
                
            else:
                displayboard(bd)
                print("already filled")
                pos2()
        if x==10:
            break
        else:
            pos2()
        
print(bd,len(bd))
playerinp()
