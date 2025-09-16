from itertools import permutations

def main():
    letters=['b','o','b','a']
    perms=set(permutations(letters))
    count=0
    for perm in perms:
        print(perm)
        pretty_perm="   ".join(perm)
        print(pretty_perm)
        count=count+1
        if count==2:
            break
main()