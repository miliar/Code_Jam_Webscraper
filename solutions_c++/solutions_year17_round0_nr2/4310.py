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

const int N = 22;
LL dp[2][10][N]; // comp, last digit, len

vector<int> get_digits(LL n) {
    vector<int> d;
    FOR(i, N) {
        d.pb(n % 10);
        n /= 10;
    }
    reverse(all(d));
    return d;
}

LL get_answer(LL n) {
    memset(dp, 0, sizeof dp);

    auto d = get_digits(n);

    dp[1][0][0] = 1;
    FOR(i, N-1) {
        FOR(ld, 10) {
            for (int nd = ld; nd < 10; ++nd) {

                dp[0][nd][i+1] += dp[0][ld][i];
                if (nd < d[i+1]) dp[0][nd][i+1] += dp[1][ld][i];
                if (nd == d[i+1]) dp[1][nd][i+1] += dp[1][ld][i];

            }
        }        
    }

    LL ans = 0;
    FOR(z, 10) {
        ans += dp[0][z][N-1];
        ans += dp[1][z][N-1];
    }
    return ans;
}

void solve() {
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);

        LL n;
        scanf("%lld", &n);
        LL z = get_answer(n);
        LL l = 1, r = n;

        while(l < r) {
            LL m = (l + r) / 2;
            if (get_answer(m) < z) l = m+1;
            else r = m;
        }

        printf("%lld\n", l);
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