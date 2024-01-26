n = input()
mylist = list(map(int , input().split()))
max = max(mylist)
sum = sum(mylist)
#한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환해 로직을 간단하게 할 수 있음
print(sum * 100 / max / int(n))
