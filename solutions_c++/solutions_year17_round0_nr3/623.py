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

int main(void) {
    //ios_base::sync_with_stdio(false);
    //cin.tie(nullptr);

    int T;

    scanf("%d", &T);
    for (int tn = 1; tn <= T; tn++) {
        ll N, K;
        scanf("%lld %lld", &N, &K);

        map<ll, ll> M;
        M[N] = 1;

        ll m = 1;
        while (K >= (m << 1)) {
            map<ll, ll> M2;
            for (auto& it : M) {
                M2[(it.first - 1) / 2] += it.second;
                M2[it.first / 2] += it.second;
            }
            swap(M2, M);

            m <<= 1;
        }
        ll leaf = K - m;    // 0 ~ m - 1

        ll ans = M.begin()->first;
        for (auto it = M.rbegin(); it != M.rend(); ++it) {
            if (leaf < it->second) {
                ans = it->first;
                break;
            }
            leaf -= it->second;
        }

        printf("Case #%d: %lld %lld\n", tn, ans / 2, (ans - 1) / 2);
    }

    return 0;
}
