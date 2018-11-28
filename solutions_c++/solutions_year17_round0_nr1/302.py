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


int main() {
  int numTests ;
  cin >> numTests ;
  int n, k;
  string s;
  FOR(test, 1, numTests + 1) {
    cin >> s >> k;
    int ret = -1;
    string t = s;
    REP(i, 1) {
        s = t;
        char check = (i == 0) ? '+' : '-';
        int cur = 0;
        REP(j, SIZE(s)) {
            if (s[j] != check) {
                cur++;
                if (j + k > SIZE(s)) {
                    cur = -1;
                    break;
                }
                FOR(i, j, j + k) {
                    s[i] = (s[i] == '+') ? '-' : '+';
                }
            }
        }
        if (cur != -1 && (ret == -1 || ret > cur)) {
            ret = cur;
        }
    }
    if (ret == -1) {
        cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
    } else {
        cout << "Case #" << test << ": " << ret << endl;
    }
  }

  return 0;
}
