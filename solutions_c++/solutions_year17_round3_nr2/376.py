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

#define MAXN    100

int gNC, gNJ;
pii gPC[MAXN + 10];
pii gPJ[MAXN + 10];
vector<pair<pii, bool>> gP;

vector<int> gF[2];

int main(void) {
    //ios_base::sync_with_stdio(false);
    //cin.tie(nullptr);

    int T;

    scanf("%d", &T);
    for (int tn = 1; tn <= T; tn++) {
        gP.clear();
        gF[0].clear();
        gF[1].clear();

        int CT = 0, JT = 0;

        scanf("%d %d", &gNC, &gNJ);
        for (int i = 0; i < gNC; i++) {
            scanf("%d %d", &gPC[i].first, &gPC[i].second);
            gP.emplace_back(gPC[i], false);
            CT += gPC[i].second - gPC[i].first;
        }
        for (int i = 0; i < gNJ; i++) {
            scanf("%d %d", &gPJ[i].first, &gPJ[i].second);
            gP.emplace_back(gPJ[i], true);
            JT += gPJ[i].second - gPJ[i].first;
        }

        if (gNC + gNJ == 1) {
            printf("Case #%d: %d\n", tn, 2);
            continue;
        }

        sort(gP.begin(), gP.end());

        if (gP[0].second == gP.back().second)
            gF[gP[0].second].push_back(gP[0].first.first + 24 * 60 - gP.back().first.second);

        for (int i = 1; i < (int)gP.size(); i++) {
            if (gP[i].second == gP[i - 1].second)
                gF[gP[i].second].push_back(gP[i].first.first - gP[i - 1].first.second);
        }

        sort(gF[0].begin(), gF[0].end());
        sort(gF[1].begin(), gF[1].end());

        int ans1 = gNC;
        for (int i = 0; i < (int)gF[0].size(); i++) {
            if (CT + gF[0][i] > 720)
                break;
            CT += gF[0][i];
            ans1--;
        }
        int ans2 = gNJ;
        for (int i = 0; i < (int)gF[1].size(); i++) {
            if (JT + gF[1][i] > 720)
                break;
            JT += gF[1][i];
            ans2--;
        }

        printf("Case #%d: %d\n", tn, max(ans1, ans2) * 2);
    }

    return 0;
}
