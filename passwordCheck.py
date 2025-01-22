def StringChallenge(strParam):
  import string
  # convert input to string
  strParam = str(strParam)
  # code goes here
  # count length of string
  stringLength = len(strParam)

  # checkign if string is shorter than 7 characters
  if stringLength < 7:
    # print("Password must be longer than 7 characters and shorter than 31 characters. It is currently ", stringLength, " characters.")
    return ("false")

  # checking if string is longer than 31 characters
  if stringLength > 31:
    # print("Password must be longer than 7 characters and shorter than 31 characters. It is currently ", stringLength, " characters.")
    return ("false")

  # checking if "password" is in the provided password
  if "password" in strParam:
    # print("Password cannot contain 'password' in it.")
    return ("false")
  
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
    # print("Password requires at least one capital letter.")
    return ("false")

  if numberFlag == False:
    # print("Password requires at least one number value.")
    return ("false")

  if punctuationFlag == False:
    # print("Password requires at least one punctuation value.")
    return ("false")

  if mathematicalSymbolFlag == False:
    # print("Password requires at least one mathematical symbol.")
    return ("false")

  return "true"

# keep this function call here 
print(StringChallenge(input()))