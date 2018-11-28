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

typedef pair<pint64, pint64> pinfo;

int64 Ad, Hd, Ak, Hk, B, D;
map<pinfo, int64> cache;

int64 solve(int64 curAd, int64 curHd, int64 curAk, int64 curHk) {
    pinfo cur = pinfo(pint64(curAd, curHd), pint64(curAk, curHk));
    if (cache.find(cur) != cache.end()) return cache[cur];
    int64 &ret = cache[cur];
    ret = -1;
    if (curHd <= 0) return (ret = -1);
    if (curHk <= 0) return (ret = 0);
    if (curAd <= 0) return (ret = -1);
    if (curHk - curAd <= 0) return (ret = 1);
    int64 check = solve(curAd, curHd - curAk, curAk, curHk - curAd);
    if (check != -1 && (ret == -1 || check + 1 < ret)) ret = check + 1;
    check = solve(curAd + B, curHd - curAk, curAk, curHk);
    if (check != -1 && (ret == -1 || check + 1 < ret)) ret = check + 1;
    check = solve(curAd, Hd - curAk, curAk, curHk);
    if (check != -1 && (ret == -1 || check + 1 < ret)) ret = check + 1;
    if (curAk > 0) {
        check = solve(curAd, curHd - MAX(curAk - D, 0), MAX(curAk - D, 0), curHk);
        if (check != -1 && (ret == -1 || check + 1 < ret)) ret = check + 1;
    }

    return ret;
}

int main() {
    int numTests ;
    cin >> numTests ;

    FOR(test, 1, numTests + 1) {
        cin >>  Hd >> Ad >> Hk >> Ak >> B >> D;
        cache.clear();
        int64 ret = solve(Ad, Hd, Ak, Hk);
        if (ret != -1) cout << "Case #" << test << ": " << ret << endl;
        else cout << "Case #" << test << ": IMPOSSIBLE" << endl;
    }

    return 0;
}
