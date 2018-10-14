#!/usr/bin/python
import sys, os, string, pickle

# Translating Googlerese

def print_usage():
  print "Usage: ./problem_a.py <train file> <input file>"
  

def read_test_data(input_filename):
  input_file = open(input_filename, 'r')
  lines =  input_file.readlines()
  input_file.close()

  num_tests = int(lines[0])
  test_cases = []
  append = test_cases.append
  for i in range(num_tests):
    append(lines[i+1].replace('\n', ''))

  return test_cases

def read_training_data(input_filename):
  input_file = open(input_filename, 'r')
  lines =  input_file.readlines()
  input_file.close()

  num_tests = int(lines[0])
  translations = []
  encrypted   = []

  t_append = translations.append
  e_append  = encrypted.append

  for i in range(num_tests):
    t_append(lines[1 + 2*i+1].replace('\n', ''))
    e_append(lines[1 + 2*i].replace('\n', ''))

  return encrypted, translations

def learn_mapping(translations, encrypted):
  mapping = {}
  for i in range(len(translations)):
    translation = translations[i]
    encrypted_msg = encrypted[i]
    if len(translation) <> len(encrypted_msg):
      raise Exception("not the same length!")
    for i in range(len(translation)):
      if encrypted_msg[i] not in mapping:
        mapping[encrypted_msg[i]] = translation[i]
  keys = mapping.keys()
  keys.sort()

  mapping['z']  = 'q'
  mapping['q'] = 'z'
  
  items = mapping.items()
  items.sort()

  return mapping

def translate(filename, mapping):
  string_of_alphabet = string.ascii_lowercase
  test_cases = read_test_data(filename)
  output = ''
  for i in range(len(test_cases)):
    test_case = test_cases[i]
    output += 'Case #' + str(i+1) + ': '
    for char in test_case:
       output += mapping[char]
    output += '\n'

  return output 

def main():
  if len(sys.argv) <> 3:
    print_usage()
    sys.exit(1)

   

  train_filename = sys.argv[1]
  input_filename = sys.argv[2]

  encrypted, translations = read_training_data(train_filename)
  mapping = learn_mapping(translations, encrypted)

  #test_cases = read_test_data(input_filename)
  output = translate(input_filename, mapping)
  print output
     
  # Create a dictionary   
  

if __name__ == "__main__":
  main()
