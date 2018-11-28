INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"
BAD_MAGICIAN_TEXT =  "Bad magician!"
BAD_CUSTOMER_TEXT = "Volunteer cheated!"


def main():
  with open(INPUT_FILENAME) as input:
    with open(OUTPUT_FILENAME, 'w') as output:
      num_cases = int(input.readline())
      # Lines are ones based indexed
      for case_num in range(1, num_cases + 1):

        print("Starting case #{}".format(case_num))

        first_question_answer = int(input.readline())
        print("First question answer: {}".format(first_question_answer))

        first_answer_line = None
        # Problem specifies 4 lines per case. Read all 4 lines, but keep the one
        # we want.
        for line_num in range(1, 4 + 1):
          number_set = input.readline()
          if line_num == first_question_answer:
            first_answer_line = number_set
        assert(first_answer_line is not None)
        first_answer_numbers = map(int, first_answer_line.split(' '))
        print("First answer numbers: {}".format(first_answer_numbers))

        second_question_answer = int(input.readline())
        print("Second question answer: {}".format(second_question_answer))

        # Read the next 4 lines, keeping the one we want
        second_answer_line = None
        for line_num in range(1, 4 + 1):
          number_set = input.readline()
          if line_num == second_question_answer:
            second_answer_line = number_set
        assert(second_answer_line is not None)
        second_answer_numbers = map(int, second_answer_line.split(' '))
        print("Second answer numbers: {}".format(second_answer_numbers))

        # If a number is found in both lists, remember it - that might be our
        # number! We also count how many we find, so we can know if we find
        # more than one.
        number_that_matches = None
        num_matches = 0
        for first_match in first_answer_numbers:
          for second_match in second_answer_numbers:
            if first_match == second_match:
              number_that_matches = first_match
              num_matches += 1
        print("Num matches: {}".format(num_matches))
        print("Matching number: {}".format(number_that_matches))

        if num_matches == 0:
          result_string = BAD_CUSTOMER_TEXT
        elif num_matches > 1:
          result_string = BAD_MAGICIAN_TEXT
        elif num_matches == 1:
          result_string = number_that_matches
        output.write("Case #{}: {}\n".format(case_num, result_string))

          
if __name__ == "__main__":
  main()
