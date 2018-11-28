#include <iostream>
#include <vector>

void checkNegative(std::vector<unsigned short> &rowV) {
  for (unsigned int i = rowV.size() - 1; i > 0; --i) {
    if (rowV[i] < 0) {
      rowV[i - 1]--;
      rowV[i] = rowV[i + 1];
    }
  }
}

void showVector(const std::vector<unsigned short> &rowV) {
  bool a = false;
  for (const auto &i : rowV) {
    if (i != 0 or a == true) {
      std::cout << i;
      a = true;
    }
  }
}

int main(int argc, char *argv[]) {
  unsigned int T, K;
  std::cin >> T;
  std::string row;

  for (unsigned int t = 0; t < T; ++t) {
    std::cin >> row;
    std::vector<unsigned short> rowV;
    for (const auto &i : row) {
      rowV.push_back(static_cast<unsigned int>(i) - 48);
    }
    int i = rowV.size() - 1;
    while (i >= 0) {
      if (i > 0) {
        if (rowV[i] >= rowV[i - 1]) {
          --i;
        } else {
          if (i == rowV.size() - 1) {
            rowV[i - 1]--;
            rowV[i] = 9;
          } else {
            rowV[i - 1]--;
            for (unsigned int h = i; h < rowV.size(); ++h) {
              rowV[h] = 9;
            }
          }
          checkNegative(rowV);
          --i;
        }
      } else {
        if (rowV[i] > rowV[i + 1]) {
          rowV[i]--;
          for (unsigned int d = i + 1; d < rowV.size() - 1; ++d) {
            rowV[d] = 9;
          }
        }
        --i;
      }
    }
    std::cout << "Case #" << t + 1 << ": ";
    showVector(rowV);
    std::cout << std::endl;
  }
  return 0;
}
