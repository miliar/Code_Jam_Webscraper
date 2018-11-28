#include <cstdint>
#include <vector>
#include <algorithm>
#include <cstdio>

uint64_t get_tidy_number(uint64_t input) {
  std::vector<uint64_t> digits;
  for (uint64_t rest = input; rest; rest /= 10) digits.push_back(rest % 10);
  std::reverse(digits.begin(), digits.end());
  int i = 0;
  for (int k = 0; k < digits.size(); k++) {
    bool found = false;
    for (i = 0; i < digits.size() - 1; i++) {
      if (digits[i] > digits[i+1]) {
        found = true;
        break;
      }
    }
    if (! found) break;
    digits[i] -= 1;
    for (int j = i+1; j < digits.size(); j++) {
      digits[j] = 9;
    }
  }
  uint64_t result = 0;
  for (int j = 0; j < digits.size(); j++) {
    result *= 10;
    result += digits[j];
  }
  return result;
}

std::vector<uint64_t> read_input(char * filename) {
  FILE * f = fopen(filename, "r");
  std::vector<uint64_t> ret;
  int num;
  uint64_t val;
  fscanf(f, "%d\n", &num);
  for (int i = 0; i < num; i++) {
    fscanf(f, "%zu\n", &val);
    ret.push_back(val);
  }
  fclose(f);
  return ret;
}

int main(int argc, char ** argv) {
  std::vector<uint64_t> input = read_input(argv[1]);
  for (int i = 0; i < input.size(); i++) {
    printf("Case #%d: %zu\n", i+1, get_tidy_number(input[i]));
  }
}
