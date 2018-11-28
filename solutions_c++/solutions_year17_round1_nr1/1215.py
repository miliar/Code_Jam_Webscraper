#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<set>
#include<bitset>
#include<map>
#include<stack>
#include<queue>
#include<vector>
#include<utility>
#define INF 0x3f3f3f3f
#define inf 2*0x3f3f3f3f
#define llinf 1000000000000000000
#define pi acos(-1)
#define mod 1000000007
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
typedef long long ll;
typedef pair<int,int>P;
int t,r,c,mm[30],dy[3]={-1,0,1},dx[3]={0,-1,0};
char m[30][30];
void dfs(int x,int y)
{
    for(int i=0;i<3;i++)
    {
        int xx=x+dx[i],yy=y+dy[i];
        if(mm[xx]==0&&xx>=0&&xx<r&&yy>=0&&yy<c&&m[xx][yy]=='?')
        {
            m[xx][yy]=m[x][y];
            dfs(xx,yy);
        }
    }
}
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("round1aalout.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        printf("Case #%d:\n",cas);
        memset(mm,0,sizeof(mm));
        map<char,int>is;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
        {
            scanf("%s",m[i]);
        }
        for(int i=0;i<r;i++)
        {
            int flag=0;
            for(int j=0;j<c;j++)
            {
                if(m[i][j]!='?')
                {
                    flag=1;
                    break;
                }
            }
            if(!flag)
            {
                mm[i]=1;
                continue;
            }
            for(int j=0;j<c;j++)
            {
                if(m[i][j]!='?'&&is[m[i][j]]==0)
                {
                    dfs(i,j);is[m[i][j]]=1;
                }
            }
        }
        for(int i=r-2;i>=0;i--)
        {
            if(mm[i]&&mm[i+1]==0)
            {
                for(int j=0;j<c;j++)
                {
                    m[i][j]=m[i+1][j];
                }
                mm[i]=0;
            }
        }
        for(int i=1;i<r;i++)
        {
            if(mm[i]&&mm[i-1]==0)
            {
                for(int j=0;j<c;j++)
                {
                    m[i][j]=m[i-1][j];
                }
                mm[i]=0;
            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cout<<m[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}
