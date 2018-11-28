#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef complex<double> cplx;

#define sqr(x) ((x)*(x))
#define pb push_back
#define X first
#define Y second
#define sit(a) set<a>::iterator
#define mit(a,b) map<a,b>::iterator

const ll mod=1000000007LL;
const int inf=0x3f3f3f3f;
const int maxn=100005,maxm=1005;
const double eps=1e-10;
const double pi=acos(-1.0);

struct hun
{
	int n;
	vector<int> g[maxm];
	int from[maxm],tot;
	bool use[maxm];
	void clc(int nt)
	{
	    n=nt;
	    for(int i=0;i<n;i++)g[i].clear();
	}
	void addedge(int i,int j)
	{
	    g[i].pb(j);
	}
	bool match(int x)
	{
		for(int i=0;i<g[x].size();i++)
		{
			if(!use[g[x][i]])
			{
				use[g[x][i]]=1;
				if(from[g[x][i]]==-1||match(from[g[x][i]]))
				{
					from[g[x][i]]=x;
					return 1;
				}
			}
		}
		return 0;
	}
	int hungry()
	{
		tot=0;
		memset(from,-1,sizeof(from));
		for(int i=0;i<n;i++)
		{
			memset(use,0,sizeof(use));
			if(match(i)) ++tot;
		}
		return tot;
	}
}dat;

int cu[105][105],fi[105][105];
int n;

bool check(int x,int y,int z)
{
    int i,j;
    if(z==0)
    {
        for(i=1;i<=n;i++)
        {
            if(i!=x&&(cu[i][y]==2||cu[i][y]==3)) return 0;
            if(i!=y&&(cu[x][i]==2||cu[x][i]==3)) return 0;
        }
        return 1;
    }
    else
    {
        for(i=1;i<=n;i++)
        {
            j=x+y-i;
            if(1<=j&&j<=n&&i!=x&&(cu[i][j]==1||cu[i][j]==3)) return 0;
            j=i+y-x;
            if(1<=j&&j<=n&&i!=x&&(cu[i][j]==1||cu[i][j]==3)) return 0;
        }
        return 1;
    }
}

void solve()
{
    int m,i,j,r=0,rt=0;
    scanf("%d %d",&n,&m);
    dat.clc(n*8);memset(cu,0,sizeof(cu));memset(fi,0,sizeof(fi));
    for(i=0;i<m;i++)
    {
        char c[5];
        int x,y;
        scanf("%s %d %d",c,&x,&y);
        if(c[0]=='x') ++r,cu[x][y]=2;
        else if(c[0]=='+') ++r,cu[x][y]=1;
        else cu[x][y]=3,r+=2;
    }
    for(i=0;i<n*n;i++)
    {
        int x=i/n+1,y=i%n+1;
        if(cu[x][y]==0)
        {
            if(check(x,y,0)) dat.addedge(x,y);
            if(check(x,y,1)) dat.addedge(x+y+n,x-y+n*2);
        }
        else if(cu[x][y]==1)
        {
            if(check(x,y,0)) dat.addedge(x,y);
        }
        else if(cu[x][y]==2)
        {
            if(check(x,y,1)) dat.addedge(x+y+n,x-y+n*2);
        }
    }
    printf("%d ",dat.hungry()+r);
    //for(int i=1;i<=n;i++) cerr<<dat.from[i]<<" ";cerr<<endl;for(int i=1+n;i<=n*3-1;i++) cerr<<dat.from[i]<<" ";cerr<<endl;
    for(i=1;i<=n;i++)
    {
        int t=dat.from[i];
        if(t!=-1) rt+=(fi[t][i]==0),fi[t][i]+=2;
    }
    for(i=1+n;i<=n*3-1;i++)
    {
        int t=dat.from[i];
        //if(t!=-1) cerr<<(i+t-3*n)/2<<","<<(i+t-3*n)/2-(i-2*n)<<endl;
        if(t!=-1) rt+=(fi[(i+t-3*n)/2][(i+t-3*n)/2-(i-2*n)]==0),fi[(i+t-3*n)/2][(i+t-3*n)/2-(i-2*n)]++;
    }
    printf("%d\n",rt);
    for(int x=1;x<=n;x++)
    {
        for(int y=1;y<=n;y++)
        {
            //cerr<<x<<","<<y<<":"<<fi[x][y]<<endl;
            if(fi[x][y]&&!cu[x][y]) printf("%c %d %d\n",fi[x][y]==1?'+':(fi[x][y]==2?'x':'o'),x,y);
            if(fi[x][y]&&cu[x][y]) printf("o %d %d\n",x,y);
        }
    }
}

int main()
{
    freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        printf("Case #%d: ",ca);
        solve();
        cerr<<"case "<<ca<<" done."<<endl;
    }
    return 0;
}
