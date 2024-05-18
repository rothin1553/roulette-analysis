from random import randint

def roll():
    return randint(0,37)

doz_bet = [i for i in range(25)]
row1 = [i for i in range(1,37,3)]
row3 = [i for i in range(3,37,3)]

def one_bet(money):
    money -= 100
    rolled = roll()
    if(rolled in doz_bet):
        money+=75
    if(rolled in row1 or rolled in row3):
        money+=75

    return money


def play(begin_amt, target_amt):
    total_play = 0
    while(begin_amt < target_amt and begin_amt >= 100):
        begin_amt = one_bet(money=begin_amt)
        total_play+=1

    return {
        "win"   : begin_amt >= target_amt,
        "plays" : total_play
    }


def test1(begin_amt=250, target_amt=350, test_count=1000):
    total_bet = 0
    total_win = 0
    for i in range(test_count):
        one_play = play(begin_amt=begin_amt, target_amt=target_amt)
        if(one_play["win"]):
            total_win+=1
            total_bet+=one_play["plays"]

    return {
        "win%": total_win/test_count,
        "avg. plays": total_bet/total_win
    }

begin = 100
target = 200
# while(test1(begin, target)["win%"] < 0.8):
#     begin = randint(100, 2000)
#     target = randint(begin+100, begin+randint(100,500))
#     print(begin, target)

while(test1(begin, target)["win%"] < 0.6):
    begin = randint(100, 2000)
    target = begin+200
    print(begin, target)

print(f"testing with ({begin}, {target}): winning ${target-begin}")
print(test1(begin_amt=begin, target_amt=target))