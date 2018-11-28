#include <iostream>
#include <string>

void print(int caseNum, std::string output) {
  std::cout << "Case #" << caseNum << ": " << output << std::endl;
}

int main() {
  std::string line;
  getline(std::cin, line);
  int T = std::stoi(line);

  for (int t = 1; t <= T; ++t) {
    getline(std::cin, line);
    size_t pos = line.find(" ");
    int R = std::stoi(line.substr(0, pos));
    int C = std::stoi(line.substr(pos+1));

    char grid[25][25] = {};
    for (int r = 0; r < R; ++r) {
      getline(std::cin, line);
      for (int c = 0; c < C; ++c) {
        grid[r][c] = line[c];
      }
    }

    for (int r = 0; r < R; ++r) {
      char lastChar = '?';
      for (int c = 0; c < C; ++c) {
        if (grid[r][c] == '?' && lastChar != '?') {
          grid[r][c] = lastChar;
        }
        lastChar = grid[r][c];
      }
    }

    for (int r = 0; r < R; ++r) {
      char lastChar = '?';
      for (int c = C-1; c >= 0; --c) {
        if (grid[r][c] == '?' && lastChar != '?') {
          grid[r][c] = lastChar;
        }
        lastChar = grid[r][c];
      }
    }

    int lastRowWithChar = -1;
    for (int r = 0; r < R; ++r) {
      if (grid[r][0] == '?' && lastRowWithChar >= 0) {
        for (int c = 0; c < C; ++c) {
          grid[r][c] = grid[r-1][c];
        }
      } else {
        lastRowWithChar = r;
      }
    }

    for (int r = R-1; r >= 0; --r) {
      if (grid[r][0] == '?') {
        for (int c = 0; c < C; ++c) {
          grid[r][c] = grid[r+1][c];
        }
      }
    }

    std::cout << "Case #" << t << ":" << std::endl;
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        std::cout << grid[r][c];
      }
      std::cout << std::endl;
    }
  }

  return 0;
}
