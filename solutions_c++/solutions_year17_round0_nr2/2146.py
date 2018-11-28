#include <iostream>
#include <fstream>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>

bool is_tidy(long long number) 
  {
  int last = 10;
  while (number > 0) 
    {
    int cur = number % 10;
    if (cur > last)
      return false;
    last = cur;
    number /= 10;
    }
  return true;
  }

long long prev_tidy(long long number) 
  {
  for (long long i = 0; i < number; ++i)
    if (is_tidy(number - i))
      return number - i;
  return -1;
  }

long long prev_tidy_fast(long long number)
  {
  while (!is_tidy(number))
    {
    std::vector<int> digits;
    while (number > 0)
      {
      digits.push_back(number % 10);
      number /= 10;
      }

    bool need_reduce = true;
    for (int i = 0; i < digits.size(); ++i)
      if ((need_reduce && digits[i] < 9) || digits[i] == -1)
        {
        digits[i] = 9;
        --digits[i + 1];
        need_reduce = false;
        }

    while (digits.back() == 0)
      digits.pop_back();
    long long factor = 1;
    for (int digit : digits)
      {
      number += digit * factor;
      factor *= 10;
      }

    }
  return number;
  }

int main() 
  {
  std::wstring test_name = L"0B_TidyNumbers";

  std::istream& in = std::ifstream(test_name + L"_input.txt"); 
  std::ostream& out = std::ofstream(test_name + L"_output.txt");
  //std::istream& in = std::cin; 
  //std::ostream& out = std::cout;

  int tests_number;
  in >> tests_number;
  for (int test_i = 1; test_i <= tests_number; ++test_i)
    {
    long long n;
    in >> n;

    long long ans = prev_tidy_fast(n);

    out << "Case #" << test_i << ": ";
    out << ans;
    out << std::endl;
    }

  return 0;
  }