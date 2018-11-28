#include <algorithm>
#include <iostream>
#include <string>
#include <vector>


namespace {

std::vector<std::string> Solve(std::vector<std::string> cake) {
  const int C = cake[0].size();
  auto fill = [](std::string& row) {
    char letter = '?';
    for (char c : row) {
      if (c != '?') {
        letter = c;
        break;
      }
    }
    for (char& c : row) {
      if (c == '?') {
        c = letter;
      } else {
        letter = c;
      }
    }
  };
  for (std::string& row : cake) fill(row);
  const std::string empty_row(C, '?');
  std::string reference = *std::find_if(cake.begin(), cake.end(),
                                        [&empty_row](const std::string& row) {
                                          return row != empty_row;
                                        });
  for (std::string& row : cake) {
    if (row == empty_row) {
      row = reference;
    } else {
      reference = row;
    }
  }
  return cake;
}

}  // namespace


int main(void) {
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; ++i) {
    int R, C;
    std::cin >> R >> C;
    std::vector<std::string> cake(R);
    for (int j = 0; j < R; ++j) {
      std::cin >> cake[j];
    }
    std::cout << "Case #" << i << ":" << std::endl;
    for (const auto& row : Solve(cake)) {
      std::cout << row << std::endl;
    }
  }

  return 0;
}
