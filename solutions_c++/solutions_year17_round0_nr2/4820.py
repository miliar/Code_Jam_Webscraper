#include <iostream>
#include <fstream>

#include <string>
#include <vector>

using std::vector;
using std::string;

void work(std::ifstream& in, std::ofstream& out) {
  string s;
  in >> s;
  for (size_t i = s.size() - 1; i > 0; --i) {
    if (s[i - 1] > s[i]) {
      for (size_t j = i; j < s.size(); ++j) {
        s[j] = '9';
      }
      --s[i - 1];
    }
  }
  if (s[0] < '1') {
    s[0] = ' ';
  }
  out << s << std::endl;
}

int main() {

  std::ifstream in("input.in");
  std::ofstream out("output.out");

  size_t T;
  in >> T;

  for (size_t i = 0; i < T; ++i) {
    out << "Case #" << i + 1 << ": ";
    work(in, out);
  }
  return 0;
}