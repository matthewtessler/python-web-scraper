from lxml import html
import requests

# initial messages detailing instructions
print("Welcome to Python Web Scraper!")
print("Enter a valid url to find the most frequent words on its page.")
print("Enter 'q' to quit the application.")
print("Have fun!")

# each iteration of the loop is one opportunity to enter url, q will quit it
user_input=""
while user_input != "q":
	user_input = input(">")
	# if user didn't input "q" go ahead
	if user_input != "q":
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
			text = []
			#now parse through that big list and take out any blanks
			for i in all_text:
				if i != "":
					text.append(i)
			print(text)
		#some error occurred in all that
		except:
			print("Something went wrong. Try again.")
			