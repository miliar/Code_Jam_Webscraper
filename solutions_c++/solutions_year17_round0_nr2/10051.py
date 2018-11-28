#include <iostream>
#include <string>

unsigned long long last_tidy_number (const unsigned long long max);
bool is_tidy_number (const unsigned long long number);

int main ()
{
  int testCases = 0;
  std::cin >> testCases;
  for (int testCase = 1; testCase <= testCases; ++testCase)
  {
    unsigned long long max = 0;
    std::cin >> max;
    unsigned long long lastTidyNumber = last_tidy_number(max);
    std::cout << "Case #" << testCase << ": " << lastTidyNumber << std::endl;
  }
  return 0;
}

unsigned long long last_tidy_number(const unsigned long long max)
{
  unsigned long long lastTidyNumber = 0;
  unsigned long long number = max;
  while (!lastTidyNumber)
  {
    if (is_tidy_number(number))
    {
      lastTidyNumber = number;
    }
    --number;
  }
  return lastTidyNumber;
}

bool is_tidy_number (const unsigned long long number)
{
  std::string numberString = std::to_string(number);
  unsigned int length = numberString.length();
  for (unsigned int i = 1; i < length; ++i)
  {
    if (numberString[i - 1] > numberString[i])
    {
      return false;
    }
  }
  return true;
}
