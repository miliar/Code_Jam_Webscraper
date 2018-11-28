#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>

using namespace std;

#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define rep(i,a)      for(int i=0;i<a;i++)
#define rep2(i,a,b)      for(int i=a;i<b;i++)
using namespace std;

static unsigned long long make_tidy(unsigned long long n) {
  unsigned long long i = n;
  int digits[20];
  int x = 0;
  while (i) {
    digits[x++] = i % 10;
    i /= 10;
  }

  if (x == 1)
    return n;

  unsigned long long res = 0;
  for (int k = x - 1; k > 0; k--) {
    res *= 10;
    res += digits[k];
    if (digits[k] <= digits[k - 1])
      continue;

    // Not tidy: make it tidy recursively.
    res *= 10;
    res -= 1;
    k--;
    for (; k > 0; k--) {
      res *= 10;
      res += 9;
    }

    return make_tidy(res);
  }

  // All tidy.

  res *= 10;
  res += digits[0];
  return res;
}

int test = 1;
void solve() {
  cout << "Case #" << test++ << ": ";
  unsigned long long n;
  cin >> n;
  cout << make_tidy (n) << endl;
}

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
