
numbers = []
def test():
    i = 0
    e= 6
    while i < e:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

test()
print("The numbers: ")

for num in numbers:
    print(num)