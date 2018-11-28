#include <iostream>
#include <fstream>

#include <string>
#include <vector>

using std::vector;
using std::string;

void work(std::ifstream& in, std::ofstream& out) {
  string s;
  size_t size;
  in >> s >> size;
  size_t res = 0;
  for (size_t i = 0; i < s.size(); ++i) {
    if (s[i] == '-') {
      if (i + size > s.size()) {
        out << "IMPOSSIBLE" << std::endl;
        return;
      }
      for (size_t j = 0; j < size; ++j) {
        s[i + j] = '+' + '-' - s[i + j];
      }
      ++res;
    }
  }
  out << res << std::endl;
}

int main() {

  std::ifstream in("input.txt");
  std::ofstream out("output.txt");

  size_t T;
  in >> T;

  for (size_t i = 0; i < T; ++i) {
    out << "Case #" << i + 1 << ": ";
    work(in, out);
  }
  return 0;
}