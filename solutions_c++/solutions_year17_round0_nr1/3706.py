#include<bits/stdc++.h>
using namespace std;
//      std macros
typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll> > vpll;
typedef vector<pair<int,int> > vpii;
typedef pair<int ,int> pii;
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
char s[1005];
int main()
{
	int t,k;
	sd(t);
	REP(l,1,t)
	{
		ss(s),sd(k);
		int len=strlen(s),ans=0;
		for(int i=0;i<len;++i)
		{
			if(s[i]=='-')
			{
				ans++;
				for(int j=i;j<(i+k) && (i+k-1)<len;++j)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		bool fl=0;
		for(int i=0;i<len;++i)
		{
			if(s[i]=='-')
			{
				fl=1;
				break;
			}
		}
		if(fl)
		{
			printf("Case #%d: IMPOSSIBLE\n",l);
		}
		else
		{
			printf("Case #%d: %d\n",l,ans);
		}
	}


return 0;
}