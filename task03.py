print('Приятной игры в скрабл!')

eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = abs(int(input('Играем на какой раскладке? Введите 1 - на английской раскладке, либо 0 - на русской: ')))
if N==0:
     print('Русский')
else:
    print('English')
word = input('Введите слово/Enter a word: ').upper()
if N == 1:
	print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
elif N == 0:
	print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
else:
    print('Вы мухлюете! Играйте по правилам!')