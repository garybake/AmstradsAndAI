"""
ODE - PAT HALL, 2/86
"""
from ode_words_list import word_idx, words

def initialise():
  r = word_idx

  h, w, d = 3, 5, 7
  r_s = [[[None for x in range(d)] for x in range(w)] for y in range(h)] 

  curr_words_idx = 0

  for i in range(1, 4):
    for j in range(1, 6):
      for k in range(1, r[i-1][j-1]+1):
        r_s[i-1][j-1][k-1] = words[curr_words_idx]
        curr_words_idx += 1
  
  n_s = [None for x in range(10)]
  for i in range(1, 11):
    n_s[i-1] = words[curr_words_idx]
    curr_words_idx += 1

  a_s = [None for x in range(10)]
  for i in range(1, 11):
    a_s[i-1] = words[curr_words_idx]
    curr_words_idx += 1

  print(r_s)
  print(n_s)
  print(a_s)



def control():
    initialise()
    # describe()
    # prompt()
    # dedication()
    # select_couplet()



if __name__ == "__main__":
    control()
