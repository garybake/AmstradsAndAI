"""
ODE - PAT HALL, 2/86
"""
import random

from ode_words_list import word_idx, words

def initialise():
  r = word_idx

  curr_words_idx = 0

  # nouns, adjectives, verbs classified into 5 categories of rhyme
  h, w, d = 3, 5, 7
  r_s = [[[None for x in range(d)] for x in range(w)] for y in range(h)] 
  for i in range(1, 4):
    for j in range(1, 6):
      for k in range(1, r[i-1][j-1]+1):
        r_s[i-1][j-1][k-1] = words[curr_words_idx]
        curr_words_idx += 1
  
  # Non rhyming nouns
  n_s = [None for x in range(10)]
  for i in range(1, 11):
    n_s[i-1] = words[curr_words_idx]
    curr_words_idx += 1

  # Non rhyming adjectives
  a_s = [None for x in range(10)]
  for i in range(1, 11):
    a_s[i-1] = words[curr_words_idx]
    curr_words_idx += 1

  return r_s, n_s, a_s

  # print(r_s)
  # print(n_s)
  # print(a_s)

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
  funcs = {
    1: couplet_1,
    2: couplet_1,
    3: couplet_1,
    4: couplet_1,
    5: couplet_1,
  }
  funcs[c_flag](r_flag, c_flag, r_s, n_s, a_s, name)

def couplet_1(r_flag, c_flag, r_s, n_s, a_s, name):
  print('Doing couplet 1')
  # out = "I LOVE TO WATCH YOUR "
  # print(out)
  # n = 1
  n = do_random(10)
  adjective = a_s[n-1]
  # print(adjective)
  # print(r_s)

  s = word_idx[0][r_flag-1]
  n = do_random(s)
  # print(s, r_flag)
  # print(r_s[0, r_flag, ])
  noun = r_s[0][r_flag][n-1]

  phrase = f'I LOVE TO WATCH YOUR {adjective} {noun}'
  print(phrase)


def couplet_2(r_s, r_f, n_s, a_s, name):
  print('Doing couplet 2')

def couplet_3(r_s, r_f, n_s, a_s, name):
  print('Doing couplet 3')

def couplet_4(r_s, r_f, n_s, a_s, name):
  print('Doing couplet 4')

def couplet_5(r_s, r_f, n_s, a_s, name):
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
