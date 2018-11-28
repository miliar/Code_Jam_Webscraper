#include <iostream>
#include <string>
#include <vector>
#include <fstream>

static bool is_tidy(unsigned long long number)
{
  std::vector<unsigned long long> tmp;
  while (number != 0)
  {
    tmp.push_back(number % 10);
    number = number / 10;
  }
  for (int i = 1; i < tmp.size(); i++)
  {
    if (tmp[i] > tmp[i - 1])
      return false;
  }
  return true;
}

static unsigned long long last_tidy_number(std::string line)
{
  unsigned long long number = 0;
  number = std::stoull(line);
  while (number != 1)
  {
    if (is_tidy(number))
      return number;
    number--;
  }
  return number;
}

static void read_file(char* argv)
{
  std::ifstream in(argv);
  std::ofstream out("output.out");
  std::string line = "";
  int i = 1;
  std::getline(in, line);
  while (std::getline(in, line))
  {
    unsigned long long last = last_tidy_number(line);
    out << "Case #" << i << ": " << last << std::endl;
    i++;
  }
  in.close();
  out.close();
}

int main(int argc, char* argv[])
{
  if (argc != 2)
    exit(1);
  read_file(argv[1]);
}
