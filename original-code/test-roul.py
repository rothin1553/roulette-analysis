from random import randint, sample

# always bet on 1-12, 25-36, 15-24
def test_case1(test=1000, win_threshold=350):

    money = 300

    data = {"win": 0, "tie": 0, "loss": 0}
    play_count = []

    for i in range(test):
        roll = randint(0,37)
        if(roll in [13, 14, 0, 37]):
            data["loss"] += 1
            money -= 150

        elif(roll in range(1, 13) or roll in range(25,37)):
            data["tie"] += 1
        
        else:
            data["win"] += 1
            money += 25

        play_count.append({"money": money, "roll": i})

        if(money >= win_threshold or money < 150):
            return money
        
    return 0
            


    print(data)
    print(f"loss: {data['loss']/test*100:.1f}%")
    print(f"tie :{data['tie']/test*100:.1f}")
    print(f"win :{data['win']/test*100:.1f}")
    print(f"w/t :{(data['win']/test*100) + (data['tie']/test*100):.1f}")
    print(f"money: ${money}")

    print(play_count)

# randomly changing bets
def test_case2(test=100, win_threshold=350):

    money = 300

    data = {"win": 0, "tie": 0, "loss": 0}
    play_count = []

    dozens = [i for i in range(1,37)] #1-36

    for i in range(test):
        roll = randint(0,37) # gen 0-37

        pick_dozens = sample([0,1,2], 2)
        not_pick = list(set([0,1,2]) - set(pick_dozens))
        not_a = not_pick[0]*12
        not_b = (not_pick[0]+1)*12
        
        not_values = sample(dozens[not_a:not_b], k=2)
        if(roll in [0, 37] or roll in not_values):
            data["loss"] += 1
            money -= 150

        elif(roll in dozens[pick_dozens[0]*12:(pick_dozens[0]+1)*12] or roll in dozens[pick_dozens[1]*12:(pick_dozens[1]+1)*12]):
            data["tie"] += 1
        
        else:
            data["win"] += 1
            money += 25

        #input(f"{pick_dozens}|{not_pick}|{not_a}|{not_b}|{not_values}||{roll}")

        play_count.append({"money": money, "roll": i})
        if(money >= win_threshold or money < 150):
            #break
            return money

    return 0
    print(data)
    print(f"loss: {data['loss']/test*100:.1f}%")
    print(f"tie :{data['tie']/test*100:.1f}")
    print(f"win :{data['win']/test*100:.1f}")
    print(f"w/t :{(data['win']/test*100) + (data['tie']/test*100):.1f}")
    print(f"money: ${money}")

    print(play_count)


## change win threshold to see difference result 
## win threshold is the case amount to reach before stop betting and to consider winning
## 300 is the initial value; any value greater than 300 can be consider as profit
win_threshold = 325

test = 1000
t={"w":0, "l":0}
t0={"w":0, "l":0}
for i in range(test):
    if(test_case2(test=10000,win_threshold=win_threshold) > 300):
        t["w"]+=1
    else:
        t["l"]+=1
    if(test_case1(test=10000, win_threshold=win_threshold) > 300):
        t0["w"]+=1
    else:
        t0["l"]+=1

print(f"win0: {t0['w']/test*100:.1f}%  |  win: {t['w']/test*100:.1f}%")


"""
run command below in shell to test 25 times
=> clear;for ((i=1;i<26;i++)) do print "test #$i"; python test-roul.py; echo "";  sleep 0.15; done;
"""