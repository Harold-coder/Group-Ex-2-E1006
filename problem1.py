def piggify(word):
	vowels = 'aeiou'
	i = 0
	middle_part = ""
	while i<len(word):
		if word[0] in vowels:
			return (word + 'yay')
			break
		else: 
			if word[i] not in vowels:
				middle_part += word[i]

			else:
				beg_part = word[i:]
				return(beg_part + middle_part + 'ay')
				break
			i += 1


while True:
	word_given = input("Give a word:")
	if word_given != '.':
		print(piggify(word_given))
	else:
		print("peace out")
		break




