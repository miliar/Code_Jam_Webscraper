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

#define sz(a) int((a).size())
#define rep(i, s, n)  for(int i = s; i <= (n); ++i)
#define rev(i, n, s)  for(int i = (n); i >= s; --i)
#define fore(x, a) for(auto &&x : a)
typedef long long ll;
const int mod = 1000000007;
const int N = 100005;

int ans[55][55];

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
  int t;
  cin >> t;
  rep(z, 1, t) {
    cout << "Case #" << z << ": ";
    ll n, k;
    cin >> n >> k;
    ll nk = 1, temp = k;
    while(temp > 1) {
      temp /= 2;
      nk *= 2;
    }
    ll ret = (n - k) / nk + 1;
    cout << ret / 2 << " " << (ret - 1) / 2 << endl;
  }
  return 0;
}