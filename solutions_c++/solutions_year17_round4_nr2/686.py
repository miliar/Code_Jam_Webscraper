#include<iostream>
#include<vector>
#include <cmath>
#include<algorithm>
#include <map>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;

const int max_n = 2005;

int T, N, C, M;
int key1[max_n], key2[max_n];


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        scanf("%d%d%d", &N, &C, &M);

        memset(key1, 0, sizeof(key1));
        memset(key2, 0, sizeof(key2));
        for (int i = 0; i < M; i++)
        {
            int p, b;
            scanf("%d%d", &p, &b);
            key1[p] ++;
            key2[b] ++;
        }

        int aa = 0, bb = 0;

        for (int i = 1; i <= C; i++)
            aa = max(aa, key2[i]);

        int tmp = 0;
        for (int i = 1; i <= N; i++)
        {
            tmp += key1[i];
            aa = max(aa, (tmp + i - 1) / i);
        }

        for (int i = 1; i <= N; i++)
        {
            bb += max(0, key1[i] - aa);
        }

        printf("Case #%d: %d %d\n", t, aa, bb);
    }
    return 0;
}
