#include <iostream>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>

void solve() {
  int r, c;
  int nonempty_r = -1;
  int nonempty_c = -1;
  char cake[32][32];

  std::cin >> r >> c;

  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      std::cin >> cake[i][j];
    }
  }

  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      if (cake[i][j] != '?') {
        nonempty_r = i;
        nonempty_c = j;
        break;
      }
    }
    if (nonempty_r != -1) {
      break;
    }
  }

  char fill = cake[nonempty_r][nonempty_c];
  for (int j = 0; j < c; j++) {
    if (cake[nonempty_r][j] == '?') {
      cake[nonempty_r][j] = fill;
    } else {
      fill = cake[nonempty_r][j];
    }
  }

  for (int i = nonempty_r - 1; i >= 0; i--) {
    for (int j = 0; j < c; j++) {
      cake[i][j] = cake[i + 1][j];
    }
  }

  for (int i = nonempty_r + 1; i < r; i++) {
    char fill = '?';
    for (int j = 0; j < c; j++) {
      if (cake[i][j] != '?') {
        fill = cake[i][j];
        break;
      }
    }

    if (fill != '?') {
      // case 1: non-empty row
      for (int j = 0; j < c; j++) {
        if (cake[i][j] == '?') {
          cake[i][j] = fill;
        } else {
          fill = cake[i][j];
        }
      }
    } else {
      // case 1: empty row
      for (int j = 0; j < c; j++) {
        cake[i][j] = cake[i - 1][j];
      }
    }
  }

  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      std::cout << cake[i][j];
    }
    std::cout << std::endl;
  }

}

int main(int argc, char *argv[]) {
  int ncase;
  std::cin >> ncase;

  for (int i = 1; i <= ncase; i++) {
    std::cout << "Case #" << i << ":" << std::endl;
    solve();
  }

	return 0;
}
