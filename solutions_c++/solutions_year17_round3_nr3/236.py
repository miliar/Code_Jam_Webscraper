#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;

int T, cas = 1;
long double p[51];

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d", &T);
    while (cas <= T) {
        int N, K;
        long double U;
        scanf("%d %d", &N, &K);
        scanf("%Lf", &U);
        for (int i = 0; i < N; i++)
            scanf("%Lf", &p[i]);
        p[N] = 1.0L;
        long double ans = 1.0L;
        if (N == K) {
            sort(p, p + N);
            while (U > 0.0L && p[0] < 1.0L) {
                int i = 0, j = 1;
                while (j < N && p[j] == p[j - 1]) j++;
                double ins = p[j] - p[i];
                if (ins * (long double)(j - i) <= U) {
                    U -= ins * (long double)(j - i);
                    for (int k = i; k < j; k++)
                        p[k] = p[j];
                }
                else {
                    for (int k = i; k < j; k++)
                        p[k] += U/((long double)(j - i));
                    U = 0.0L;
                }
            }
            for (int i = 0; i < N; i++)
                ans *= p[i];
        }
        printf("Case #%d: %.9Lf\n", cas, ans);
        cas++;
    }
    return 0;
}