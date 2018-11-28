#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define DEBUG(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long double ld;
typedef long long ll;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

vector<vector<char> > add_bishops(vector<vector<char> > board) {
  int n = int(board.size());
  vector<char> diag1_free(2 * n - 1, 1);
  vector<char> diag2_free(2 * n - 1, 1);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (board[i][j] == 1) {
        diag1_free[i + j] = 0;
        diag2_free[i - j + n - 1] = 0;
      }
    }
  }
  while (true) {
    vector<int> diag1_free_count(diag1_free.size(), 0);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (diag1_free[i + j] == 1 && diag2_free[i - j + n - 1] == 1) {
          ++diag1_free_count[i + j];
        }
      }
    }
    int d1 = -1;
    for (int d = 0; d < int(diag1_free.size()); ++d) {
      if (diag1_free_count[d] > 0 && (d1 == -1 || diag1_free_count[d] < diag1_free_count[d1])) {
        d1 = d;
      }
    }
    if (d1 == -1) {
      break;
    }
    int row = -1, col = -1;
    for (int i = 0; i < n; ++i) {
      int j = d1 - i;
      if (j >= 0 && j < n && diag2_free[i - j + n - 1] == 1) {
        row = i;
        col = j;
        break;
      }
    }
    board[row][col] = 1;
    diag1_free[row + col] = 0;
    diag2_free[row - col + n - 1] = 0;
  }
  return board;
}

vector<vector<char> > add_rooks(vector<vector<char> > board) {
  int n = int(board.size());
  vector<char> row_free(n, 1);
  vector<char> col_free(n, 1);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (board[i][j]) {
        row_free[i] = 0;
        col_free[j] = 0;
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    if (row_free[i] == 1) {
      int j = 0;
      while (j < n && col_free[j] == 0) {
        ++j;
      }
      assert(j < n);
      board[i][j] = 1;
      col_free[j] = 0;
    }
  }
  return board;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n, m;
    cin >> n >> m;
    vector<vector<char> > bishop(n, vector<char>(n, 0));
    vector<vector<char> > rook(n, vector<char>(n, 0));
    for (int i = 0; i < m; ++i) {
      char type;
      int row, col;
      cin >> type >> row >> col;
      --row;
      --col;
      if (type == '+' || type == 'o') {
        bishop[row][col] = 1;
      }
      if (type == 'x' || type == 'o') {
        rook[row][col] = 1;
      }
    }
    vector<vector<char> > bishop2 = add_bishops(bishop);
    vector<vector<char> > rook2 = add_rooks(rook);

    int points = 0;
    int models_added = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (bishop2[i][j] == 1) {
          ++points;
        }
        if (rook2[i][j] == 1) {
          ++points;
        }
        if (bishop2[i][j] != bishop[i][j] || rook2[i][j] != rook[i][j]) {
          ++models_added;
        }
      }
    }
    cout << "Case #" << ca << ": " << points << " " << models_added << endl;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (bishop2[i][j] != bishop[i][j] || rook2[i][j] != rook[i][j]) {
          if (bishop2[i][j] && rook2[i][j]) {
            cout << "o";
          } else if (bishop2[i][j]) {
            cout << "+";
          } else {
            cout << "x";
          }
          cout << " " << i + 1 << " " << j + 1 << endl;
        }
      }
    }
  }
}
