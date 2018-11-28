#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

#define LL long long

using namespace std;

inline void work()
{
    int D, N;
    scanf("%d%d", &D, &N);
    double mx = 0.0;
    for (int i = 0; i < N; ++i)
    {
        int K, S;
        scanf("%d%d", &K, &S);
        double cost = 1.0 * (D - K) / S;
        if (cost > mx) mx = cost;
    }
    printf("%.10f\n", D / mx);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        work();
    }
}
