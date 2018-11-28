#include<bits/stdc++.h>
using namespace std;
//      std macros
typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll> > vpll;
typedef vector<pair<int,int> > vpii;
typedef pair<int ,int> pii;
typedef pair<ll ,ll> pll;
//      dereference
#define F first
#define S second
#define pb push_back
#define mp make_pair
//      loops
#define rep(i,n) for(int i=0;i<n;++i)
#define REP(i,a,b) for(int i=a;i<=b;++i)
#define PER(i,b,a) for(int i=b;i>=a;--i)
#define all(X) (X).begin(), (X).end()
//      I/O
#define sd(n) scanf("%d",&n)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sd3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define sll(n) scanf("%lld",&n)
#define sll2(x,y) scanf("%lld%lld",&x,&y)
#define sll3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define sc(n) scanf("%c",&n)
#define ss(n) scanf("%s",n)
#define oll(n) printf("%lld\n",n)
//      debug
#define debug(x) cerr<<"debug->"<<#x<<"::"<<x<<endl
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n"
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n"
#define debug4(x,y,z,w) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#w<<" :: "<<w<<"\n"
//      set values
#define mset(n,k) memset(n,k,sizeof(n))
#define MOD 1000000007
ll INV2=500000004;
ll INV6=166666668;
//modular expo
ll power(ll a,ll b, ll c){
    ll x=1,y=a;
    while(b>0){
        if(b&1)
            x=(x*y)%c;
        y=(y*y)%c;
        b/=2;
    }
    return x%c;
}
//perfect numbers till 10^6 6, 28, 496, 8128
int dx[]={0,-1,0,1};
int dy[]={-1,0,1,0};//clockwise from left
int dr[]={1,1,0,-1,-1,-1, 0, 1};
int dc[]={0,1,1, 1, 0,-1,-1,-1};//anticlockwise from down
ll r[55],q[55][55];
vector<ll>v[50],ki[1000005][3];
int main()
{

	int t;
	sd(t);
	REP(l,1,t)
	{
		int ans=0;
		int n,p;
		sd2(n,p);
		REP(i,1,n)
		{
			sll(r[i]);
		}
		ll mx=0;
		REP(i,0,3)
			v[i].clear();
		REP(i,1,1000000){
			rep(j,3)
			ki[i][j].clear();
		}
		REP(i,1,n)
		{
			REP(j,1,p)
			{
				sll(q[i][j]);
				v[i].pb(q[i][j]);
			}
		}
		sort(all(v[1]));
		int vl=0;
		REP(i,1,n)
		{
			REP(j,1,p)
			{
				bool fl=0;
				REP(k,1,1000000)
				{
					ll mn=ceil(k*r[i]*0.9),mx=floor(k*r[i]*1.1);
					if(mn>q[i][j])
						break;
					if(q[i][j]>=mn && q[i][j]<=mx)
					{
						//debug2(q[i][j],k);
						ki[q[i][j]][i].pb(k),fl=1;
					}
				}
				if(fl)
					vl++;
			}
		}
		if(n==1)
		{
			printf("Case #%d: %d\n",l,vl);
			continue;
		}
		do
		{
			int cnt=0;
			REP(i,1,p)
			{
				ll fi=v[1][i-1],se=v[2][i-1],fl=0;
				//debug2(fi,se);
				for(int j=0;j<ki[fi][1].size();++j)
				{
					auto it=lower_bound(all(ki[se][2]),ki[fi][1][j]);
					if(it!=ki[se][2].end())
					{
						if((*it)==ki[fi][1][j])
						{
							fl=1;
							break;
						}
					}
				}
				if(fl)
					cnt++;
			}
			ans=max(ans,cnt);
		}while(next_permutation(all(v[1])));

		printf("Case #%d: %d\n",l,ans);
	}

            


return 0;
}