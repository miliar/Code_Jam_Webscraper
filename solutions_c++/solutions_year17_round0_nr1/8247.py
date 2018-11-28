#include <algorithm>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>

#define kHappy '+'
#define kBlank '-'

int nFlip(char* cakes, char* const end, const size_t width, char* const pos) {
  char* firstBlank = std::find(pos, end, kBlank);
  // nothing to do if no blank pancake found
  if (firstBlank == end) return 0;
  // can't flip anymore
  if (end - firstBlank < width) return -1;
  // flip
  for (size_t j = 0; j < width; ++j) {
    if (firstBlank[j] == kHappy) {
      firstBlank[j] = kBlank;
    } else {
      firstBlank[j] = kHappy;
    }
  }
  char* nextBlank = std::find(pos, end, kBlank);
  int subFlip = nFlip(cakes, end, width, nextBlank);
  if (subFlip < 0) {
    return -1;
  } else {
    return subFlip + 1;
  }
  return 0;
}

int main(int argc, char** argv) {
  if (argc <= 2) return -1;

  std::ifstream ifs(argv[1]);
  std::ofstream ofs(argv[2]);
  int nCase = 0;
  ifs >> nCase;
  std::cout << "#Cases: " << nCase << std::endl;
  char cakes[1000];
  for (size_t i = 0; i < nCase; ++i) {
    std::string line;
    int width;
    ifs >> line >> width;

    strcpy(cakes, line.c_str());
    int result = nFlip(cakes, cakes + line.size(), width, cakes);
    std::cout << "Case #" << i + 1 << ": ";
    ofs << "Case #" << i + 1 << ": ";
    if (result >= 0) {
      std::cout << result;
      ofs << result;
    } else {
      std::cout << "IMPOSSIBLE";
      ofs << "IMPOSSIBLE";
    }
    std::cout << std::endl;
    ofs << std::endl;
  }
}
