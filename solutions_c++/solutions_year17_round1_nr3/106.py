#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 100005

int H,A,HK,AK,B,D;
int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    cin >> H >> A >> HK >> AK >> B >> D;
    int ans = INF;
    REP(d,0,101) {
      REP(b,0,101) {
        int hp = H, a = A, hk = HK, ak = AK;
        int cntd = 0, cntb = 0;
        REP(t,1,301) {
          if (a >= hk) {
            ans = min(ans, t);
            break;
          }
          if (hp - ak <= 0 && (cntd == d || (cntd < d && hp - max(ak - D, 0) <= 0))) hp = H;
          else {
            if (cntd < d) {
              ak -= D;
              ak = max(0, ak);
              cntd++;
            } else if (cntb < b) {
              a += B;
              cntb++;
            } else {
              hk -= a;
            }
          }
          hp -= ak;
          if (hp <= 0) break;
        }
      }
    }
    if (ans == INF) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
  return 0;
}
