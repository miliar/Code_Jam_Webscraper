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

#define MAXN        50
#define EPSILON     1e-8

int gN;
int gK;

double gU;
double gP[MAXN + 10];

int main(void) {
    //ios_base::sync_with_stdio(false);
    //cin.tie(nullptr);

    int T;

    scanf("%d", &T);
    for (int tn = 1; tn <= T; tn++) {
        scanf("%d %d", &gN, &gK);
        scanf("%lf", &gU);

        map<double, int> M;
        for (int i = 0; i < gN; i++) {
            scanf("%lf", &gP[i]);
            ++M[gP[i]];
        }

        while (gU > EPSILON) {
            auto it = M.begin();
            double p = it->first;
            int n = it->second;

            M.erase(it);
            if (M.empty()) {
                M[p + gU / n] = n;
                break;
            }

            auto it2 = M.begin();
            double diff = it2->first - it->first;
            if (diff * n < gU) {
                M.begin()->second += n;
                gU -= diff * n;
            } else {
                M[p + gU / n] = n;
                break;
            }
        }

        double p = 1.0;
        for (auto it : M) {
            p *= pow(it.first, it.second);
        }

        printf("Case #%d: %f\n", tn, p);
    }

    return 0;
}
