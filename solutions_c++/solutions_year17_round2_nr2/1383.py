#include <iostream>
#include <fstream>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>

int main() 
  {
  std::wstring test_name = L"1AB_Second";

  std::istream& in = std::ifstream(test_name + L"_input.txt"); 
  std::ostream& out = std::ofstream(test_name + L"_output.txt");
  //std::istream& in = std::cin; 
  //std::ostream& out = std::cout;

  char letters[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };

  int tests_number;
  in >> tests_number;
  for (int test_i = 1; test_i <= tests_number; ++test_i)
    {
    // INPUT
    long n;
    in >> n;
    char unicorn;
    // red, orange (red + yellow), yellow, green (yellow + blue), blue, violet (blue + red)
    // R, O=RY, Y, G=YB, B, V=BR

    std::vector<int> unicorns(6);
    for (long i = 0; i < 6; ++i)
      in >> unicorns[i];

    // ALGO
    std::vector<int> result;
    int prev_unicorn;
    for (long i = 0; i < n; ++i)
      {
      int max_three = 0, index = 8;
      bool is_best_near_first = false;
      for (int j = 0; j < 6; ++j)
        {
        if ((result.empty() || abs(j - prev_unicorn) % 6 > 1) && unicorns[j] > 0)
          {
          const long cur = unicorns[(j + 5) % 6] + unicorns[j] + unicorns[(j + 1) % 6];
          bool is_current_near_first = true;
          if (i > 0)
            is_current_near_first = abs(j - result[0]) % 6 < 2;

          if ((is_current_near_first && !is_best_near_first) ||
              (is_current_near_first == is_best_near_first && cur > max_three))
            {
            is_best_near_first = is_current_near_first;
            max_three = cur;
            index = j;
            }
          }
        }
      if (index == 8)
        break;
      result.push_back(index);
      --unicorns[index];
      prev_unicorn = index;
      }

    if (result.size() > 1 && abs(result[0] - result.back()) % 6 < 2)
      result.pop_back();

    // OUTPUT
    out << "Case #" << test_i << ": ";
    if (result.size() < n)
      out << "IMPOSSIBLE";
    else
      for (long i = 0; i < n; ++i)
        out << letters[result[i]];
    out << std::endl;
    }

  return 0;
  }