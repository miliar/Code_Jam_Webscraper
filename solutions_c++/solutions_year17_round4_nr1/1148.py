#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 100 + 10;
int G[MAXN], P; 

//struct rec
//{
    //int a, b, c;
    //rec() {}
    //rec (int _a, int _b, int _c)
    //{
        //a = _a;
        //b = _b;
        //c = _c;
    //}
//};
//
//vector <rec> plans[5];
int f[MAXN][MAXN][MAXN];

int dfs(int a, int b, int c)
{
    if (f[a][b][c] != -1)
        return f[a][b][c];

    if (a != 0 || b != 0 || c != 0)
        f[a][b][c] = 1;
    else
        f[a][b][c] = 0;

    for (int i = 0; i <= min(a, 10); ++i)
        for (int j = 0; j <= min(b, 10); ++j)
            for (int k = 0; k <= min(c, 10); ++k)
            {
                int sum = i + 2 * j + 3 * k;
                if (sum != 0 && sum % P == 0)
                {
                    f[a][b][c] = max(f[a][b][c], dfs(a - i, b - j, c - k) + 1);
                }
            }

    return f[a][b][c];
}

int main()
{
    int testCase;
    scanf("%d", &testCase);
    
    for (int nowTestCase = 1; nowTestCase <= testCase; ++nowTestCase)
    {
        int N;
        scanf("%d%d", &N, &P);
        for (int i = 1; i <= N; ++i)
            scanf("%d", &G[i]);

        int cnt[4];
        cnt[0] = 0;
        cnt[1] = 0;
        cnt[2] = 0;
        cnt[3] = 0;

        for (int i = 1; i <= N; ++i)
            ++cnt[G[i] % P];

        memset(f, -1, sizeof(f));

        printf("Case #%d: %d\n", nowTestCase, cnt[0] + dfs(cnt[1], cnt[2], cnt[3]));
    }
    return 0;
}
