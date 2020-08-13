from itertools import permutations
import sys
import time

in_word = sys.argv[1]
already_seen = []
if len(sys.argv) > 2:
    already_seen = sys.argv[2:]

eng_dict = open("english3.txt", "r").read().split("\n")
eng_dict_gen = (x for x in eng_dict)
p = permutations(in_word)
found = False

perm_arr = []

for tup in list(p):
    perm_arr.append(''.join(tup).lower())

perm_arr.sort()

perm_arr = list(dict.fromkeys(perm_arr))
count = 0
t1 = time.time()


while(count < len(eng_dict)):
    if found == False:
        w = str(next(eng_dict_gen))
        for word in perm_arr:
            if word == w and word not in already_seen:
                found = True
                print(w)
                break
        count = count+1
    else:
        break

if found == False:
    print("sorry..not found")

t2 = time.time()
print(f"Time Elapsed: {t2-t1} seconds")
