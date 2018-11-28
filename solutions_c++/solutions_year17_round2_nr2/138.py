#include <bits/stdc++.h>

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-7;
int INF    = 1000000000;
LL INFLL   = 1000000000000000000LL;

#define fi            first
#define se            second
#define mp            make_pair
#define pb            push_back

#define input(in)     freopen(in,"r",stdin)
#define output(out)   freopen(out,"w",stdout)

#define MIN(a, b)     (a) = min((a), (b))
#define MAX(a, b)     (a) = max((a), (b))

#define RESET(a, b)   memset(a,b,sizeof(a))
#define ALL(a)        (a).begin(), (a).end()
#define SIZE(a)       (int)a.size()
#define SORT(a)       sort(ALL(a))
#define UNIQUE(a)     (a).erase( unique( ALL(a) ), (a).end() )
#define FOR(a, b, c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a, b, c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a, b)   for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); a++)

int mx[8] = {-1,1,0,0,-1,-1,1,1};
int my[8] = {0,0,-1,1,-1,1,-1,1};

// ----- //

int initC[3];
int C[3];
int C2[3];
string SC = "RYB";
string SC2 = "GVO";

vector<pii> getOrderedC() {
  vector<pair<int, pii>> res;
  vector<pii> res2;
  for(int i = 0; i < 3; i++) {
    res.pb(mp(C[i], mp(initC[i], i)));
  }
  sort(res.begin(), res.end());
  reverse(res.begin(), res.end());
  for(auto c: res) {
    res2.pb(mp(c.fi, c.se.se));
  }
  return res2;
}

string convC(vector<int> res) {
  string s = "";
  for(auto c: res) {
    s += SC[c];
    while(C2[c]) {
      s += SC2[c];
      s += SC[c];
      C2[c]--; 
    }
  }
  return s;
}

int main() {
  int t = 0;
  scanf("%d", &t);
  while(t--) {
    static int tc; tc++;
    printf("Case #%d: ", tc);
    int n;
    scanf("%d%d%d%d%d%d%d", &n, &C[0], &C2[2], &C[1], &C2[0], &C[2], &C2[1]);
    C[0] -= C2[0];
    C[1] -= C2[1];
    C[2] -= C2[2];
    bool fail = 0;
    for(int i = 0; i < 3; i++) {
      if (C[i] < 0) {
        fail = 1;
        break;
      }
      if (C[i] == 0 && C2[i] > 0 && 2 * C2[i] != n) {
        fail = 1;
        break;
      }
    }
    if (fail) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    initC[0] = C[0];
    initC[1] = C[1];
    initC[2] = C[2];

    vector<int> res;
    while (true) {
      vector<pii> v = getOrderedC();
      if (v[0].fi == 0) {
        break;
      }
      if (SIZE(res) > 0 && res.back() == v[0].se) {
        if (v[1].fi == 0) {
          break;
        } else {
          res.pb(v[1].se);
          C[v[1].se]--;
        }
      } else {
        res.pb(v[0].se);
        C[v[0].se]--;
      }
    }
    if (SIZE(res) == initC[0] + initC[1] + initC[2]) {
      if (SIZE(res) == 0) {
        string res = "";
        for(int i = 0; i < 3; i++) {
          while(C2[i]) {
            res += SC2[i];
            res += SC[i];
            C2[i]--;
          }
        }
        cout << res << endl;
      } else if (res[0] != res.back()) {
        cout << convC(res) << endl;
      } else {
        cout << "IMPOSSIBLE" << endl;
      }
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}