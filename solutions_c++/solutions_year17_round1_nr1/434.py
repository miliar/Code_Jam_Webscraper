#include <bits/stdc++.h>

using namespace std;

int R, C;
char G[100][100];

bool f(int r)
{
    for(int i=0; i<C; i++)
        if(G[r][i]!='?')
            return true;
    return false;
}

void _main(int TEST)
{
    scanf("%d%d", &R, &C);
    for(int i=0; i<R; i++)
        scanf("%s", G[i]);
    for(int i=0, j; i<R; i=j+1)
    {
        for(j=i; j<R && !f(j); j++);
        if(j==R)
            break;
        int last=0;
        char c='0';
        for(int k=0; k<C; k++) if(G[j][k]!='?')
        {
            c=G[j][k];
            for(int x=i; x<=j; x++)
                for(int y=last; y<=k; y++)
                    G[x][y]=c;
            last=k+1;
        }
        for(int x=i; x<=j; x++)
            for(int y=last; y<C; y++)
                G[x][y]=c;
    }
    for(int i=1; i<R; i++)
        for(int j=0; j<C; j++)
            if(G[i][j]=='?')
                G[i][j]=G[i-1][j];
    for(int i=0; i<R; i++)
        printf("%s\n", G[i]);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        //cerr << i << endl;
        printf("Case #%d:\n", i);
        _main(i);
    }
    return 0;
}
