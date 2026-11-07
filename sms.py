[COLOR="Plum"]import requests

while True:
	number = input("Enter the Target's phone number (With the country code, but without '+':")
	message = input('Enter your message: ')

	print(f'Receiver : {number}\nYour Message: {message}')

	print("If you want to continue (1)\nIf you want to change the info above(2)")
	edit=int(input())
	
	if edit==1:
		resp = requests.post('https://textbelt.com/text', {
		'phone': number,
		'message': message,
		'key': 'textbelt',
		})
		response = resp.json()
		if response['success'] == False:
 			print('ERROR : ',response['error'])

		elif response['success'] == True:
 			print('DONE! Your Message ID is:',response['textId'])
		break
	elif edit==2:
		continue
	else:
 		print("Wrong Command!\nBe sure you to check the message info for security")
	continue
[/COLOR]
