for i in range(1,101):
	while i%7 == 0 or i%10 == 7 or i//10 == 7:
		continue
	print(i)
	print('\n')
	
