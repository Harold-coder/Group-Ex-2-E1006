def find(s, substring):
	length = len(substring)
	i = 0
	while i < len(s):
		end = i + length
		if s[i:end] == substring:
			return i 

		i += 1
	return -1

print(find("ACGT", "AC"))


def find_multi(s, substring): 
    
    list_i = []
    for i in range(len(s)): 
        if s.startswith(substring, i):
           s.count(substring) 
           list_i.append(i) 
    return list_i

print(find_multi("ATGCGCGCGAT", "GCG"))