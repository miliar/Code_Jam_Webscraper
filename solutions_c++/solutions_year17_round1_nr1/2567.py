#include <iostream>
#include <limits>
#include <bitset>
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <unordered_map>

using namespace std;

typedef unsigned long long ull;
const ull IMPOSSIBLE = std::numeric_limits<ull>::max(); 


int main() {
  std::ios::sync_with_stdio(false);

  ull T; cin >> T;
  for (ull i = 1; i <= T; ++i) {
		ull R, C; cin >> R >> C;
    vector<string> cake(R);
    for (auto& r : cake) {
      cin >> r;
    }
    cout << "Case #" << i << ":\n";

    auto fill_right = [&cake, C](size_t r, size_t c) {
      bool filled = false;
      char initial = cake[r][c];
      for (size_t i = c+1; i < C; ++i) {
        char& pos = cake[r][i];
        if (pos == '?') {
          pos = initial;
          filled = true;
        } else {
          break;
        }
      }
      return filled;
    };

    auto fill_left = [&cake](size_t r, size_t c) {
      bool filled = false;
      if (c > 0) {
        char initial = cake[r][c];
        for (ssize_t i = c - 1; i >= 0; --i) {
          char& pos = cake[r][i];
          if (pos == '?') {
            pos = initial;
            filled = true;
          } else {
            break;
          }
        }
      }
      return filled;
    };

    auto fill_up = [&cake](size_t r, size_t c) {
      bool filled = false;
      if (r > 0) {
        char initial = cake[r][c];
        for (ssize_t i = r-1; i >=0; --i) {
          char& pos = cake[i][c];
          if (pos == '?') {
            pos = initial;
            filled = true;
          } else {
            break;
          }
        }
      }
      return filled;
    };

    auto fill_down = [&cake, R](size_t r, size_t c) {
      bool filled = false;
      char initial = cake[r][c];
      for (size_t i = r+1; i < R; ++i) {
        char& pos = cake[i][c];
        if (pos == '?') {
          pos = initial;
          filled = true;
        } else {
          break;
        }
      }
      return filled;
    };

    int count = 1;
    while (count > 0) {
      count = 0;
      for (size_t r = 0; r < R; ++r) {
        bool filled_row = false;
        for (size_t c = 0 ; c < C; ++c) {
          if (cake[r][c] != '?') {
            bool filled_right = fill_right(r,c);
            bool filled_left = fill_left(r,c);
            filled_row = filled_row || (filled_right || filled_left);
            if (filled_right || filled_left) {
              // cout << "Filled row at (" << r << ',' << c << ")\n";
            }
          } else {
            ++count;
          }
        }

        if (!filled_row) {
          for (size_t c = 0 ; c < C; ++c) {
            if (cake[r][c] != '?') {
              bool filled_up = fill_up(r,c);
              bool filled_down = fill_down(r,c);
              if (filled_up || filled_down) {
              }
            } else {
              ++count;
            }
          }
        }
      }
    }

    for (const auto& r : cake) {
      cout << r << '\n';
    }
  }
}
