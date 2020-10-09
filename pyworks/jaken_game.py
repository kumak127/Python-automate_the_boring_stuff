from random import randint
from time import sleep

hand={1:"グー",2:"チョキ",3:"パー"}
rule={(1,1):"引き分け",(2,2):"引き分け",(3,3):"引き分け",
      (1,2):"あなたの勝ち",(2,3):"あなたの勝ち",(3,1):"あなたの勝ち",
      (1,3):"あなたの負け",(2,1):"あなたの負け",(3,2):"あなたの負け"
      }
win=0
lose=0

while True:
    print("ジャン")
    sleep(1)
    print("ケン")
    sleep(1)
    user_hand=int(input("1:グー 2:チョキ 3:パー 0:やめる"))
    com_hand=randint(1,3)
    if user_hand==0:
        break
    if user_hand not in  hand:
        continue
    print("あなたは{},わたしは{}".format(hand[user_hand],hand[com_hand]))
    sleep(1)
    if rule[(user_hand,com_hand)]=="あなたの勝ち":
        win+=1
    elif rule[(user_hand,com_hand)]=="あなたの負け":
        lose+=1
    print("{} 勝ち:{} 負け:{}\n".format(rule[(user_hand,com_hand)],win,lose))
    sleep(1)