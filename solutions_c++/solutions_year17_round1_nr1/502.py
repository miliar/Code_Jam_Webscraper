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
  vector<string> grid;
  void read(ifstream & input)
  {
    int r;
    int c;
    input >> r >> c;
    grid.resize(r);
    for (auto & g : grid)
    {
      input >> g;
    }
  }
};

struct output_data
{
  vector<string> grid;
  void write(ofstream & output)
  {
    output << '\n';
    bool printed = false;
    for (auto & g : grid)
    {
      if (printed)
        output << '\n';
      printed = true;
      output << g;
    }
  }
};

output_data calc(input_data data)
{
  output_data res = {data.grid};
  auto & v = res.grid;
  string last = "";
  for (int i = 0; i < v.size(); ++i)
  {
    char c = 0;
    auto & row = v[i];
    for (int j = 0; j < row.size(); ++j)
    {
      if (row[j] != '?')
      {
        c = row[j];
        break;
      }
    }
    if (c==0 && last == "")
      continue;
    if (c==0)
    {
      row = last;
      continue;
    }
    for (int j = 0; j < row.size(); ++j)
    {
      if (row[j] == '?')
        row[j] = c;
      else
        c = row[j];
    }
    last = row;
  }
  last = "";
  for (int i = v.size() - 1; i >= 0; --i)
  {
    char c = 0;
    auto & row = v[i];
    for (int j = row.size() - 1; j  >= 0; --j)
    {
      if (row[j] != '?')
      {
        c = row[j];
        break;
      }
    }
    if (c==0 && last == "")
      continue;
    if (c==0)
    {
      row = last;
      continue;
    }
    for (int j = row.size() - 1; j  >= 0; --j)
    {
      if (row[j] == '?')
        row[j] = c;
      else
        c = row[j];
    }
    last = row;
  }
  return res;
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