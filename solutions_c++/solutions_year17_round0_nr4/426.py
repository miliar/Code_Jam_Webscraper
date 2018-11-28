#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <tuple>

using namespace std;

const int N_MAX = 120;
int N;
char rect_grid[N_MAX][N_MAX];
char diag_grid[N_MAX][N_MAX];

void print_rect() {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++)
      cout << rect_grid[i][j];
    cout << endl;
  }
}

void print_diag() {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++)
      cout << diag_grid[i][j];
    cout << endl;
  }
}

void place_rect(char val, int r, int c) {
  for (int i = 0; i < N; i++) {
    rect_grid[r][i] = rect_grid[i][c] = 'x';
  }
  rect_grid[r][c] = val;
}

void place_diag(char val, int r, int c) {
  for (int i = 0; i < N; i++) {
    int d = r - i;
    if (0 <= c - d && c - d < N)
      diag_grid[i][c - d] = 'x';
    if (0 <= c + d && c + d < N)
      diag_grid[i][c + d] = 'x';
  }
  diag_grid[r][c] = val;
}



void init() {
  int M;
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      rect_grid[i][j] = diag_grid[i][j] = '.';
    }
  }

  for (int i = 0; i < M; i++) {
    char x;
    int r, c;
    cin >> x >> r >> c;
    if (x == '+' || x == 'o')
      diag_grid[r - 1][c - 1] = 'a';
    if (x == 'x' || x == 'o')
      rect_grid[r - 1][c - 1] = 'b';
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (rect_grid[i][j] == 'b')
        place_rect('b', i, j);
      if (diag_grid[i][j] == 'a')
        place_diag('a', i, j);
    }
  }
}

void solve_case(int t) {
  init();

  // print_rect();
  // print_diag();

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (rect_grid[i][j] == '.')
        place_rect('B', i, j);
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j <= i; j++) {
      int r = i - j, c = j;
      if (diag_grid[r][c] == '.')
        place_diag('A', r, c);
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j <= i; j++) {
      int r = N - 1 - j, c = N - 1 - i + j;
      if (diag_grid[r][c] == '.')
        place_diag('A', r, c);
    }
  }

  // print_rect();
  // print_diag();

  int score = 0;
  vector<tuple<char,int,int>> additions;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      char rect = rect_grid[i][j];
      char diag = diag_grid[i][j];
      assert(rect != '.' && diag != '.');
      if (rect != 'x') score++;
      if (diag != 'x') score++;

      if (diag == 'A' || rect == 'B') {
        char update = 'o';
        if (diag == 'x')
          update = 'x';
        else if (rect == 'x')
          update = '+';
        additions.push_back(make_tuple(update, i + 1, j + 1));
      }
    }
  }

  cout << "Case #" << t << ": " << score << " " << additions.size() << "\n";
  for (int i = 0; i < additions.size(); i++) {
    auto model = additions[i];
    cout << get<0>(model) << " " << get<1>(model) << " " << get<2>(model) << "\n";
  }
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
