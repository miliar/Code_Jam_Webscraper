#include <iostream>
#include <string>
#include <vector>
#include <fstream>

static int count_flips(std::string line)
{
  int i = 0;
  std::string pancakes = line.substr(0, line.find(" "));
  int size = stoi(line.substr(line.find(" "), line.find("\n")));
  int flips = 0;
  while (i != pancakes.size())
  {
    while (i != pancakes.size() && pancakes[i] == '+')
      i++;
    if (i + size > pancakes.size())
      break;
    flips++;
    for (int p = 0; p < size && i + p != pancakes.size(); p++)
    {
      if (pancakes[p + i] == '-')
	pancakes[p + i] = '+';
      else
	pancakes[p + i] = '-';
    }
  }
  for (int p = 0; p < pancakes.size(); p++)
  {
    if (pancakes[p] == '-')
      return -1;
  }
  return flips;
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
    int count = count_flips(line);
    out << "Case #" << i << ": ";
    if (count >= 0)
      out << count;
    else
      out << "IMPOSSIBLE";
    out << std::endl;
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
