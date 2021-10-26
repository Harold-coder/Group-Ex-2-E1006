def print_box(s):

	arr = s.split("\\n")

	maximum = 0
	for i in arr:
		if len(i) > maximum:
			maximum = len(i)

	print('*' * (maximum + 4))
	for i in arr:
		beg = (maximum - len(i))//2
		print('* ' + (' ' * beg) +  i + (' ' * (maximum - len(i) - beg)) + ' *')
	print('*' * (maximum + 4))



word_given = input("Give me a word to box:")

print_box(word_given)

