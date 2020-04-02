with open('email_one.txt') as email:
    email_one = email.read()
with open('email_two.txt') as email:
    email_two = email.read()
with open('email_three.txt') as email:
    email_three = email.read()
with open('email_four.txt') as email:
    email_four = email.read()
#Write a function that can censor a specific word or
#phrase from a body of text, and then return the text.
#Mr. Cloudy has asked you to use the function to
#censor all instances of the phrase learning algorithms from the first email, email_one. Mr. Cloudy doesn’t care how you censor it, he just wants it done.


def censor(word):

    return email_one.replace('learning algorithms','...')

#print(censor('email_one.txt'))



proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#for i in proprietary_terms:
 #   if i=='she':
  #      print(i)
def censor1(word):
    for i in email_two.split():
        for m in proprietary_terms:
            if i==m:
                return email_two.replace(i,'---')
#print(censor1(proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor3(lakirti):
    for p in email_three.split():
        for k in lakirti:
            if p==k:
                return email_three.replace(p,'###')

#print(censor3('email_three.txt'))

#print(email_three)
