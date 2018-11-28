
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>

std::string flip(std::string to_flip)
{
  std::string result{};
  if(to_flip == "+")
    result += "-";
  else
    result += "+";
  return result;
}

std::string handle_input(int count, std::string line)
{
  if(count == 0)
    return "";
  std::string pancakes = line.substr(0, line.find(" "));
  std::string k_str = line.substr(line.find(" ")+1, line.length());
  int k = std::stoi(k_str);
  int counter = 0;
  if(pancakes.find("-") == std::string::npos)
  {
    return "Case #" + std::to_string(count) + ": 0\n";
  }

  for(int i = 0; i <= pancakes.length()-k ; ++i)
  {
    if(pancakes.at(i) == '-')
    {
      std::string tmp_str{};
      for(int j = 0; j<k;++j)
      {
        std::string tmp(1, pancakes.at(i+j));
        pancakes.replace(i+j, 1, flip(tmp));
      }
      counter++;
    }
    std::cout << std::to_string(i) << " " << pancakes.length()-k << std::endl;
  }
  if(pancakes.find('-') == std::string::npos)
   return "Case #" + std::to_string(count) + ": " + std::to_string(counter) + "\n";
  else
    return "Case #" + std::to_string(count) + ": IMPOSSIBLE\n";


}


int main(int argc, char const *argv[]) {

  std::string output{};
  int count = 0;
  std::fstream file("A-large.in", std::fstream::in);
  for( std::string line; getline( file, line ); )
  {
    output +=handle_input(count, line);
    count ++;
  }
  file.close();
  std::ofstream output_file;
  output_file.open("output_file.txt", std::fstream::out);
  output_file << output << std::flush;
  output_file.close();

  return 0;
}
