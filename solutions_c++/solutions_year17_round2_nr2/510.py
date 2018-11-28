#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long li;
typedef long double ld;

const int N = 10;

int n;
vector<int> a;

char get_char(int color) {
  if (color == 1)
    return 'R';
  if (color == 2)
    return 'Y';
  if (color == 4)
    return 'B';
  if (color == 3)
    return 'O';
  if (color == 5)
    return 'V';
  if (color == 6)
    return 'G';
  throw;
}

std::string solve() {
  for (int i = 1; i <= 4; ++i) {
    if (a[i] > n / 2) {
      return "IMPOSSIBLE";
    }
  }

  vector<int> x;
  x.push_back(1);
  x.push_back(2);
  x.push_back(4);

  vector<int> p;
  for (int i = 0; i < n; i += 2)
    p.push_back(i);
  for (int i = 1; i < n; i += 2)
    p.push_back(i);

  do {
    int cur = 0;
    string ans;
    ans.resize(n);
    for (int i = 0; i < 3; ++i)
      for (int j = 0; j < a[x[i]]; ++j)
        ans[p[cur++]] = get_char(x[i]);

    if (ans[0] == ans.back())
      continue;
    bool good = true;
    for (int i = 0; i + 1 < ans.size(); ++i)
      if (ans[i] == ans[i + 1]) {
        good = false;
        break;
      }

    if (good)
      return ans;
  } while (next_permutation(x.begin(), x.end()));

  return "IMPOSSIBLE";
}

int main() {
  int tests;
  cin >> tests;

  cout.precision(10);
  cout << fixed;

  for (int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    // red = 1
    // yellow = 2
    // blue = 4
    // red + yellow = orange = 3
    // red + blue = violet = 5
    // yellow + blue = green = 6
    a.assign(10, 0);
    cin >> n >> a[1] >> a[3] >> a[2] >> a[6] >> a[4] >> a[5];

    cout << solve() << endl;
  }
  return 0;
}