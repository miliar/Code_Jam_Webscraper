#include<bits/stdc++.h>
using namespace std;
int N, M;
char arr[26][26];


pair<int, char> count(int sx, int sy, int ex, int ey)
{
    int a = 0;
    char b = 0;
    for(int i=sx; i<=ex; ++i)
        for(int j=sy; j<=ey; ++j)
            if( arr[i][j] != '?' )
            {
                a++;
                b = arr[i][j];
            }
    return make_pair(a, b);
}

void logic(int sx, int sy, int ex, int ey)
{
    pair<int, char> s = count(sx, sy, ex, ey);
    if(s.first==1)
    {
        for(int i=sx; i<=ex; ++i)
            for(int j=sy; j<=ey; ++j)
                arr[i][j] = s.second;
        return;
    }
    for(int i=sx; i<ex; ++i)
    {
        if(count(i, sy, i, ey).first != 0)
        {
            if(count(i+1, sy, ex, ey).first !=0)
            {
                logic(sx, sy, i, ey);
                logic(i+1, sy, ex, ey);
                return;
            }
            break;
        }
    }
    for(int j=sy; j<ey; ++j)
    {
        if(count(sx, j, ex, j).first!=0)
        {
            if(count(sx, j+1, ex, ey).first != 0)
            {
                logic(sx, sy, ex, j);
                logic(sx, j+1, ex, ey);
                return;
            }
            break;
        }
    }
    return;
}
void solve()
{
    scanf("%d%d",&N,&M);
    for(int i=0; i<N; ++i) scanf("%s",arr[i]);
    logic(0, 0, N-1, M-1);
    for(int i=0; i<N; ++i) puts(arr[i]);
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1; i<=T; ++i)
    {
        printf("Case #%d:\n",i);
        solve();
    }  
}