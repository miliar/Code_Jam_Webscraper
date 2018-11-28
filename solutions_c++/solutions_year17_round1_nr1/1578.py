#include <algorithm>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>

void setArray(char* array, size_t ncol, size_t row, size_t col, char c) {
  size_t idx = row * ncol + col;
  array[idx] = c;
}
char getArray(char* array, size_t ncol, size_t row, size_t col) {
  size_t idx = row * ncol + col;
  return array[idx];
}

int main(int argc, char** argv) {
  if (argc <= 2) return -1;

  std::ifstream ifs(argv[1]);
  std::ofstream ofs(argv[2]);
  int nCase = 0;
  ifs >> nCase;
  std::cout << "#Cases: " << nCase << std::endl;
  char* board = new char[100 * 100];
  for (size_t i = 0; i < nCase; ++i) {
    int nrow, ncol;
    ifs >> nrow >> ncol;

    std::cout << "Case #" << i + 1 << ": " << std::endl;
    ofs << "Case #" << i + 1 << ": " << std::endl;

    for (int j = 0; j < nrow; j++) {
      std::string row_string;
      ifs >> row_string;
      for (size_t k = 0; k < ncol; k++) {
        setArray(board, ncol, j, k, row_string[k]);
      }
    }
    for (int j = 0; j < nrow; j++) {
      char fill_c = '?';
      for (int k = 0; k < ncol; k++) {
        char cur_c = getArray(board, ncol, j, k);
        if (cur_c == '?') {
          setArray(board, ncol, j, k, fill_c);
        } else {
          fill_c = cur_c;
        }
      }
      fill_c = '?';
      for (int k = ncol - 1; k >= 0; k--) {
        char cur_c = getArray(board, ncol, j, k);
        if (cur_c == '?') {
          setArray(board, ncol, j, k, fill_c);
        } else {
          fill_c = cur_c;
        }
      }
    }
    for (int k = 0; k < ncol; k++) {
      char fill_c = '?';
      for (size_t j = 0; j < nrow; j++) {
        char cur_c = getArray(board, ncol, j, k);
        if (cur_c == '?') {
          setArray(board, ncol, j, k, fill_c);
        } else {
          fill_c = cur_c;
        }
      }
      fill_c = '?';
      for (int j = nrow - 1; j >= 0; j--) {
        char cur_c = getArray(board, ncol, j, k);
        if (cur_c == '?') {
          setArray(board, ncol, j, k, fill_c);
        } else {
          fill_c = cur_c;
        }
      }
    }
    std::string row_string;
    row_string.resize(ncol);
    for (int j = 0; j < nrow; j++) {
      for (int k = 0; k < ncol; k++) {
        row_string[k] = getArray(board, ncol, j, k);
      }
      std::cout << row_string << std::endl;
      ofs << row_string << std::endl;
    }
  }
}
