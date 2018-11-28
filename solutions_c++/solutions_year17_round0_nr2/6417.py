#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::string readStr() {
  std::string str;
  std::cin >> str;
  return str;
}

int readInt() {
  int x;
  std::cin >> x;
  return x;
}

int64_t readInt64() {
  int64_t x;
  std::cin >> x;
  return x;
}

int64_t pow(const int64_t x, const int deg) {
  int64_t result = 1;
  for (int i = 0; i < deg; ++i) {
    result *= x;
  }
  return result;
}

int64_t Solve(const int64_t x, int64_t max_level = 17) {
  if (max_level == -1) {
    return 0;
  }
  int64_t power = (pow(10, max_level + 1) - 1) / 9;
  bool flag = true;
  int64_t cipher = 0;
  while(cipher < 10) {
    if (cipher * power > x) {
      break;
    }
    ++cipher;
  }
  --cipher;
  // std::cout << "cipher = " << cipher << "\n";
  return cipher * pow(10, max_level) + Solve(x - cipher * pow(10, max_level), max_level - 1);
}

void printAnswer(const int test, const int64_t x) {
  std::cout << "Case #" << test << ": " << x << "\n";
}

int main() {

  int T = readInt();

  for (int i = 0; i < T; ++i) {
    int64_t number = readInt64();
    int64_t answer = Solve(number);
    printAnswer(i + 1, answer);
  }

}