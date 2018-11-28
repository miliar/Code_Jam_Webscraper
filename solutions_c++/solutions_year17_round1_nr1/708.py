#include <bits/stdc++.h>
using namespace std;

char s[50][50];
bool filled[50];

int main()
{
    freopen("0.in", "r", stdin);
    freopen("0.out", "w", stdout);

    int tc, n;

    scanf("%d", &tc);
    
    for(int t = 1; t <= tc; t++)
    {
        printf("Case #%d:\n", t);

        int N, M;
        scanf("%d %d", &N, &M);

        for(int i = 0; i < N; i++)
        {
            scanf("%s", s[i]);
            filled[i] = false;
        }

        for(int i = 0; i < N; i++)
        {
            int cnt = 0;
            for(int j = 0; j < M; j++)
            {
                if(s[i][j] == '?')
                {
                    continue;
                }
                cnt++;
                for(int k = j - 1; k >= 0; k--)
                {
                    if(s[i][k] != '?') break;
                    s[i][k] = s[i][k + 1];
                }
                for(int k = j + 1; k < M; k++)
                {
                    if(s[i][k] != '?') break;
                    s[i][k] = s[i][k - 1];
                }
            }
            if(cnt)
            {
                filled[i] = true;
            }
        }

        for(int i = 0; i < N; i++)
        {
            if(filled[i])
            {
                for(int k = i - 1; k >= 0; k--)
                {
                    if(filled[k])
                    {
                        break;
                    }
                    filled[k] = true;
                    for(int j = 0; j < M; j++)
                    {
                        s[k][j] = s[i][j];
                    }
                }
                for(int k = i + 1; k < N; k++)
                {
                    if(filled[k])
                    {
                        break;
                    }
                    filled[k] = true;
                    for(int j = 0; j < M; j++)
                    {
                        s[k][j] = s[i][j];
                    }
                }
            }
        }

        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < M; j++)
            {
                printf("%c", s[i][j]);
            }printf("\n");
        }

    }



    return 0;
}
