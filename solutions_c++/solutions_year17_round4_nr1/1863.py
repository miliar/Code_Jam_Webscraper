#include <cstdint>
#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

struct input_data
{
  int n;
  int p;
  vector<int> g;
  void read(ifstream & input)
  {
    input >> n >> p;
    g.resize(n);
    for (auto & a : g)
      input >> a;
  }
};

struct output_data
{
  int y;
  void write(ofstream & output)
  {
    output << y;
  }
};

output_data calc(input_data data)
{
  auto n = data.n;
  auto p = data.p;
  auto g = data.g;
  map<int, vector<int>> mp;
  for (auto & a : g)
    mp[a % p].push_back(a);
  int result = n;
  int rest = 0;
  while (true)
  {
    bool stop = true;
    for (int i = 0; i < p; ++i)
      stop &= mp[i].empty();
    if (stop)
      break;
    if (rest)
      result--;
    if (!mp[rest].empty())
    {
      mp[rest].pop_back();
      rest = 0;
      continue;
    }
    for (int i = 0; i < p; ++i)
    {
      if (!mp[i].empty())
      {
        auto last = mp[i].back();
        auto e = min(rest, last);
        rest -= e;
        last -= e;
        if (last)
        {
          rest = p - (last % p);
        }
        mp[i].pop_back();
        break;
      }
    }
    
  }
  return {result};
}

const bool multithread = false;

int main(int /*argc*/, char **argv) {
  ios::sync_with_stdio(false);
  string input_file = argv[1];
  string output_file = argv[2];
  ifstream input(input_file);
  ofstream output(output_file);
  int total;
  input >> total;

  list<future<output_data>> tasks;
  for (int current = 0; current < total; ++current)
  {
    input_data data;
    data.read(input);
    if (multithread)
    {
      tasks.push_back(
        std::async(
          [data = std::move(data)]()
          {
            return calc(std::move(data));
          }));
    }
    else
    {
      auto result = calc(std::move(data));
      tasks.push_back(
        std::async(
          [result = std::move(result)]()
          {
            return result;
          }));
    }
  }
  int index = 1;
  for (auto & task : tasks)
  {
    std::cout<< index << "\n";
    output << "Case #" << index++ << ": ";  
    task.get().write(output);
    output << "\n";
  }
  return 0;
}