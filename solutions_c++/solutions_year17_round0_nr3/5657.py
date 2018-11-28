#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>

int max, min;
std::vector<int> find_stall(std::vector<int> free_stalls)
{
  auto max_space = max_element(std::begin(free_stalls), std::end(free_stalls));

  int max_space_int = *max_space;
  //std::cout << max_space_int << std::endl;
  if(max_space_int ==1 )
  {
    free_stalls.at(max_space - free_stalls.begin()) = 0;
    max = 0;
    min = 0;
  }
  else if(max_space_int % 2 == 0)
  {
    int new_space_left  = (max_space_int / 2)-1;
    if(new_space_left <0 )
      new_space_left = 0;
    int new_space_right  = max_space_int / 2;
    max = new_space_right;
    min = new_space_left;
    int place = max_space - free_stalls.begin();
    //std::cout << place << " " << free_stalls.size() << std::endl;
    free_stalls.at(place) =new_space_left;
    if(place == free_stalls.size()-1)
      free_stalls.push_back(new_space_right);
    else
      free_stalls.insert(free_stalls.begin() + place+1, new_space_right);

    //free_stalls.push_back(new_space_left);
    //free_stalls.push_back(new_space_right);
  }
  else
  {
    int new_space_left  = max_space_int / 2;
    int new_space_right  = max_space_int / 2;
    int place = max_space - free_stalls.begin();
    max = new_space_right;
    min = new_space_left;
    free_stalls.at(place) =new_space_left;
    if(place == free_stalls.size()-1)
      free_stalls.push_back(new_space_right);
    else
      free_stalls.insert(free_stalls.begin() + place+1, new_space_right);
  }
  return free_stalls;
}

std::string handle_input(int count, std::string line)
{
  if(count == 0)
    return "";
  int stall_int, bobs_int;
  std::string stalls = line.substr(0, line.find(" "));
  std::string bobs = line.substr(line.find(" ")+1, line.length());

  stall_int = std::stoi(stalls);
  bobs_int = std::stoi(bobs);
  std::vector<int> free_stalls;
  free_stalls.push_back(stall_int);
  for(int i = bobs_int ; i>0; --i)
  {
    free_stalls = find_stall(free_stalls);
  }
  std::cout << "max" << max << std::endl;
  std::cout << "min" << min << std::endl;
  //std::cout << stall_int << std::endl;
  //std::cout << bobs_int << std::endl;
  return "Case #" +std::to_string(count) + ": " +  std::to_string(max)+ " " + std::to_string(min) + "\n";
}

int main(int argc, char const *argv[]) {

  std::string output{};
  int count = 0;
  std::fstream file("C-small-1-attempt2.in", std::fstream::in);
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
}
