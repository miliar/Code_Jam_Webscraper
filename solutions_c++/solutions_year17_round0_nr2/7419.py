#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <sstream>

std::string last_tidy(unsigned long n) {
  std::string str;
  std::ostringstream ss;

  ss << n;
  str = ss.str();

  if (str.size() == 1)
    return str;
  bool greater = false;
  do {
    greater = false;
    for (int i = 0; i < str.size() - 1; i++) {
      if (str[i] > str[i+1]) {
        int j = str[i] - '0';
        j--;
        str[i] = j + '0';
        for (j = i+1; j < str.size(); j++) {
          str[j] = '9';
        }
        greater = true;
      }
    }
  } while (greater);
  return str;

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
    unsigned long n;
    std::stringstream ss2(fileLine);
    ss2 >> n;
    std::string success = last_tidy(n);
    ss2.clear();
    ss2.str(success);
    ss2 >> n;
    printf("Case #%d: %lu\n", count, n);
    count++;
  }

  return 0;
}
