#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <sstream>

int is_flippable(std::string str, int k) {
  int count = 0;
  for (int i = 0; i < str.size(); i++) {
    if (str[i] == '-' && i + k <= str.size()) {
      for (int j = i; j < i + k; j++) {
        str[j] = (str.at(j) == '-') ? '+' : '-';
      }
      count++;
    }
  }
  
  for (int i = 0; i < str.size(); i++) {
    if (str[i] == '-')
      return -1;
  }

  return count;
}

int main(int argc, char** argv) {
  if (argc < 2) {
    std::cout << "Please give me the name of tidy num file!" << std::endl;
    return 1;
  }
  std::ifstream inputFile;

  // open input file
  inputFile.open(argv[1]);
  if (inputFile.fail())
  {
    // Report error and return if file failed to open
    std::cout << "Could not open file" << std::endl;
    return 1;
  }
  std::string fileLine;
  int numTries;
  getline(inputFile, fileLine);

  int count = 1;
  while (getline(inputFile, fileLine) ) {
    int k;
    std::stringstream ss2(fileLine);
    std::string str;
    getline(ss2, str, ' ');
    ss2 >> k;

    int success = is_flippable(str, k);

    if (success >= 0)
      std::cout << "Case #" << count << ": " << success << std::endl;
    else
      std::cout << "Case #" << count << ": " << "IMPOSSIBLE" << std::endl;
    count++;
  }

  return 0;
}
