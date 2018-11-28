
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>


std::vector<int> help_order(std::vector<int> unordered)
{
  int tmp_1;
  if(unordered.empty())
  return std::vector<int> ();
  tmp_1 = unordered.front();
  if(tmp_1 == 0)
  {
    unordered.erase(unordered.begin());
    if(!unordered.empty())
    {
      tmp_1 = unordered.front();
    }else
      return std::vector<int> ();
  }
  if(unordered.size() == 1)
    return unordered;

  std::vector<int> ordered;
  for(std::vector<int>::iterator iter = unordered.begin(); iter != unordered.end() ; ++iter)
  {
    int tmp_2 = *iter;
    if(tmp_2 < tmp_1)
    {
      tmp_1--;
      if(!ordered.empty())
      {
        ordered.pop_back();
        ordered.push_back(tmp_1);
        ordered = help_order(ordered);
      }
      for(std::vector<int>::iterator iter2 = iter; iter2 != unordered.end(); ++iter2)
      {
        ordered.push_back(9);
      }
      return ordered;

    }else
    {
      ordered.push_back(tmp_2);
      tmp_1 = tmp_2;
    }
  }
  return ordered;
}

std::string handle_input(int count, std::string line)
{
  if(count == 0)
    return "";
  std::stringstream result;
  std::vector<int> unordered, ordered;
  unordered.reserve(line.size());
  std::transform(std::begin(line), std::end(line), std::back_inserter(unordered), [](char c) {return c - '0';});
  ordered = help_order(unordered);
  if(!ordered.empty())
    std::copy(ordered.begin(), ordered.end(), std::ostream_iterator<int>(result, ""));

  return "Case #" + std::to_string(count) +": " + result.str() + "\n";

}

int main(int argc, char const *argv[]) {

  std::string output{};
  int count = 0;
  std::fstream file("B-large.in", std::fstream::in);
  std::cout << "start!"<< std::endl;
  for( std::string line; getline( file, line ); )
  {
    output +=handle_input(count, line);
    count ++;
  }
  file.close();
  std::cout << output;
  std::ofstream output_file;
  output_file.open("output_file.txt", std::fstream::out);
  output_file << output << std::flush;
  output_file.close();

  return 0;
}
