#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
char cake[30][30];
int r,c;
void solve(int x,int y)
{
    char c=cake[x][y];
    cake[x][y]='?';
    int id1,id2,id3,id4;
    int ma=0;
    for(int i=0;i<=x;++i)
    for(int j=0;j<=y;++j)
    for(int ii=x;ii<r;++ii)
    for(int jj=y;jj<c;++jj)
    {
        int cnt=0;
        for(int m=i;m<=ii;++m)
        for(int n=j;n<=jj;++n)
        if(cake[m][n]=='?')
            cnt++;
        if(cnt==(ii-i+1)*(jj-j+1))
        {
            if(ma<cnt)
            {
                ma=cnt;
                id1=i;
                id2=j;
                id3=ii;
                id4=jj;
            }
        }
    }
    for(int i=id1;i<=id3;++i)
        for(int j=id2;j<=id4;++j)
            cake[i][j]=c;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&r,&c);
        vector<pair<int,int>>alpha;
        for(int i=0;i<r;++i)
        {
            scanf("%s",cake[i]);
            for(int j=0;j<c;++j)
                if(cake[i][j]!='?')
                alpha.push_back(make_pair(i,j));
        }
        for(int i=0;i<alpha.size();++i){
            solve(alpha[i].first,alpha[i].second);
        }
        printf("Case #%d:\n",++ca);
        for(int i=0;i<r;++i)
            puts(cake[i]);
    }
}
