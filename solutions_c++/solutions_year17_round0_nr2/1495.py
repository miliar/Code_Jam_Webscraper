#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

struct input_data
{
  string a;
  void read(ifstream & input)
  {
    input >> a;
  }
};

struct output_data
{
  std::string res;
  void write(ofstream & output)
  {
    if (res[0] == '0')
      res.erase(0, 1);
    output << res;
  }
};

bool test(const string a)
{
  for (int i = 1; i < a.size(); ++i)
    if (a[i] < a[i-1])
      return false;
  return true;
}

output_data calc(input_data data)
{
  output_data res{data.a };
  for (int i = res.res.size() - 1 ; i >= 0 ; --i)
  {
    if (test(res.res))
      return res;
    res.res[i] = '9';
    for (int j = i - 1; j >= 0; --j)
    {
      if(res.res[j] == '0')
      {
        res.res[j] = '9';
      }
      else
      {
        res.res[j] = res.res[j] - 1;
        break;
      }
    }
  }
  return res;
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