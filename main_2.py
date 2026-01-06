'''
rock=1
paper=-1
scissor=0
'''
import random
server= random.choice([1,-1,0])
youstr=input("enter your choice :")
youdict={"r":1,
         "p":-1,
         "s":0}
reversedict={1:"rock",
            -1:"paper",
             0:"scissor"}
you =youdict[youstr]

#By now we have 2 numbers(variables), you and computer 

print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[server]}")

if(server== you):
    print("its a draw")

else:
    if (server==1 and you ==-1 ): ##rock 
        print("you win!")
    elif (server==1 and you ==0 ):
        print("you lose!")
    elif (server==-1 and you ==0 ): ## paper
        print("you win!")
    elif (server==-1 and you ==1 ):
       print("you lose!")
    elif (server==0 and you ==1 ): ## scissor
        print("you win!")
    elif (server==0 and you ==-1 ):
        print("you lose!")
    else:
        print("something went wrong!")
        