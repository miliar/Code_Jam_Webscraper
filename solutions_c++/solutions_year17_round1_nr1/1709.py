#include <bits/stdc++.h>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define REV(i,j,k) for(int i=j;i>=k;i--)
#define FORR(i,j,k,l) for(int i=j;i<=k;i+=l)
#define inf         freopen("in.txt", "r", stdin)
#define outf        freopen("out.txt", "w", stdout)
#define pf          printf
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c)    scanf("%d %d %d", &a, &b, &c)
#define minn          (long long)-1000000000000000000
#define maxx          (long long) 1000000000000000000
#define mod          1000000007
#define LL           long long
#define NL '\n'
#define cnd tree[idx]
#define lnd (idx<<1)
#define rnd ((idx<<1)+1)
#define PB push_back
#define F first
#define S second
#define MK make_pair
#define valid(nx,ny)  ((nx >= 0) && (nx < row) && (ny >= 0) && (ny < col))
typedef pair<int,int> pr;

string str[30];
int row,col;

void up(int x, int y, char ch)
{
    str[x][y]=ch;
    if(valid(x+1,y)&&str[x+1][y]=='?') up(x+1,y,ch);
}
void down(int x, int y, char ch)
{
    str[x][y]=ch;
    if(valid(x-1,y)&&str[x-1][y]=='?') down(x-1,y,ch);
}
int chk(int i, int j, char ch, int a)
{
    if(!valid(i,j+a)) return 0;
    else if(str[i][j]==ch&&str[i][j+a]!='?') return 1;
    else return 0;
}
int main()
{
    ios::sync_with_stdio(false);
    inf;
    outf;
    int tc;
    cin>>tc;
    FOR(tt,1,tc)
    {
        int i,j,x,y,n,m,a,b,c,d;
        cin>>n>>m; row=n; col=m;
        FOR(i,0,n-1) cin>>str[i];
        FOR(i,0,n-1)
        {
            FOR(j,0,m-1)
            {
                if(str[i][j]!='?')up(i,j,str[i][j]),down(i,j,str[i][j]);
            }
        }
        FOR(i,0,n-1)
            FOR(j,0,m-2)
            {
                if(str[i][j]!='?')
                {
                    a=chk(i,j,str[i][j],1);
                    if(a==0)
                    {
                        x=i; y=j+1; c=i; d=j;
                        while(x<n&&str[x][y]=='?'&&str[c][d]==str[i][j])
                        {
                            str[x][y]=str[i][j];
                            x++; y++; c++; d++;
                        }
                    }
                }
            }
        FOR(i,0,n-1)
            REV(j,m-1,1)
            {
                if(str[i][j]!='?')
                {
                    a=chk(i,j,str[i][j],-1);
                    if(a==0)
                    {
                        x=i; y=j-1; c=i; d=j;
                        while(x<n&&str[x][y]=='?'&&str[c][d]==str[i][j])
                        {
                            str[x][y]=str[i][j];
                            x++; y++; c++; d++;
                        }
                    }
                }
            }
        cout<<"Case #"<<tt<<":\n";
        FOR(i,0,n-1) cout<<str[i]<<NL;
    }
    return 0;
}
