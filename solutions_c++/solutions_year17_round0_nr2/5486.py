#include <cstdio>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
using namespace std;

ll solve(ll num) {
  vector<int> d;
  int n = 0;
  while (num > 0) {
    d.push_back(num % 10);
    num /= 10;
    n++;
  }
  reverse(d.begin(), d.end());
  // premier chiffre en 0, dernier chiffre en n-1

  bool is_tidy = false;
  while (true)
  {
    int i = 0;
    while (i < n-1 && d[i] <= d[i+1]) {
      i++;
    }
    if (i == n-1) {
      is_tidy = true;
    }
    if (is_tidy) {
      break;
    } else {
      assert(d[i] != 0);
      d[i] = d[i] - 1;
      for (int j = i+1; j < n; j++) {
        d[j] = 9;
      }
    }
  }

  ll res = 0;
  for (auto c : d) {
    res *= 10;
    res += c;
  }

  return res;
}

int main(int nargs, char **argv) {
    std::ios::sync_with_stdio(false);
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
      ll n;
      cin >> n;
      cout << "Case #" << i << ": ";
      cout << solve(n) << endl;
    }
    return 0;
}
