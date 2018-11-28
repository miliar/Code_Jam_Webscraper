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
const int maxn=1000005,maxm=605;
const double eps=1e-16;
const double pi=acos(-1.0);

typedef pair<ll,ll> pa;

int a[105],q[105][105];
int id[105],cur,r;

int solve()
{
    int n,p,i,j;
    scanf("%d %d",&n,&p);
    for(i=0;i<n;i++) scanf("%d",a+i);
    for(i=0;i<n;i++) {for(j=0;j<p;j++) scanf("%d",&q[i][j]);sort(q[i],q[i]+p);}
    memset(id,0,sizeof(id));cur=1;r=0;
    while(1)
    {
        for(i=0;i<n;i++)
        {
            for(;id[i]<p;)
            {
                for(;id[i]<p&&q[i][id[i]]*10LL<cur*a[i]*9LL;id[i]++);
                if(id[i]>=p) return r;
                if(q[i][id[i]]*10LL<=cur*a[i]*11LL) break;
                else cur=max(cur+1LL,(10LL*q[i][id[i]])/(11LL*a[i]));
            }
            if(id[i]>=p) return r;
        }
        for(i=0;i<n;i++) if(q[i][id[i]]*10LL<cur*a[i]*9LL||q[i][id[i]]*10LL>cur*a[i]*11LL) break;
        if(i>=n) {++r;for(i=0;i<n;i++) id[i]++;}
    }
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,j;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		printf("Case #%d: %d\n",ca,solve());
		cerr<<"Case #"<<ca<<" done\n";
	}
	return 0;
}
