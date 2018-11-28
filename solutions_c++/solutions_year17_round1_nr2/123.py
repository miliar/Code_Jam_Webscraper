#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <iomanip>

using namespace std;

typedef long long int64 ;
typedef unsigned long long uint64 ;
typedef pair<int, int> pint ;
typedef pair<int64, int64> pint64 ;
typedef vector<int> vint ;

#define px first
#define py second

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define REPD(i, n) for (int i = (n) ; i >= 0 ; i --)
#define FOR(i, a, b) for (int i = (a) ; i < (b) ; i ++)
#define FORD(i, a, b) for (int i = (a) ; i >= (b) ; i --)

#define MUL64(x, y) (((int64) (x)) * ((int64) (y)))
#define MULMOD(x, y, modul) (MUL64(x, y) % modul)
#define MUL(x, y) MULMOD(x, y, modul)
#define ADD(reg, val) { reg += val ; if (reg >= modul) reg -= modul ; }

#define SET(v, val) memset(v, val, sizeof(v)) ;
#define SIZE(v) ((int) (v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) { sort(ALL(v)) ; }
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }

#define EPS 1e-9
#define FLOOR(x) ((int64)((x) + EPS))
#define CEIL(x) ((int64)((x) + 1 - EPS))

#define MAXN 888


int n, np;
double R[MAXN], Q[MAXN][MAXN];

int main() {
  int numTests ;
  cin >> numTests ;
  FOR(test, 1, numTests + 1) {
    priority_queue<pint64> pq[MAXN], active[MAXN];
    vector<int64> x;
    cin >> n >> np;
    REP(i, n) cin >> R[i];
    REP(i, n) {
        REP(j, np) {
            cin >> Q[i][j];
            int64 low = CEIL(Q[i][j]/(1.1*R[i]));
            int64 high = FLOOR(Q[i][j]/(0.9*R[i]));
            if (low > high) continue;
            pq[i].push(pint64(-low, -high));
            x.push_back(low);
            x.push_back(high);
        }
    }
    RUNIQUE(x);
    int ret = 0;
    REP(ix, SIZE(x)) {
        int64 curx = x[ix];
        REP(i, n) {
            while (SIZE(pq[i]) > 0) {
                pint64 topi = pq[i].top();
                if (-topi.first <= curx) {
                    active[i].push(pint64(topi.second, topi.first));
                    pq[i].pop();
                } else break;
            }
            while (SIZE(active[i]) > 0) {
                pint64 topi = active[i].top();
                if (-topi.first < curx) active[i].pop();
                else break;
            }
        }
        bool can = true;
        while (can) {
            REP(i, n) {
                if (SIZE(active[i]) == 0 || -active[i].top().second > curx) {
                    can = false;
                    break;
                }
            }
            if (can) {
                REP(i, n) active[i].pop();
                ret++;
            }
        }
    }
    cout << "Case #" << test << ": " << ret << endl;
  }

  return 0;
}
