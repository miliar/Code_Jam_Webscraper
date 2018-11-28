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

int gD, gN;
pii gH[MAXN + 10];  // (K, S)

int main(void) {
    //ios_base::sync_with_stdio(false);
    //cin.tie(nullptr);

    int T;

    scanf("%d", &T);
    for (int tn = 1; tn <= T; tn++) {
        scanf("%d %d", &gD, &gN);
        for (int i = 0; i < gN; i++)
            scanf("%d %d", &gH[i].first, &gH[i].second);

        sort(gH, gH + gN);

        double res = 0;
        int t = 0;
        for (int i = 0; i < gN; i++) {
            double tA = double(gD - gH[i].first) / gH[i].second;

            bool last = true;
            for (int j = i + 1; j < gN; j++) {
                double tB = double(gD - gH[j].first) / gH[j].second;
                if (tA < tB) {
                    last = false;
                    break;
                }
            }

            if (last) {
                res = gD / tA;
                break;
            }
        }

        printf("Case #%d: %.9f\n", tn, res);
    }

    return 0;
}
