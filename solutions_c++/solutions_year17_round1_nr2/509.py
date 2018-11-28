#include <algorithm>
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
  vector<int64_t> ws;
  vector<vector<int64_t>> ins;
  void read(ifstream & input)
  {
    int64_t n;
    int64_t p;
    input >> n >> p;
    ws.resize(n);
    for (auto & w : ws)
      input >> w;
    ins.resize(n);
    for (auto & in : ins)
    {
      in.resize(p);
      for (auto & ingr : in)
        input >> ingr;
      sort(in.begin(), in.end());
    }
  }
};

struct output_data
{
  int64_t res = 0;
  void write(ofstream & output)
  {
    output << res;
  }
};

output_data calc(input_data input)
{
  output_data data;
  auto & res = data.res;
  vector<int> variant;
  for (int64_t cnt = 1; cnt <= 1000 * 1000 * 2; ++cnt)
  {
    variant.clear();
    for (int64_t i = 0; i< input.ws.size(); ++i)
    {
      auto w = input.ws[i];
      auto & ins = input.ins[i];
      int good = -1;
      for (int64_t j = 0; j < ins.size(); ++j)
      {
        if (ins[j] == -1)
          continue;
        if (w * cnt * 9  <= ins[j] * 10 && w * cnt * 11 >= ins[j] * 10)
        {
          good = j;
          break;
        }
      }
      if (good != -1)
        variant.push_back(good);
      else
        break;
    }
    if (variant.size() == input.ws.size())
    {
      for (int64_t i = 0; i< input.ws.size(); ++i)
      {
        auto & ins = input.ins[i];
        ins[variant[i]] = -1;
      }
      ++res;
      cnt--;
    }
  }
  return data;
}

const bool multithread = false;

int main(int /*argc*/, char **argv) {
  ios::sync_with_stdio(false);
  string input_file = argv[1];
  string output_file = argv[2];
  ifstream input(input_file);
  ofstream output(output_file);
  int64_t total;
  input >> total;

  list<future<output_data>> tasks;
  for (int64_t current = 0; current < total; ++current)
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
  int64_t index = 1;
  for (auto & task : tasks)
  {
    std::cout<< index << "\n";
    output << "Case #" << index++ << ": ";  
    task.get().write(output);
    output << "\n";
  }
  return 0;
}