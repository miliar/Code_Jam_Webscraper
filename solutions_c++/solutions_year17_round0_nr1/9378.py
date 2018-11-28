#include <iostream>
#include <vector>

void flip(std::string& pancakes, int position, int flipperSize)
{
  for (int i = position; i < position + flipperSize; ++i)
  {
    if (pancakes[i] == '-')
    {
      pancakes[i] = '+';
    }
    else
    {
      pancakes[i] = '-';
    }
  }
}

int main() {
  int cases = 0;
  std::cin >> cases;
  for (int i = 0; i < cases; ++i)
  {
    bool possible = true;
    std::string readIn;
    std::cin >> readIn;
    int flipperNumber;
    std::cin >> flipperNumber;
    int flips = 0;
    for (auto i = 0; i < readIn.size() - flipperNumber + 1; ++i)
    {
      if (readIn[i] == '-')
      {
        flip(readIn, i, flipperNumber);
        ++flips;
      }
    }
    for (auto&& c : readIn)
    {
      if (c == '-')
      {
        std::cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << std::endl;
        possible = false;
        break;
      }
    }
    if (possible)
      std::cout << "Case #" << i + 1 << ": " << flips << std::endl;
  }
}