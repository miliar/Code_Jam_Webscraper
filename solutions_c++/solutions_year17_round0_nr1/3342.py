#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

void flip(std::vector<char> &pcs, const int first, const int size)
{
  if(first + size <= pcs.size())
  {
    for(int i = 0; i < size; ++i)
    {
      const int id = i + first;
      if(pcs[id] == '+')
      {
        pcs[id] = '-';
      }
      else
      {
        pcs[id] = '+';
      }
    }
  }
}

bool is_happy(const std::vector<char> &cakes)
{
  for(int i = 0; i < cakes.size(); ++i)
  {
    if(cakes[i] == '-')
    {
      return false;
    }
  }
  return true;
}

void parse(const std::string &line, std::vector<char> &cakes, int &k)
{
  int pos = line.find(" ");
  cakes.resize(pos);

  for(int i = 0; i < pos; ++i)
  {
    cakes.at(i) = line[i];
  }

  k = std::stoi(line.substr(pos));
}

int main()
{
  std::ifstream in;
  std::ofstream out;
  in.open("small.in");
  out.open("output.out");

  int num_case;
  in >> num_case;

  std::string tmp;
  std::getline(in, tmp);

  for(int iter = 0; iter < num_case; ++iter)
  {
    out << "Case #" << iter + 1 << ": ";

    std::string line;
    std::vector<char> cakes; 
    int k;
    int r = 0;

    std::getline(in, line);
    parse(line, cakes, k);

    for(int i = 0; i <= cakes.size() - k; ++i)
    {
      if(cakes.at(i) == '-')
      {
        flip(cakes, i, k);
        ++r;
      }
    }
    if(is_happy(cakes))
    {
      out << r << std::endl;
    }
    else
    {
      out << "IMPOSSIBLE" << std::endl;
    }
  }

  in.close();
  out.close();
  return 0;
}
