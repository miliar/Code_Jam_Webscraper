#include <memory.h>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cstring>
#include <climits>
#include <cmath>
#include <vector>
#include <string>
#include <memory>
#include <functional>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

#define PROFILE_START(i)    clock_t start##i = clock()
#define PROFILE_STOP(i)     fprintf(stderr, "elapsed time (" #i ") = %f\n", double(clock() - start##i) / CLOCKS_PER_SEC)

#define rep(i,n)        for (int i = 0; i < n; i++)
#define REP(i,s,e)      for (int i = s; i <= e; i++)
#define repr(i,n)       for (int i = n - 1; i >= 0; i--)
#define REPR(i,s,e)     for (int i = e; i >= s; i--)

#ifndef M_PI
#define M_PI       3.14159265358979323846   // pi
#define M_1_PI     0.318309886183790671538  // 1/pi
#define M_SQRT2    1.41421356237309504880   // sqrt(2)
#endif

typedef long long           ll;
typedef unsigned long long  ull;

typedef vector<int>     vi;
typedef pair<int, int>  pii;
typedef pair<ll, ll>    pll;
#define fi              first
#define se              second
#define pb              push_back
#define eb              emplace_back
#define em              emplace
#define mp              make_pair

#define MAXN    1000

int gN, gK;
pair<int, int> gRH[MAXN + 10];

ll gDP[MAXN + 10][MAXN + 10];

int main(void) {
    //ios_base::sync_with_stdio(false);
    //cin.tie(nullptr);

    int T;

    scanf("%d", &T);
    for (int tn = 1; tn <= T; tn++) {
        scanf("%d %d", &gN, &gK);
        for (int i = 0; i < gN; i++)
            scanf("%d %d", &gRH[i].first, &gRH[i].second);
        sort(gRH, gRH + gN, [](const pair<int,int>& l, const pair<int, int>& r) {
            return l.first == r.first ? l.second > r.second : l.first > r.first;
        });

        ll ans = 0;
        for (int k = 0; k <= gN - gK; k++) {
            memset(gDP, 0, sizeof(gDP));

            ll base = ll(gRH[k].first) * gRH[k].first + 2ll * gRH[k].first * gRH[k].second;
            for (int i = k + 1; i < gN; i++) {
                ll area = 2ll * gRH[i].first * gRH[i].second;
                for (int j = 1; j < gK; j++) {
                    gDP[i + 1][j] = max(gDP[i][j], gDP[i][j - 1] + area);
                }
            }
            ans = max(ans, gDP[gN][gK - 1] + base);
        }

        printf("Case #%d: %.9f\n", tn, ans * M_PI);
    }

    return 0;
}
