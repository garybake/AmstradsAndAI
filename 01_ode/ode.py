"""
ODE - PAT HALL, 2/86
Code is written to be close to original so not pythonic
"""
import random

from ode_words_list import word_idx, words

def initialise():
  r = word_idx

  curr_words_idx = 1

  # nouns, adjectives, verbs classified into 5 categories of rhyme
  h, w, d = 3, 5, 7
  r_s = [[[None for x in range(d+1)] for x in range(w+1)] for y in range(h+1)] 
  for i in range(1, 3+1):
    for j in range(1, 5+1):
      for k in range(1, r[i][j]+1):
        r_s[i][j][k] = words[curr_words_idx]
        curr_words_idx += 1
  
  # Non rhyming nouns
  n_s = [None for x in range(10+1)]
  for i in range(1, 10+1):
    n_s[i] = words[curr_words_idx]
    curr_words_idx += 1
  
  # Non rhyming adjectives
  a_s = [None for x in range(10+1)]
  for i in range(1, 10+1):
    a_s[i] = words[curr_words_idx]
    curr_words_idx += 1

  return r_s, n_s, a_s

def prompt():
  name = 'Gary'
  print("Enter a name: " + name)
  return name

def describe():
  description = """
USING THIS PROGRAM YOU CAN WRITE A
POEM DEDICATED TO A CLOSE FRIEND. THE
AMSTRAD 6128 WILL SELECT WORDS WHICH
RHYME.
ALL YOU HAVE TO DO IS TYPE THE NAME
OF THE PERSON TO WHOM YOU WISH TO
OFFER YOUR ODE.
  """
  print(description)

def dedication(name):
  print(f"ODE TO {name}")

def select_couplet(r_s, n_s, a_s, name):
  s = 5
  r_flag = do_random(s)  # rhyme flag
  c_flag = do_random(s)  # couplet flag
  do_couplet(r_flag, c_flag, r_s, n_s, a_s, name)
  

def do_random(s):
  return random.randint(1, s)

def do_couplet(r_flag, c_flag, r_s, n_s, a_s, name):
  c_flag = 2  # TODO remove
  funcs = {
    1: couplet_1,
    2: couplet_2,
    3: couplet_3,
    4: couplet_4,
    5: couplet_5,
  }
  funcs[c_flag](r_flag, c_flag, r_s, n_s, a_s, name)

def couplet_1(r_flag, c_flag, r_s, n_s, a_s, name):
  # print('Doing couplet 1')
  n = do_random(10)
  adjective = a_s[n]

  s = word_idx[1][r_flag]
  n = do_random(s)
  noun = r_s[1][r_flag][n]

  phrase = f'I LOVE TO WATCH YOUR {adjective} {noun},'
  print(phrase)

  s = word_idx[3][r_flag]
  n = do_random(s)
  word = r_s[3][r_flag][n]

  phrase = f'DESPITE THE FACT YOU SEEM TO {word}.'
  print(phrase)

def couplet_2(r_flag, c_flag, r_s, n_s, a_s, name):
  print('Doing couplet 2')

  n = do_random(10)
  adjective = a_s[n]

  n = do_random(10)
  noun = n_s[n]

  s = word_idx[1][r_flag]
  n = do_random(s)
  word = r_s[1][r_flag][n]

  phrase = f'THE {adjective} {noun} REMINDS ME OF YOUR {word},'
  print(phrase)

  n = do_random(5)
  rn = n
  s = word_idx[1][rn]
  n = do_random(s)
  noun = r_s[1][rn][n]

  s = word_idx[2][r_flag]
  n = do_random(s)
  adjective = r_s[2][r_flag][n]

  phrase = f'EVEN THOUGH YOUR {noun} IS RATHER {adjective}.'
  print(phrase)

def couplet_3(r_flag, c_flag, r_s, n_s, a_s, name):
  print('Doing couplet 3')

def couplet_4(r_flag, c_flag, r_s, n_s, a_s, name):
  print('Doing couplet 4')

def couplet_5(r_flag, c_flag, r_s, n_s, a_s, name):
  print('Doing couplet 5')

def control():
    r_s, n_s, a_s = initialise()
    describe()
    name = prompt()
    dedication(name=name)
    for i in range(1):
      select_couplet(r_s, n_s, a_s, name)



if __name__ == "__main__":
    control()
