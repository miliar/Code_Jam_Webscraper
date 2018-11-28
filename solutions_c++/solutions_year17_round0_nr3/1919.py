#include<bits/stdc++.h>
using namespace std;
#define pc putchar_unlocked
#define gc getchar_unlocked
typedef long long ll;
typedef unsigned long long llu;
#define mp make_pair
#define pb push_back
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define scl(x) scanf("%lld",&x)
#define scl2(x,y) scanf("%lld%lld",&x,&y)
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define scstr(x) scanf("%s",x)
#define pd(x) printf("%d",x)
#define pstr(x) printf("%s",x)
#define newl() printf("\n")
#define fl(i,n) for (i=0;i<n;i++)
#define fle(i,n) for (i=1;i<=n;i++)
#define fla(i,a,n) for (i=a;i<n;i++)
#define mem(a,i) memset(a,i,sizeof(a))
#define fi first
#define se second
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii ;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
#define gcd __gcd
#define wl(n) while (n--)
#define debug(x) cerr<<"debug->"<<#x<<"::"<<x<<endl
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n"
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n"
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(v) v.begin(),v.end()
#define tatt(cont) typeof(cont.begin())
const double eps=0.000000000000001 ;
#define MOD 1000000007
typedef long double LF;
typedef double lF;
#define hihihaha ((double)CLOCKS_PER_SEC)
#define nl putchar('\n')
//-------------
ll n,k;
int main()
{	//ios::sync_with_stdio(0), cin.tie(0);
	int t,tst=0;
	sc(t);
	wl(t)
	{
		tst++;
		debug(tst);
		scl2(n,k);
		ll mx,mn;
		ll don=0;
		ll hav[2]={0},freq[2]={0};
		hav[n&1]=n;
		freq[n&1]=1;
		ll c=0;
		map<ll,ll>::iterator it;
		while (don+(1LL<<c)<k){

			map<ll,ll>ma;
			//s.insert(hav[0]/2);
			if (freq[0]>0&&hav[0]>0)
			{
				ma[hav[0]/2]+=freq[0];
				if (hav[0]%2==0)
				{
					ma[(hav[0]-1)/2]+=freq[0];
				}
				else
					ma[hav[0]/2]+=freq[0];
			}
			//s.insert(hav[1]/2);
			if (freq[1]>0&&hav[1]>0)
			{
				ma[hav[1]/2]+=freq[1];
				if (hav[1]%2==0)
				{
					ma[(hav[1]-1)/2]+=freq[1];
				}
				else
					ma[hav[1]/2]+=freq[1];

			}
			assert(ma.size()<=2);
			it=ma.begin();
			int lol=0;
			while (it!=ma.end())
			{
				hav[lol]=it->fi;
				freq[lol]=it->se;
				lol++;
				it++;
			}
			if (lol<2)
			{	freq[1]=0;
				hav[1]=0;
			}
			don+=(1LL<<c);
			c++;
			/*debug2(hav[0],hav[1]);
			debug2(freq[0],)*/
		}
		ll diff=k-don,ans=-1;
		if (hav[0]<hav[1])
		{
			swap(hav[0],hav[1]);
			swap(freq[0],freq[1]);
		}
		//debug(diff);
		if(freq[0]>=diff){
			ans=hav[0];
		}
		else ans=hav[1];
		assert(ans>=0);
		//cerr<<"ans is :"<<ans<<endl;
		/*debug2(hav[0],hav[1]);
		debug2(freq[0],freq[1]);*/
		
		mx=ans/2;
		if(ans%2==1)
		{
			mn=ans/2;
		}
		else mn=(ans-1)/2;
		printf("Case #%d: %lld %lld\n",tst,mx,mn);
	}		
	return 0;

}


//01010110 01101100 01100001 01100100 00101110