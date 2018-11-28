#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define f first
#define s second
#define pb push_back
#define pp pop_back
#define mp make_pair
#define ll long long
#define ld long double
#define ull unsigned long long
#define PI pair < int, int > 

const int N = 123;
const int M = 123;
const ld Pi = acos(-1);
const ll Inf = 1e18;
const int inf = 1e2;
const int mod = 1e9 + 7;
const ld eps = 1e-12;

void add(int &a, int b) {
  a += b;
  if (a >= mod) a -= mod;
}
int mult(int a, int b) {
  return 1ll * a * b % mod;
}
int sum(int a, int b) {
  add(a, b);
  return a;
}

int id, t, n, cnt[3], k;

void solve() {
  int trash;
  cin >> n >> k;
  int ans = 0;
  if (k == 2) {
    int count = 0;
    for (int i = 1;i <= n;i++) {
      int x; cin >> x;
      if (x % 2) {
        count++;
      } else ans++;
    }
    ans += (count + 1) / 2;
  }
  if (k == 3) {
    memset(cnt, 0, sizeof cnt);
    for (int i = 1, x;i <= n;i++) {
      cin >> x;
      cnt[x % 3]++;
    }
    ans += cnt[0];
    int tmp = min(cnt[1], cnt[2]);
    ans += tmp;
    cnt[1] -= tmp;
    cnt[2] -= tmp;
    int rem = 0;
    while(cnt[1] > 0) {
      if (rem == 0) {
        rem = 2;
        ans++;
      } else {
        if (rem == 1) {
          rem = 0;
        } else {
          rem = 1;
        }
      }
      cnt[1]--;
    }
    while(cnt[2] > 0) {
      if (rem == 0) {
        ans++;
        rem = 1;
      } else {
        if (rem == 1) {
          rem = 2;
        } else {
          rem = 0;     
        }      
      }
      cnt[2]--;
    }
  }
  if (k == 4) {

  }
  id++;
  cout << "Case #" << id << ": " << ans << endl;
}
int main() {
  #ifdef wws
    freopen("in", "r", stdin);
    freopen("out", "w", stdout); 
  #endif 
  ios_base::sync_with_stdio(0);
  cin >> t;
  while(t--) solve();
  return 0; 
}