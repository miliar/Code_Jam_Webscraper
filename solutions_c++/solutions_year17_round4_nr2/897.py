#include<bits/stdc++.h>
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
const int maxn=10005,maxm=605;
const double eps=1e-16;
const double pi=acos(-1.0);

typedef pair<ll,ll> pa;

int n,m,c;
int a[maxn],b[maxn];

bool v[maxn];
vector<int> ve[maxn];
int jj[maxn];

void solve()
{
    int i,j;
    scanf("%d %d %d",&n,&c,&m);
    for(i=0;i<maxn;i++) ve[i].clear();
    for(i=0;i<m;i++) scanf("%d %d",a+i,b+i),ve[a[i]-1].pb(b[i]-1);
    for(i=0;i<n;i++) sort(ve[i].begin(),ve[i].end());
    int r=0,ans=0;
    int mt=m;
    while(m>0)
    {
        int cur=0;
        memset(v,0,sizeof(v));
        for(i=0;i<n;i++)
        {
            int ct=0;
            for(j=0;j<ve[i].size();j++)
            {
                if(ve[i][j]<0) continue;
                else
                {
                    if(v[ve[i][j]]==0&&cur<=i)
                    {
                        v[ve[i][j]]=1;cur++;ve[i][j]=-1;--m;
                    }
                }
            }
        }
        if(cur>0) ++r;
    }
    for(i=0;i<n;i++)
    {
        if(r<ve[i].size()) ans+=int(ve[i].size())-r;
    }
    printf("%d %d\n",r,ans);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,j;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		printf("Case #%d: ",ca);
		solve();
		cerr<<"Case #"<<ca<<" done\n";
	}
	return 0;
}
