import math
from itertools import combinations

values='23456789TJQKA'
suits='HDCS'

def main():
    cards=[]
    for suit in suits:
        for value in values: 
            cards.append(value+suit)
    
    subsets=set(combinations(cards,5))
    print(len(subsets))
    
    print("by math function", math.comb(52,5))
main()