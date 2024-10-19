from telnetlib import theNULL

more = [x + 1 for x in [1, 2, 3, 4]] #x takes on values 1, 2, 3, and 4.
print() #the value of more at this point is [2, 3, 4, 5]

def square(n:int)-> int: # n=1 returns 1, n=2 returns 4, n=3 returns 9, n=4 returns 16.
    return n*n

squares = [square(x) for x in [1, 2, 3, 4]]
print() #squares is [1, 4, 9, 16]. This is each n**2.

def check(n:int) -> bool: # n=0, return None, n=1, return None, n=2, return None, n=3, return 3, n=4 return 4
    return n>2

answer = [x for x in range(5) if check(x)] #answer: [3, 4]
print()

def inc(m: int)-> int: #
    return m+1      #call to 0: m is none & return none, call to 1: m is none  & return none, call to 2: m is none & return none
                    #call to 3: m is 3 & return 4, call to 4: m is 4 & return 5

def check(n:int) -> bool:
    return n>2     #call to 0: n is 0, call to 1: n is 1, call to 2: n is 2, call to 3: n is 3, call to 4: n is 4

answer = [inc(x) for x in range(5) if check(x)]    # answer: [4,5]
print()


def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num
    return total

#num = 4 & total = 4. num = 9 and total = 13. num = 2 and total = 15. num = 1 and total = 16
#total at end of loop body = 16, and num = 1.
result = tally([4, 9, 2, 1])

def copy(nums: list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
    return new_list
# idx = 0, and new list is [4]. idx = 1, and new list is [4, 9]. idx = 2, and new list is [4, 9, 2]. idx = 3, and new list is [4, 9, 2, 1].
# This loop differs from above because this creates a copy and outputs a copy of the list, while the loop above this loop
# ^ is an integer with value of the sum of the list elements.
result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)
    return new_list
# new list = [5, 10, 3, 1]
result = increment_all([4, 9, 2, 1])


