#include <iostream>
#include <fstream>

#include <algorithm>
#include <vector>
#include <queue>
#include <string>

int main() 
  {
  std::wstring test_name = L"0A_OversizedPancakeFlipper";

  std::istream& in = std::ifstream(test_name + L"_input.txt"); 
  std::ostream& out = std::ofstream(test_name + L"_output.txt");
  //std::istream& in = std::cin; 
  //std::ostream& out = std::cout;

  int tests_number;
  in >> tests_number;
  for (int test_i = 1; test_i <= tests_number; ++test_i)
    {
    std::string cakes;
    long k;
    in >> cakes >> k;

    int flips_number = 0;
    int cakes_size = int(cakes.size());
    bool possible = true;
    std::queue<int> flips;
    for (int i = 0; i < cakes_size; ++i)
      {
      if (!flips.empty() && flips.front() == i - k)
        flips.pop();
      int current = (int(cakes[i] == '-') + flips.size()) % 2;
      if (current == 1)
        {
        if (i > cakes_size - k)
          possible = false;
        else
          {
          ++flips_number;
          flips.push(i);
          }
        }
      }

    out << "Case #" << test_i << ": ";
    if (possible)
      out << flips_number;
    else
      out << "IMPOSSIBLE";
    out << std::endl;
    }

  return 0;
  }