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
    int N, R, O, Y, G, B, V;
    scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
    if (R * 2 > N || Y * 2 > N || B * 2 > N)
    {
        printf("IMPOSSIBLE\n");
        return;
    }
    
    pair<int, char> hh[3];
    hh[0] = make_pair(R, 'R');
    hh[1] = make_pair(Y, 'Y');
    hh[2] = make_pair(B, 'B');
    sort(hh, hh + 3);
    swap(hh[0], hh[2]);
    
    char ans[N];
    int N0 = N;
    for (int i = 0; N0; i += 2, --N0)
    {
        if (i >= N) i = 1;
        if (hh[0].first) --hh[0].first, ans[i] = hh[0].second;
        else if (hh[1].first) --hh[1].first, ans[i] = hh[1].second;
        else --hh[2].first, ans[i] = hh[2].second;
    }
    for (int i = 0; i < N; ++i) printf("%c", ans[i]);
    printf("\n");
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
