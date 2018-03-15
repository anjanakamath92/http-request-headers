import requests


url = 'http://ec2-34-207-132-244.compute-1.amazonaws.com/'
headers = {'X-Authorization-Date': '2018-03-15', 'X-Session-Id': 'aS95L0ZQUGJYSFE4N0NReE5RRUhTaWdKS3VzMTZxaVNLY1dBbHRhcmZWUXIyWnpQTWtWMGFkNzU5c1c3cGJoSWRMNDdhNzR2WW1BT0VYdGlESjdxaTFWZWJmWTZtNGt3N2JQWDIwSjdIbVV6NFRqeHdhbkNnZ0VKZzdTWS9COFFuOGdacGQzWnhaTDNORUhscWQ0SzQzeVRpNVd1ZHBTdUwzYW8yNHpkZ2ZUTmFXQXFaMHlwNEZuUGI3em9LTnc3b2tLTkE4L2hiNHdoZ1IrcTV4eWdxTlcyUjJmRnY3bDlNbjF1VkIyOGZLMD0tLUFRRWZVSzlmeG1xR0ErVWphSmxLY0E9PQ%3D%3D--9a8b0bda619fa0c2f0b0168c6c76b1d8f2afcc80', 'X-Signature-AllComp':'6b648170fd15a7d0f557905311b9cca48f67b5ab'}

for i in range(1,10):
	response = requests.get(url, headers=headers)
	print(response.content)
