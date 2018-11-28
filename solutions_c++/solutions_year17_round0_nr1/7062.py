#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

void get_params(const std::string &in_line, std::string &pancake, int &pan_size) {
  char *dup = strdup(in_line.c_str());
  char *tok = strtok(dup, " ");
  pancake = std::string(tok);
  tok = strtok(NULL, " ");
  pan_size = std::atoi(tok);
}



int Solve(std::string pancake, const int &pan_size) {
  int flip = 0;
  for (int i = 0; i < pancake.size() - pan_size + 1; i++) {
    if (pancake[i] == '-') {
      flip++;
      for (int j = 0; j < pan_size; j++) {
        if (pancake[i + j] == '-') {
          pancake[i + j] = '+';
        }
        else {
          pancake[i + j] = '-';
        }
      }
    }
  }
  bool is_valid = true;
  for (int i = 0; i < pancake.size(); i++) {
    if (pancake[i] == '-') is_valid = false;
  }
  if (is_valid) {
    return flip;
  }
  else {
    return -1;
  }
}

int main() {
  std::string in_line;
  std::getline(std::cin, in_line);
  const int n_cases = std::atoi(in_line.c_str());
  for (int i = 0; i < n_cases; i++) {
    std::getline(std::cin, in_line);
    std::string pancake;
    int pan_size;
    get_params(in_line, pancake, pan_size);
    int res = Solve(pancake, pan_size);
    printf("Case #%d: ", i + 1);
    if (res == -1) {
      printf("IMPOSSIBLE\n");
    }
    else {
      printf("%d\n", res);
    }
  }
  return 0;
}