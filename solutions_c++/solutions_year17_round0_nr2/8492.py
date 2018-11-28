#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

bool is_tidy_number(uint64_t number) {
  std::string num = std::to_string(number);
  if (num.length() == 1) return true;
  char last_num = num[0];
  for (int i = 1; i < num.length(); i++) {
    if ((int(num[i]) - 48) < (int(last_num) - 48))
      return false;
    last_num = num[i];
  }
  return true;
}

uint64_t get_last_tidy_number(uint64_t number) {
  for (uint64_t i = number; i > 0; i--) {
    if (is_tidy_number(i))
      return i;
    std::string t = std::to_string(i);
    for (int j = 1; j < t.length(); j++) {
      if (t[j] < t[j - 1]) {
        for (; j < t.length(); j++)
          t[j] = '0';
      }
    }
    i = strtoll(t.c_str(), NULL, 10);
  }
  return -1;
}

int main(int argc, char **args) {
  int test_cases = 0;
  uint64_t num = 0;
  cin >> test_cases;
  for (int i = 1; i <= test_cases; i++) {
    cin >> num;
    cout << "Case #" << i << ": " << get_last_tidy_number(num) << endl;
  }
  return 0;
}
