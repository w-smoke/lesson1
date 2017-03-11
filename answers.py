t=str('')
def get_answer(question):
	question=str(question)
	answers={"Hi": "Hi-Hi", "How are you?": "Fine!", "Bi": "Bi-Bi!!!"}
	a=answers.get(question,'Fuck')
	a=a.lower()
	return a
question_1=str(input("something from (Hi or Bi)"))
t=question_1
while t == "":
	question_1=str(input("something from (Hi or Bi)"))
	t=question_1
print(t)
t = get_answer(question_1)
print(t)