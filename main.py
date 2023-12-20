import openai
import config

while True:
	print ("\n##################################################")
	print ("☺	Made By ImJoseitoh(+5356960902)		☻")
	print ("♦	   Model text-davinci-003		♣")
	print ("##################################################")
	prompt = input("\nIntroduce una pregunta: ")
	if prompt == "exit":
		break
	response = openai.Completion.create(
   		engine="text-davinci-003",
		prompt=prompt,
    	max_tokens=2048
)
	message = response.choices[0].text.strip()
	print(message)