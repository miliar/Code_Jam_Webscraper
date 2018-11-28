#include <algorithm>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>

int descendingPos(char* digits, size_t len) {
  if (len <= 1) return -1;
  for (size_t i = 0; i < len - 1; ++i) {
    if (digits[i] > digits[i + 1]) {
      return i;
    }
  }
  return -1;
}

void fixAscend(char* digits, size_t len, int pos) {
  if (pos < 0) return;
  int fillPos = pos + 1;
  int decPos = pos;
  for (auto i = pos; i >= 0; i--) {
    digits[i]--;
    if (i > 0 && digits[i] >= digits[i - 1]) {
      fillPos = i + 1;
      break;
    }
    decPos = i;
  }
  if (decPos == 0) {
    fillPos = 1;
  }
  for (auto i = fillPos; i < len; ++i) {
    digits[i] = '9';
  }
}

int main(int argc, char** argv) {
  if (argc <= 2) return -1;

  std::ifstream ifs(argv[1]);
  std::ofstream ofs(argv[2]);
  int nCase = 0;
  ifs >> nCase;
  std::cout << "#Cases: " << nCase << std::endl;
  char digits[100];
  for (size_t i = 0; i < nCase; ++i) {
    std::string line;
    ifs >> line;

    strcpy(digits, line.c_str());
    std::cout << "Case #" << i + 1 << ": ";
    ofs << "Case #" << i + 1 << ": ";

    // find a descending point
    int desc_pos = descendingPos(digits, line.size());
    fixAscend(digits, line.size(), desc_pos);

    std::string output = (digits[0] == '0') ? std::string(digits + 1) : std::string(digits);
    std::cout << output << std::endl;
    ofs << output << std::endl;
  }
}
