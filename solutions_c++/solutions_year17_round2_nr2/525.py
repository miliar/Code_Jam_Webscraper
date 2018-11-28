#include <algorithm>
#include <chrono>
#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;
using namespace std::chrono;

struct state_t {
  vector<int> cnt;
  int last;

  state_t() {
    cnt.resize(6);
    cnt.assign(6, 0);
  }

  int get_sum() const {
    int res = 0;
    for (int i = 0; i < 6; ++i)
      res += cnt[i];
    return res;
  }

  bool operator <(const state_t& it) const {
    int sum = get_sum();
    int itsum = it.get_sum();

    if (sum < itsum)
      return true;
    else if (sum > itsum)
      return false;

    for (int i = 0; i < 6; ++i) {
      if (cnt[i] < it.cnt[i])
        return true;
      else if (cnt[i] > it.cnt[i])
        return false;
    }

    return last < it.last;
  }
};

vector<char> color = {'R', 'O', 'Y', 'G', 'B', 'V'};

char get_color(int c) {
  return color[c];
}

bool has_red(int c) {
  return c == 0 || c == 1 || c == 5;
}

bool has_yellow(int c) {
  return c == 1 || c == 2 || c == 3;
}

bool has_blue(int c) {
  return c == 3 || c == 4 || c == 5;
}

bool can_set(int p, int n) {
  int common = 0;
  common += has_red(p) && has_red(n);
  common += has_yellow(p) && has_yellow(n);
  common += has_blue(p) && has_blue(n);
  return common == 0;
}

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int n;
    vector<int> cnt(6, 0);
    cin >> n;
    for (int i = 0; i < 6; ++i)
      cin >> cnt[i];

    int r = cnt[0], y = cnt[2], b = cnt[4];

    if (2 * r > n || 2 * y > n || 2 * b > n) {
      cout << "Case #" << test << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << test << ": ";

      int prev = 0;
      for (int i = 0; i < 6; ++i)
        if (cnt[i] > cnt[prev])
          prev = i;
      int first = prev;

      while (prev >= 0) {
        cout << get_color(prev);
        --cnt[prev];
        int buf = -1;
        for (int i = 0; i < 6; ++i) {
          if (cnt[i] == 0)
            continue;
          if (can_set(prev, i)) {
            if (buf == -1)
              buf = i;
            else if (cnt[i] > cnt[buf])
              buf = i;
            else if (cnt[i] == cnt[buf] && i == first)
              buf = i;
          }
        }
        prev = buf;
      }
      cout << endl;

    }

  }


  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
