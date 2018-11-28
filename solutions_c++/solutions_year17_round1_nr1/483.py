#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 30;

char map[MAXN][MAXN];

int main()
{
    int testCase;
    scanf("%d", &testCase);

    for (int nowTestCase = 1; nowTestCase <= testCase; ++nowTestCase)
    {
        int N, M;
        scanf("%d%d", &N, &M);
        for (int i = 1; i <= N; ++i)
            scanf("%s", map[i] + 1);

        printf("Case #%d: \n", nowTestCase);

        for (int i = 1; i <= N; ++i)
        {
            bool flag = false;
            char last = '?';
            for (int j = 1, k = 1; j <= M; j = k + 1)
            {
                for (k = j; k <= M; ++k)
                    if (map[i][k] != '?')
                        break;

                if (k <= M)
                {
                    flag = true;
                    for (int l = j; l < k; ++l)
                        map[i][l] = map[i][k];
                    last = map[i][k];
                }
                else
                {
                    if (last != '?')
                        for (int l = j; l < k; ++l)
                            map[i][l] = last;
                }
            }

            if (flag == false)
            {
                if (i > 1 && map[i - 1][1] != '?')
                    for (int j = 1; j <= M; ++j)
                        map[i][j] = map[i - 1][j];
            }
        }

        for (int i = 1, j; i <= N; i = j + 1)
        {
            for (j = i; j <= N; ++j)
                if (map[j][1] != '?') 
                    break; for (int k = i; k < j; ++k)
                for (int l = 1; l <= M; ++l)
                    map[k][l] = map[j][l];
        }

        for (int i = 1; i <= N; ++i)
            printf("%s\n", map[i] + 1);
    }
}
