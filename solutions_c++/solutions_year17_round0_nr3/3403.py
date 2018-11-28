#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>

void insert(std::list<int> &count, std::list<unsigned long long> &value, 
    const unsigned long long val)
{
  std::list<unsigned long long>::iterator it_v = value.begin();
  std::list<int>::iterator it_c = count.begin();

  if(*it_v < val)
  {
    value.insert(it_v, val);
    count.insert(it_c, 1);
  }
  else
  {
    while(true)
    {
      if(it_v == value.end() || *(it_v) < val)
      {
        value.insert(it_v, val);
        count.insert(it_c, 1);
        break;
      }
      else if(*it_v == val)
      {
        ++(*it_c);
        break;
      }

      ++it_c;
      ++it_v;
    }
  }
}

void split(const unsigned long long val, unsigned long long &v0, unsigned long long &v1)
{
  unsigned long long h = val >> 1;
  v1 = h;
  if(val % 2 == 0)
  {
    v0 = h - 1;
  }
  else
  {
    v0 = h;
  }
}

void erase(std::list<int> &count, std::list<unsigned long long> &value)
{
  if(count.empty())
  {
    return;
  }

  unsigned long long val = value.front();
  unsigned long long v0, v1;
  split(val, v0, v1);
  //  std::cout << "erase " << val << " " << v0 << " " << v1 << std::endl;
  if(count.front() <= 1)
  {
    count.pop_front();
    value.pop_front();
  }
  else
  {
    --count.front();
  }

  insert(count, value, v0);
  insert(count, value, v1);
}

int main()
{
  std::ifstream in;
  std::ofstream out;
  in.open("small.in");
  out.open("output.out");

  int num_case;
  in >> num_case;

  for(int iter = 0; iter < num_case; ++iter)
  {
    out << "Case #" << iter + 1 << ": ";
    unsigned long long m, n;

    in >> n >> m;

    std::list<int> count;
    std::list<unsigned long long> value;

    count.push_back(1);
    value.push_back(n);
    
    unsigned long long v0, v1;
    for(unsigned long long id = 0; id < m; ++id)
    {
      unsigned long long val = value.front();
      split(val, v0, v1);
      //    for(unsigned long long v : value) std::cout << v << " "; std::cout << std::endl;
      //    for(int v : count) std::cout << v << " "; std::cout << std::endl;
      //    std::cout << "do\n";
      erase(count, value);
    }
    out << v1 << " " << v0 << std::endl;
  }

  in.close();
  out.close();
  return 0;
}
