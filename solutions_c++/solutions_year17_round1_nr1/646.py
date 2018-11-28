#include <iostream>
#include <string>
#include <vector>


int main() {
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t) {
    int r, c;
    std::cin >> r >> c;
    std::vector<std::string> cake(r);
    for (auto& row : cake)
      std::cin >> row;
    int first_nonempty_row = -1;
    for (int i = 0; i < r; ++i) {
      if (cake[i].find_first_not_of('?') == std::string::npos) {
        if (first_nonempty_row != -1)
          cake[i] = cake[i-1];
      }
      else
      {
        if (first_nonempty_row == -1)
          first_nonempty_row = i;
        int first_nonempty_column = cake[i].find_first_not_of('?');
        for (int j = 0; j < c; ++j) {
          if (cake[i][j] != '?')
            continue;
          if (j < first_nonempty_column)
            cake[i][j] = cake[i][first_nonempty_column];
          else
            cake[i][j] = cake[i][j-1];
        }
      }
    }
    for (int i = 0; i < first_nonempty_row; ++i)
      cake[i] = cake[first_nonempty_row];

    std::cout << "Case #" << t+1 << ":" << std::endl;
    for (auto row : cake)
      std::cout << row << std::endl;
  }
  return EXIT_SUCCESS;
}
