#include <iostream>
#include <string>

const char HAPPY_SIDE = '+';
const char BLANK_SIDE = '-';

void flip (std::string & pancakes, const int flipPosition, const int flipperSize);
int blanks (const std::string & pancakes, const int flipPosition, const int flipperSize);
bool allHappy (const std::string & pancakes);
bool solve (std::string & pancakes, const int pos, const int flipperSize, int & flips);

int main ()
{
  int testCases = 0;
  std::cin >> testCases;
  std::cin.ignore();
  for (int testCase = 1; testCase <= testCases; ++testCase)
  {
    std::string pancakes;
    std::getline(std::cin, pancakes, ' ');
    int flipperSize = 0;
    std::cin >> flipperSize;
    std::cin.ignore();
    std::cout << "Case #" << testCase << ": ";
    int flips = 0;
    if (solve(pancakes, 0, flipperSize, flips))
    {
      std::cout << flips << std::endl;
    }
    else
    {
      std::cout << "IMPOSSIBLE" << std::endl;
    }
  }
  return 0;
}

void flip (std::string & pancakes, const int flipPosition, const int flipperSize)
{
  for (int i = 0; i < flipperSize; ++i)
  {
    if (pancakes[i + flipPosition] == HAPPY_SIDE)
    {
      pancakes[i + flipPosition] = BLANK_SIDE;
    }
    else if (pancakes[i + flipPosition] == BLANK_SIDE)
    {
      pancakes[i + flipPosition] = HAPPY_SIDE;
    }
  }
  return;
}

int blanks (const std::string & pancakes, const int flipPosition, const int flipperSize)
{
  int blanks = 0;
  for (int i = 0; i < flipperSize; ++i)
  {
    if (pancakes[i + flipPosition] == BLANK_SIDE)
    {
      ++blanks;
    }
  }
  return blanks;
}

bool allHappy (const std::string & pancakes)
{
  for (int i = 0; i < pancakes.length(); ++i)
  {
    if (pancakes[i] == BLANK_SIDE)
    {
      return false;
    }
  }
  return true;
}

bool solve (std::string & pancakes, const int pos, const int flipperSize, int & flips)
{
  int length = pancakes.length();
  if (allHappy(pancakes))
  {
    return true;
  }
  for (int i = 0; i < flipperSize && length - i - flipperSize >= 0; ++i)
  {
    if (pancakes[length - i - 1] == BLANK_SIDE)
    {
      flip(pancakes, length - i - flipperSize, flipperSize);
      ++flips;
    }
  }
  if (allHappy(pancakes))
  {
    return true;
  }
  for (int i = pos; i < length - flipperSize + 1; ++i)
  {
    //if (blanks(pancakes, i, flipperSize) != 0)
    if (pancakes[i] == BLANK_SIDE)
    {
      flip(pancakes, i, flipperSize);
      ++flips;
      if (allHappy(pancakes))
      {
        return true;
      }
      else
      {
        if (solve(pancakes, pos + 1, flipperSize, flips))
        {
          return true;
        }
        else
        {
          flip(pancakes, i, flipperSize);
          --flips;
        }
      }
    }
  }
  return false;
}
