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
  uint64_t k;
  uint64_t n;
  void read(ifstream & input)
  {
    input >> n >> k;
  }
};

struct output_data
{
  uint64_t mn;
  uint64_t mx;
  void write(ofstream & output)
  {
    output << mx << ' ' << mn;
  }
};

std::pair<uint64_t, uint64_t> split(uint64_t n)
{
  --n;
  uint64_t mn = n / 2;
  uint64_t mx = n - mn;
  return {mn, mx};
}

output_data calc(input_data data)
{
  std::map<uint64_t, uint64_t, std::greater<uint64_t>> mp;
  auto n = data.n;
  auto k = data.k;
  mp[n] = 1;
  while (k)
  {
    auto great_it = mp.begin();
    const auto cur_n = great_it->first;
    const auto cur_cnt = great_it->second;
    auto split_values = split(cur_n);
    if (cur_cnt >= k)
    {
      return {split_values.first, split_values.second};
    }
    else
    {
      k -= cur_cnt;
      mp[split_values.first] += cur_cnt;
      mp[split_values.second] += cur_cnt;
      mp.erase(great_it);
    }
  }
}

const bool multithread = false;

int main(int argc, char **argv) {
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