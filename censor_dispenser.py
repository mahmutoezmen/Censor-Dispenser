email_one = open("/Users/mahmutozmen/Desktop/censor_dispenser/email_one.txt", "r").read()
email_two = open("/Users/mahmutozmen/Desktop/censor_dispenser/email_two.txt", "r").read()
email_three = open("/Users/mahmutozmen/Desktop/censor_dispenser/email_three.txt", "r").read()
email_four = open("/Users/mahmutozmen/Desktop/censor_dispenser/email_four.txt", "r").read()


def censor1(email,word):

    return email.replace(word,'*'*len(word))


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_list_of_words(email,word_list):
        objected_list = ['']
        objected_list[0] = email
        for i in word_list:
            if i in objected_list[0]:
                objected_list[0]=objected_list[0].replace(i,'REDACTED')
        return objected_list[0]




negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_two_lists_of_words(phrases,email,after=0):

    objected_list = ['']

    objected_list[0] = email

    for i in phrases:

        if i in objected_list[0]:

            object_variable = objected_list[0].find(i)

            for j in phrases:
                if j in objected_list[0][object_variable+1:]:
                    objected_list[0] = objected_list[0][:object_variable + 1] + objected_list[0][object_variable + 1:].replace(i, 'REDACTED')

    return censor_list_of_words(objected_list[0],proprietary_terms)


def censoreAll(email):
  objected_list = ['']
  objected_list2 = ['']
  objected_list3 = []
  objected_list[0] = email
  objected_list[0] = censor_list_of_words(objected_list[0], proprietary_terms)
  objected_list[0] = censor_list_of_words(objected_list[0], negative_words)
  objected_list2[0] = objected_list[0].replace('\n', ' lineBreak ')
  objected_list3 = objected_list2[0].split(' ')
  y = 0
  while y < len(objected_list3) - 1:
    if (objected_list3[y] == 'REDACTED') or (objected_list3[y] == 'REDACTEDe') or (objected_list3[y] == 'REDACTEDous') or (objected_list3[y] == 'REDACTEDly') or (objected_list3[y] == 'REDACTED\'s') or (objected_list3[y] == 'REDACTED.') or (objected_list3[y] == 'REDACTEDs') or (objected_list3[y] == 'REDACTED!') or (objected_list3[y] == 'REDACTEDe.'):
      if y == 0 and (not objected_list3[1] == 'lineBreak'):
        objected_list3[y + 1] = 'REDACTED'
        continue
      if not y == (objected_list3.index(objected_list3[-1])):
        if not objected_list3[y + 1] == 'lineBreak':
          objected_list3[y + 1] = 'REDACTED'
        if not objected_list3[y - 1] == 'lineBreak':
          objected_list3[y - 1] = 'REDACTED'
      y += 2
    y += 1
  objected_list[0] = ' '.join(objected_list3)
  objected_list[0] = objected_list[0].replace('lineBreak', '\n')
  return objected_list[0]
