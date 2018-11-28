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
//typedef long long LL;
typedef long double LD;

const int N = 1007;
char st[N];

void solve() {
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);

        scanf("%s", st);
        int k;
        scanf("%d", &k);
        int n = strlen(st);

        int ans = 0;
        bool bad = false;

        for (int i = 0; i + k - 1 < n; ++i) {
            if (st[i] == '-') {
                FOR(j, k) {
                    st[i+j] = (int)'+' + '-' - st[i+j];
                }
                ++ans;
            }
        }

        FOR(i, n) {
            if (st[i] == '-') {
                bad = true;
                break;
            }
        }

        if (bad) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
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