import random
word = random.choice(open('word.txt').read().split()).strip()

print(word)

wrong_count = 0
underscores = ['_'] * len(word)

while True:
  print(underscores)
  letter = input("what is your letter? : ").lower()
  if letter not in word.lower():
    wrong_count = wrong_count + 1
  else:
    for i in range(len(word)):
      if (word[i] == letter) or (word[i].lower() == letter):
          underscores[i] = letter
  if '_' not in underscores:
    print("the word was ",  word)
    print("you won!")
    break
  if wrong_count == 6:
    print("the word was", word)
    print("you lost :(")
    break
