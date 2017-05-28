''''
basic levenshtein algorithm implementation 
using dynamic programming
'''

#inputs memoization table, title of the song from spoify playlist, title of song from YT
def fill_table(table,s1,s2):
	#fill first row from 0 to s1.length
	for i in range(0,len(table)):
		table[i][0]=i
	for i in range(0,len(table[0])):
		table[0][i]=i
		
	#fill the rest
	for i in range(1,len(table)):
		for j in range(1,len(table[i])):
            #main step in the algorithm
			min_val=min(table[i-1][j-1],table[i-1][j],table[i][j-1])
			if s1[j-1]==s2[i-1]:
				table[i][j]=min_val
			else:
				table[i][j]=min_val+1
	return table
	
#not yet implemented
def search_whitelist(s2):
	'''
	list of regular expression patters
	with which the string will be compared to
	'''
	patterns=[]
	return false

#returns the title of the yt video that best matches the spotify song
def find_best_string(s1,title_list):
	min=1337
	res=""
	
	#placeholder for whitelist
	if search_whitelist(title_list)==true:
		return getMainTitle
	
	for title in title_list:
		table=fill_table(s1,title)
		if table[len(table)-1][len(table[len(table)-1])-1) < min:
			min= table[len(table)-1][len(table[len(table)-1])-1)
			res=title
	return res