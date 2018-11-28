#include <iostream>
#include <vector>

const unsigned int NUM_DIGITS = 10;

unsigned long my_ipow(unsigned int base, unsigned int my_exp)
{
  unsigned long ret = 1U;
  for(unsigned int idx = 0; idx < my_exp; ++idx)
    ret *= base;
  return ret;
}

unsigned long get_offset(unsigned long num, unsigned short digit, unsigned int power_idx)
{
  unsigned long offset = 0;
  while(num > 0)
  {
    unsigned short curr_digit = num % NUM_DIGITS;
    num /= NUM_DIGITS;
    if (curr_digit == digit)
    {
      offset += my_ipow(NUM_DIGITS, power_idx) * digit;
      ++power_idx;
    }
  }
  return offset;
}

bool is_tidy(unsigned long num, unsigned long& offset)
{
  unsigned int power_idx = 0;
  unsigned short last_digit = num % NUM_DIGITS;
  num /= NUM_DIGITS;
  while(num > 0)
  {
    offset += my_ipow(NUM_DIGITS, power_idx) * last_digit;
    ++power_idx;

    unsigned short curr_digit = num % NUM_DIGITS;
    num /= NUM_DIGITS;
    if (curr_digit > last_digit)
    {
      offset += get_offset(num, curr_digit, power_idx);
      return false;
    }

    last_digit = curr_digit;
  }
  return true;
}

unsigned long find_last_tidy(unsigned long start_num)
{
  unsigned long idx = 0;
  for(unsigned long curr_num = start_num; curr_num > 0; ++idx)
  {
    unsigned long offset = 0;
    if (is_tidy(curr_num, offset))
      return curr_num;
    curr_num -= (offset > 0) ? offset : 1;
  }
  return 0U;
}

int main()
{

  unsigned int num_tests = 0;
  std::cin >> num_tests;
  for(unsigned idx = 1; idx <= num_tests; ++idx)
  {
    unsigned long start_num = 0;
    std::cin >> start_num;
    std::cout << "Case #" << idx << ": ";
    std::cout << find_last_tidy(start_num) << std::endl;
  }
}
