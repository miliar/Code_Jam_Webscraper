/*
  by Nazarbek Altybay
  nazarbek.altybay@gmail.com
*/

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

#define f first
#define s second

#define pb push_back
#define mp make_pair

using namespace std;

const int N = (int) 1e6 + 7;
const int MOD = (int) 1e9 + 7;

const int magic = 2000;

int hd, ad, hk, ak, b, d;
int A, B, C, D, E, F;

void init() {
  hd = A;
  ad = B;
  hk = C;
  ak = D;
  b = E;
  d = F;
}
  
void solve() {
  cin >> A >> B >> C >> D >> E >> F;
  
  int ans = MOD;
  for (int cb = 0; cb <= 100; cb++) {
    for (int cd = 0; cd <= 100; cd++) {
      int moves = 0;
      init();
      int cdd = cd;
      while (cdd > 0 && moves <= magic) {
        if (hd - max(0, ak - d) <= 0) {
          hd = A;
          moves++;
          hd -= ak;
        } else {
          ak = max(0, ak - d);
          moves++;
          cdd--;
          hd -= ak;
        }
          if (hd <= 0) break;
      }
      int cbb = cb;
      while (cbb > 0 && moves <= magic) {
        if (hd - ak <= 0) {
          hd = A;
          moves++;
          hd -= ak;
        } else {
          ad += b;
          moves++;
          cbb--;
          hd -= ak;
        }
          if (hd <= 0) break;
      }
      if (hd <= 0)
        continue;
      while (moves < magic) {
        if (hd - ak <= 0 && hk - ad > 0) {
          hd = A;
          moves++;
          hd -= ak;
          if (hd <= 0) {
            moves = magic;
            break;
          }
        } else {
          hk -= ad;
          moves++;
          if (hk <= 0)
            break;
          hd -= ak;
          if (hd <= 0) {
            moves = magic;
            break;
          }
        }
      }
      if (hd > 0) {
        //if(!cb&&!cd)cerr<<cb<<' '<<cd<<' '<<moves<<endl;
        ans = min(ans, moves);
      }
    }
  }
  if (ans < 1000)
    cout << ans << endl;
  else
    cout << "IMPOSSIBLE\n";
}

int main() {
  #ifdef LOCAL
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif

  int t;
  scanf("%d", &t);
  for (int cases = 1; cases <= t; cases++) {
    printf("Case #%d: ", cases);
    //prepare();
    solve();
    cerr << cases << "done\n";
  }

  return 0;
}