#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

int N, M, ok;
char a[26][26];
vector <char> clr;
int f[30];

void bck(int x, int y, char aa[26][26])
{
    if(ok)  return;
    if(x >= N)
    {
        for(int i = 0; i < N; i++)
        {
             aa[i][M] = 0;
            puts(aa[i]);
        }

        ok = 1;
        return;
    }
    int nxtx = x + (y + 1) / M;
    int nxty = (y + 1) % M;
    if(aa[x][y] != '.')
    {
        bck(nxtx, nxty, aa);
        return;
    }

    char a[26][26];


    for(auto c: clr)
    {
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                a[i][j] = aa[i][j];
        a[x][y] = c;
        int xmin, xmax, ymin, ymax;
        xmin = ymin = 1<< 30;
        xmax = ymax = -1;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                if(a[i][j] == c)
                {
                    xmin = min(xmin, i);
                    xmax = max(xmax, i);
                    ymin = min(ymin, j);
                    ymax = max(ymax, j);
                }
        int o = 1;
        for(int i = xmin; i <= xmax && o; i++)
            for(int j = ymin; j <= ymax && o; j++)
                if(a[i][j] == '.' || a[i][j] == c);
                else o = 0;
        if(o)
        {
            for(int i = xmin; i <= xmax && o; i++)
                for(int j = ymin; j <= ymax && o; j++)
                    a[i][j] = c;
            bck(nxtx, nxty, a);
        }
    }
}

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d:\n", test);
        scanf("%d%d\n", &N, &M);
        for(int i = 0; i < N; i++)
            gets(a[i]);
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                if(a[i][j] == '?')
                    a[i][j] = '.';
        memset(f, 0, sizeof(f));
        clr.clear();
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                if(a[i][j] != '.')
                    if(!f[ a[i][j] - 'A' ])
                        clr.push_back(a[i][j]), f[ a[i][j] - 'A' ] = 1;
        for(int c = 0; c < 26; c++)
        {
            int xmin, xmax, ymin, ymax;
            xmin = ymin = 1<< 30;
            xmax = ymax = -1;
            for(int i = 0; i < N; i++)
                for(int j = 0; j < M; j++)
                    if(a[i][j] == 'A' + c)
                    {
                        xmin = min(xmin, i);
                        xmax = max(xmax, i);
                        ymin = min(ymin, j);
                        ymax = max(ymax, j);
                    }
            if(xmax == -1)  continue;
            for(int i = xmin; i <= xmax; i++)
                for(int j = ymin; j <= ymax; j++)
                    a[i][j] = c + 'A';
        }
        ok = 0;
        bck(0, 0, a);
    }

    return 0;
}
