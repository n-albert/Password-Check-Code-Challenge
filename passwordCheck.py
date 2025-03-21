def StringChallenge(strParam):
  import string
  # convert input to string
  strParam = str(strParam)

  # find the length of a string
  stringLength = len(strParam)

  failing_conditions = []

  # checking if string is shorter than 7 characters
  if stringLength < 7:
    failing_conditions.append(f"Password must be longer than 7 characters and shorter than 31 characters. It is currently {stringLength} characters long.")
    # return ("false")

  # checking if string is longer than 31 characters
  if stringLength > 31:
    failing_conditions.append(f"Password must shorter than 31 characters. It is currently {stringLength} characters long.")
    # return ("false")

  # checking if "password" is in the provided password
  if "password" in strParam:
    failing_conditions.append("Password cannot contain 'password' in it.")
    #return ("false")
  
  # convert string to set to check for individual character criteria
  stringSet = set(strParam)

  capitalLetterFlag = False
  numberFlag = False
  punctuationFlag = False
  mathematicalSymbolFlag = False

  for character in strParam:
    # check if punctuation
    if character in string.punctuation:
      punctuationFlag = True
    # check if number
    if character.isnumeric():
      numberFlag = True
    # check if capitalized
    if character.isupper():
      capitalLetterFlag = True
    if character in ["+", "-", "/", "x", "*", "%", "="]:
      mathematicalSymbolFlag = True
    
  if capitalLetterFlag == False:
    failing_conditions.append("Password requires at least one capital letter.")
    # return ("false")

  if numberFlag == False:
    failing_conditions.append("Password requires at least one number value.")
    # return ("false")

  if punctuationFlag == False:
    failing_conditions.append("Password requires at least one punctuation value.")
    # return ("false")

  if mathematicalSymbolFlag == False:
    failing_conditions.append("Password requires at least one mathematical symbol.")
    # return ("false")

  if failing_conditions:
    print(f"The password {strParam} fails under these conditions: {failing_conditions}")
    return ("false")
  else:
    print(f"The password {strParam} passes under all conditions.")
    return "true"

# uncomment below line if you want to enter your own password
# print(StringChallenge(input()))

# test cases code

password_test_cases = [
  'password',
  'Appolonius_Jt0',
  'Januz_password',
  'Ordinateur0r',
  'G50mb-ntpass',
  'QuantPassW2+',
  'Kenelm-passW2-'
]

for test_case in password_test_cases:
  print(StringChallenge(test_case))