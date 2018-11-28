#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cassert>
using namespace std;

#define sz(a) int(a.size())
#define rep(i, s, n)  for(int i = s; i <= n; ++i)
#define rev(i, n, s)  for(int i = n; i >= s; --i)
#define fore(x, a) for(auto &&x : a)
typedef long long ll;
const int mod = 1000000007;
const int N = 100005;

int a[N];


int main() {
#ifdef loc
  if(!freopen((string(FOLDER) + "inp.txt").c_str(), "r", stdin)) {
    assert(0);
  }
  freopen((string(FOLDER) + "out.txt").c_str(), "w", stdout);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int num_tests;
  cin >> num_tests;
  rep(_, 1, num_tests) {
    cout << "Case #" << _ << ": ";
    int n, p;
    cin >> n >> p;
    rep(i, 0, n - 1) {
      cin >> a[i];
      a[i] %= p;
    }
    int ans = 0;
    if(p == 2) {
      int one = 0;
      rep(i, 0, n - 1) {
        if(a[i] == 0) {
          ans++;
        } else {
          one++;
        }
      }
      ans += (one + 1) / 2;
    } else if(p == 3) {
      int one = 0, two = 0;
      rep(i, 0, n - 1) {
        if(a[i] == 0) {
          ans++;
        } else if(a[i] == 1) {
          one++;
        } else {
          two++;
        }
      }
      int x = min(one, two);
      ans += x;
      one -= x;
      two -= x;
      ans += (max(one, two) + 2) / 3;
    } else {
      int one = 0, two = 0, thr = 0;
      rep(i, 0, n - 1) {
        if(a[i] == 0) {
          ans++;
        } else if(a[i] == 1) {
          one++;
        } else if(a[i] == 2) {
          two++;
        } else {
          thr++;
        }
      }
      int x = two / 2;
      ans += x;
      two -= 2 * x;
      x = min(one, thr);
      ans += x;
      one -= x;
      thr -= x;
      one = max(one, thr);
      if(two) {
        if(one >= 2) {
          one -= 2;
          ans++;
          ans += (one + 3) / 4;
        } else {
          ans++;
        }
      } else {
        ans += (one + 3) / 4;
      }
    }
    cout << ans << endl;
  }
  return 0;
}