from clint.textui.colored import red, green, magenta, cyan
dict_list = [
  {
    "question" : "How many colors does a standard full RGB keyboard light up in?" ,
    "choices" : {"a" : "17559347" , "b" : "16777216" , "c" : "3" , "d" : "256"} ,
    "correct" : "b"
  },
  {
    "question" : "What is my most listened track on Spotify of all time?" ,
    "choices" : {"a" : "La Vie en Rose - IZONE" , "b" : "Energetic - Wanna One" , "c" : "X1-MA - Produce X !01" , "d" : "BOSS - MCT U"} ,
    "correct" : "b"
  },
  {
    "question" : "How many hours does Sam Cabuay have in Counter Strike?" ,
    "choices" : {"a" : "756 Hours" , "b" : "1585 Hours" , "c" : "2236 Hours" , "d" : "3092 Hours"} ,
    "correct" : "b"
  } 
]

for x in dict_list:
  print (magenta(x['question']))
  print (cyan(x['choices']))
  answer = input()
  if answer == x['correct']:
    print (green("correct"))
  else:
    print (red("wrong"))
