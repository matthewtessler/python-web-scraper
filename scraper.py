from lxml import html
import requests

print("Welcome to Python Web Scraper!")
print("Enter a valid url to find the most frequent words on its page.")
print("Enter 'q' to quit the application.")
print("Have fun!")

user_input=""
while user_input != "q":
	user_input = input(">")
	if user_input != "q":
		try:
			page = requests.get(user_input)
			tree = html.fromstring(page.content)
			pees = tree.xpath("//p//text()")
			all_text = []
			for i in pees:
				all_text.append(i.lower().split(" "))
			print(all_text)

		except:
			print("Something went wrong. Try again.")
			