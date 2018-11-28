#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

void reset(std::vector<char> &num, const int start)
{
  for(int i = start; i < num.size(); ++i)
  {
    num.at(i) = '9';
  }
}

bool is_tidy(const std::vector<char> &num)
{
  for(int i = 1; i < num.size(); ++i)
  {
    if(num.at(i - 1) > num.at(i))
    {
      return false;
    }
  }
  return true;
}

std::vector<char> find(const std::vector<char> &num)
{
  std::vector<char> t(num.size(), '9');
  for(int s = 0; s < num.size(); ++s)
  {
  }
  return t;
}

int main()
{
  std::ifstream in;
  std::ofstream out;
  in.open("small.in");
  out.open("output.out");

  int num_case;
  in >> num_case;

  std::string line;
  std::getline(in, line);

  for(int iter = 0; iter < num_case; ++iter)
  {
    out << "Case #" << iter + 1 << ": ";

    std::vector<char> elem;
    std::getline(in, line);
    elem.reserve(line.size());
    for(int i = 0; i < line.size(); ++i)
    {
      if(line[i] >= '0' && line[i] <= '9')
      {
        elem.push_back(line[i]);
      }
    }

    for(int iter = 1; iter < elem.size(); ++iter)
    {
      for(int i = 1; i < elem.size(); ++i)
      {
        if(elem.at(i - 1) > elem.at(i))
        {
          while(elem.at(i - 1) <= '0' && i >= 1)
          {
            --i;
          }
          --elem.at(i - 1);

          for(int j = i; j < elem.size(); ++j)
          {
            elem.at(j) = '9';
          }
          break;
        }
      }
      if(is_tidy(elem))
      {
        break;
      }
    }

    int i = 0;
    while(elem.at(i) <= '0')
    {
      ++i;
    }
    for(; i < elem.size(); ++i)
    {
      out << elem.at(i);
    }
    out << std::endl;
  }

  in.close();
  out.close();
  return 0;
}
