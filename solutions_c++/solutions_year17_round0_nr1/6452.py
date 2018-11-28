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

char reverse(const char c) {
  if (c == '-') {
    return '+';
  } else {
    return '-';
  }
}

int Solve(const std::string& str, const int flips) {

  // std::cout << str << " " << flips <<"\n";

  std::string str_copy = str;
  int count = 0;

  for (int i = 0; i + flips <= str.length(); ++i) {
    if (str_copy[i] == '-') {
      ++count;
      for (int j = 0; j < flips; ++j) {
        str_copy[i + j] = reverse(str_copy[i + j]);
      }
      // std::cout << str_copy << "\n";
    }
  }

  bool flag = true;
  for (int i = 0; i < str.length(); ++i) {
    if (str_copy[i] == '-') {
      flag = false;
      break;
    }
  }

  if (flag) {
    return count;
  } else {
    return -1;
  }
}

void printAnswer(const int test, const int x) {
  if (x >= 0) {
    std::cout << "Case #" << test << ": " << x << "\n";
  } else {
    std::cout << "Case #" << test << ": IMPOSSIBLE\n";
  }
  }

int main() {

  // std::ifstream in("input.txt", 'r');
  // std::ofstream out("output.txt", std::ofstream::out);

  // out << "kek\n";

  int T = readInt();

  for (int i = 0; i < T; ++i) {
    std::string str = readStr();
    int flips = readInt();
    int answer = Solve(str, flips);
    printAnswer(i + 1, answer);
  }

}