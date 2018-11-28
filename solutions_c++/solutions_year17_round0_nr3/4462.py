#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cassert>
#include <map>
#include <string>
#include <iomanip>
#include <set>
#include <queue>
#include <ctime>
#include <vector>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define sz(v) (int)(v).size()
#define mp make_pair
#define all(v) (v).begin(), (v).end()
//typedef double LD;
#define for1(i,n) for(int i = 1; i <= (int)(n); ++ i)
#define ford1(i,n) for(int i = (int)(n); i >= 1; -- i)
#define ford(i,n) for(int i = (int)(n)-1; i >= 0; -- i)
#define forn(i,n) for(int i = 0; i < (int)(n); ++ i)
typedef vector<int> vi;
typedef vector<pair<int, int> > vpi;
typedef pair<int, int> pii;
typedef long long LL;
// typedef long double LD;

map<LL, LL> M;
LL N;

LL getcnt(LL n, LL m) {
    if (n == 0) return 0;
    if (M.count(n)) return M[n];

    LL h1 = (n-1)/2;
    LL h2 = n-1 - h1;
    LL x = min(h1, h2) * N + max(h1, h2);

    LL ret = (x >= m) + getcnt(h1, m) + getcnt(h2, m);
    M[n] = ret;

    return ret;
}

void solve() {
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);

        LL n, k;
        scanf("%lld%lld", &n, &k);
        N = n;

        LL l = n * 0 + 0;
        LL r = n * (n-1) + (n-1);

        while(l < r) {
            LL m = (l + r + 1) / 2;
            M.clear();
            if (getcnt(n, m) >= k) l = m;
            else r = m-1;
        }

        printf("%lld %lld\n", l % n, l / n);
    }
}

void testgen() {
    FILE *f = fopen("input.txt", "w");
    srand(time(0));
    fclose(f);
}

int  main(int argc, char* argv[]) {
#ifdef harhro94
    //testgen();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
#define task "blackjack"
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
#endif

    solve();

#ifdef harhro94
    //cerr << "\ntime = " << clock() / 1000.0 << endl;
#endif
    return 0;
}