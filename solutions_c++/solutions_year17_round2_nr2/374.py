#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int,char> PIC;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

#define MOD 1000000007
#define INF 2000000000

int GLL(LL& x) {
    return scanf("%lld", &x);
}

int GI(int& x) {
    return scanf("%d", &x);
}

const int MAXN = 1005;
char res[MAXN];

int T;

int n, r, o, y, g, b, v;

int next(int p) {
    p += 2;

    if (n % 2 == 1) {
        p = (p % n);
    }
    else {
        if (p == n) {
            p = 1;
        }
    }

    return p;
}

void solve() {
    cin >> n >> r >> o >> y >> g >> b >> v;

    vector<PIC> cnt;

    cnt.PB(MP(r, 'R'));
    cnt.PB(MP(y, 'Y'));
    cnt.PB(MP(b, 'B'));

    sort(cnt.rbegin(), cnt.rend());

    if (r > n / 2 || y > n / 2 || b > n / 2) {
        printf("IMPOSSIBLE\n");
    }
    else {
        int pos = 0;

        FORN(i, 3) {
            FORN(j, cnt[i].FF) {
                res[pos] = cnt[i].SS;
                pos = next(pos);
            }
        }

        FORN(i, n) {
            cout << res[i];
        }
        cout << "\n";
    }
}

int main() {
    GI(T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}
