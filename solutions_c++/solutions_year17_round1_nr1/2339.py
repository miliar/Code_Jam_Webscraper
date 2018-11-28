#include <bits/stdc++.h>
using namespace std;
char str[30][30];
int r, c;
struct alphabet
{
    int lx, rx, ty, dy;
} ara[30];

int left_expand(int dy, int ty, int lx, char c)
{
    if(lx==0) return lx;
    for(int i=dy; i<=ty; i++)
    {
        if(str[i][lx-1]!='?') return lx;
    }
    for(int i=dy; i<=ty; i++)
    {
        str[i][lx-1]=c;
    }
    return left_expand(dy, ty, lx-1, c);
}

int right_expand(int dy, int ty, int rx, char ch)
{
    if(rx==(c-1)) return rx;
    for(int i=dy; i<=ty; i++)
    {
        if(str[i][rx+1]!='?') return rx;
    }
    for(int i=dy; i<=ty; i++)
    {
        str[i][rx+1]=ch;
    }
    return right_expand(dy, ty, rx+1, ch);
}

int up_expand(int lx, int rx, int ty, char c)
{
    if(ty==(c-1)) return ty;
    for(int i=lx; i<=rx; i++)
    {
        if(str[ty+1][i]!='?') return ty;
    }
    for(int i=lx; i<=rx; i++)
    {
        str[ty+1][i]=c;
    }
    return up_expand(lx, rx, ty+1, c);
}

int down_expand(int lx, int rx, int dy, char c)
{
    if(dy==0) return dy;
    for(int i=lx; i<=rx; i++)
    {
        if(str[dy-1][i]!='?') return dy;
    }
    for(int i=lx; i<=rx; i++)
    {
        str[dy-1][i]=c;
    }
    return down_expand(lx, rx, dy-1, c);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cs=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d %d", &r, &c);
        assert(r>=1 && c>=1);
        for(int i=0; i<r; i++)
        {
            scanf("%s", str[i]);
        }
        for(int i=0; i<30; i++)
        {
            ara[i].dy=31;
            ara[i].ty=-1;
            ara[i].lx=31;
            ara[i].rx=-1;
        }
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                if(str[i][j]>='A' && str[i][j]<='Z')
                {
                    ara[str[i][j]-'A'].dy=min(ara[str[i][j]-'A'].dy, i);
                    ara[str[i][j]-'A'].ty=max(ara[str[i][j]-'A'].ty, i);
                    ara[str[i][j]-'A'].lx=min(ara[str[i][j]-'A'].lx, j);
                    ara[str[i][j]-'A'].rx=max(ara[str[i][j]-'A'].rx, j);
                }
            }
        }
        for(int i=0; i<26; i++)
        {
            if(ara[i].dy!=31 && ara[i].ty!=-1 && ara[i].lx!=31 && ara[i].rx!=-1)
            {
                for(int j=ara[i].dy; j<=ara[i].ty; j++)
                {
                    for(int k=ara[i].lx; k<=ara[i].rx; k++)
                    {
                        assert(str[j][k]=='?' || str[j][k]==(i+'A'));
                        str[j][k]=i+'A';
                    }
                }
            }
        }
        for(int i=0; i<26; i++) if(ara[i].lx!=31)ara[i].lx=left_expand(ara[i].dy, ara[i].ty, ara[i].lx, i+'A');
        for(int i=0; i<26; i++) if(ara[i].rx!=-1)ara[i].rx=right_expand(ara[i].dy, ara[i].ty, ara[i].rx, i+'A');
        for(int i=0; i<26; i++) if(ara[i].dy!=31)ara[i].dy=down_expand(ara[i].lx, ara[i].rx, ara[i].dy, i+'A');
        for(int i=0; i<26; i++) if(ara[i].ty!=-1)ara[i].ty=up_expand(ara[i].lx, ara[i].rx, ara[i].ty, i+'A');
        printf("Case #%d:\n", ++cs);
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                assert(str[i][j]!='?');
                printf("%c", str[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
