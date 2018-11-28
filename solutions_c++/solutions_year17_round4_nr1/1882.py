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

#define PI 3.14159265359

#define MAXN 1888

#define MAXP 888

int solve(vector<int> solution, int P) {
    int cur = 0;
    int sum = 0;
    REP(i, SIZE(solution)) {
        if (sum == 0) cur++;
        sum = (sum + solution[i]) % P;
    }
    return cur;
}

int main() {
  int numTests ;
  cin >> numTests ;
  FOR(test, 1, numTests + 1) {
    int N, P;
    cin >> N >> P;
    vector<pint> v;
    int cnt[MAXP] = {0};
    REP(i, N) {
        int G;
        cin >> G;
        cnt[G%P]++;
    }
    vector<int> solution;
    int ret = 0;
    if (P == 2) {
        REP(i, cnt[0]) solution.push_back(0);
        REP(i, cnt[1]) solution.push_back(1);
        ret = solve(solution, P);
    }
    if (P == 3) {
        REP(i, cnt[0]) solution.push_back(0);
        int dup = MIN(cnt[1], cnt[2]);
        REP(i, dup) { solution.push_back(1); solution.push_back(2); }
        cnt[1] -= dup;
        cnt[2] -= dup;
        REP(i, cnt[1]) { solution.push_back(1); }
        REP(i, cnt[2]) { solution.push_back(2); }
        ret = solve(solution, P);
    }
    if (P == 4) {
        REP(i, cnt[0]) solution.push_back(0);
        REP(i, cnt[2]/2) solution.push_back(2);
        cnt[2] %= 2;
        int dup = MIN(cnt[1], cnt[3]);
        REP(i, dup) { solution.push_back(1); solution.push_back(3); }
        cnt[1] -= dup;
        cnt[3] -= dup;
        if (cnt[2] > 0) {
            if (cnt[1] >= 2) {
                solution.push_back(2); solution.push_back(1); solution.push_back(1);
                cnt[2]--;
                cnt[1] -= 2;
            }
            if (cnt[3] >= 2) {
                solution.push_back(2); solution.push_back(3); solution.push_back(3);
                cnt[2]--;
                cnt[3] -= 2;
            }
        }
        REP(i, cnt[1]) solution.push_back(1);
        REP(i, cnt[3]) solution.push_back(3);
        ret = solve(solution, P);
    }

    cout << "Case #" << test << ": " << ret << endl;
  }

  return 0;
}
