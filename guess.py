import random

x = input('請輸入範圍 (底標)')
y = input('請輸入範圍 (高標)')
x = int(x)
y = int(y)
r = random.randint(x, y)
count = 0

while True:
	count += 1 ## 快寫法 for count = count + 1
	test = input("數字猜猜看: ")
	test = int(test)
	
	if test == r:
		print("終於猜對了")
		break
	elif test > r:
		print('比答案大')
	elif test < r:
		print('比答案小')
	print('這是你猜的第',count, '次!')


