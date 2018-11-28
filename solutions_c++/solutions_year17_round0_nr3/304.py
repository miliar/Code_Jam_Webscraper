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
    uint64 n, k;
    FOR(test, 1, numTests + 1) {
        cin >> n >> k;
        map<uint64, uint64> cnt;
        uint64 minLength, maxLength;
        uint64 curMax, curMin;
        cnt[n] = 1;
        while (true) {
            uint64 largestLen = cnt.rbegin()->first;
            uint64 largestCnt = cnt.rbegin()->second;
            curMax = largestLen / 2;
            curMin = (largestLen - 1) / 2;
            cnt.erase(largestLen);
            if (k <= largestCnt) {
                maxLength = curMax;
                minLength = curMin;
                break;
            }
            k -= largestCnt;
            if (cnt.find(curMax) == cnt.end()) {
                cnt[curMax] = 0;
            }
            if (cnt.find(curMin) == cnt.end()) {
                cnt[curMin] = 0;
            }
            cnt[curMax] = cnt[curMax] + largestCnt;
            cnt[curMin] = cnt[curMin] + largestCnt;
        }
        cout << "Case #" << test << ": " << maxLength << " " << minLength << endl;
    }

    return 0;
}
