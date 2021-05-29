
introduction=input("Please introduce yourself.")

count=0
wordCount=0

for intro in introduction:
	print(intro)
	count=count+1
	if(intro == " "):
		wordCount = wordCount + 1

print()

print(count)

print()

print(wordCount)