from lxml import html
import requests

# initial messages detailing instructions
print("Welcome to Python Web Scraper!")
print("Enter a valid url to find the most frequent words on its page.")
print("Enter 'q' to quit the application.")
print("Have fun!")

# each iteration of the loop is one opportunity to enter url, ^q will quit it
user_input=""
while user_input != "^q":
	user_input = input(">")
	# if user didn't input "q" go ahead
	if user_input != "^q":
		# attempt to request the url and parse through its text
		try:
			page = requests.get(user_input)
			tree = html.fromstring(page.content)
			pees = tree.xpath("//p//text()") #just text from <p> tags right now
			all_text = []
			# go through each <p> tag
			for i in pees:
				parsed_text=""
				# go through each char in the text of the <p> tag
				for j in i:
					# if it is a letter or a space, let it through
					if j.isalpha() or j == " ":
						parsed_text += j
				# add all parsed_text to the big initial list
				all_text += parsed_text.lower().split(" ")
			
			# some data type should store one word and its frequency
			no_reps = {}
			for i in all_text:
				if i != "" and i not in no_reps:
					no_reps[i] = 1
				elif i in no_reps:
					no_reps[i] += 1

			tups = [ (v,k) for k,v in no_reps.items() ]
			tups.sort(reverse=True) # natively sort tuples by first element
			for i in tups:
				print(i[1], ": ", i[0], sep="")

			
			print("Find a specific word, or enter '^rs' to do a new search.")
			one_word = ""
			while one_word != "^rs":
				one_word = input(">")
				if one_word != "^rs":
					if one_word in no_reps:
						print("The word", one_word, "appeared", no_reps[one_word], "times.")
					else:
						print("The word", one_word, "does not exist on this page.")

		#some error occurred in all that
		except:
			print("Something went wrong. Try again.")
			