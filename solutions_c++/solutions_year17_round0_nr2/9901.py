#include <string>
#include <algorithm>
#include <iostream>

static std::string
getTidyNumber(std::string number)
{
  for (size_t i = 0, size = number.size(); size > 1 && i < size - 1; ++i)
  {
    if (number[i] <= number[i + 1])
      continue;

    size_t index = (number[i] == number[0]) ? 0 : i;

    number[index] = number[i] - 1;
    std::fill(number.begin() + index + 1, number.end(), '9');

    if (number[index] == '0')
      number.erase(0, 1);

    break;
  }

  return number;
}

int
main(int argc, char** argv)
{
  std::string line;
  std::getline(std::cin, line);

  size_t t = std::stoi(line);

  for (size_t i = 1; i <= t; ++i)
  {
    std::getline(std::cin, line);
    std::cout << "Case #" << i << ": " << getTidyNumber(line) << std::endl;
  }

  return 0;
}
