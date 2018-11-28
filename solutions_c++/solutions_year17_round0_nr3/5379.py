#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int > pii;
typedef pair<int,pii > piii;
typedef vector<int>     VI;

/*#define sc1(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);
*/
#define sc1(x) scanf("%lld",&x);
#define sc2(x,y) scanf("%lld%lld",&x,&y);
#define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);

#define pb push_back
#define mp make_pair
#define ini(x,val) memset(x,val,sizeof(x));
#define fs first
#define sc second
#define MOD 1000000007
#define inf 1000000001
#define linf 99999999999999999ll	//long long inf
#define PI 3.1415926535897932384626
const double eps=0.000000000000001 ;

#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define PrintCont(cont) {cout<<("\n----------------\n");\
for(typeof(cont.begin()) it = cont.begin();it!=cont.end();++it) cout<<*it<<" ";cout<<("\n----------------\n");}
#define all(v) v.begin(),v.end()
string convertstring(ll n) { stringstream ss; ss << n ; return ss.str(); }

#define debug(x) cerr<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";
#define debug4(x,y,z,a) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#a<<" :: "<<a<<"\n";
#define debugarr(a,st,en) {cerr<<"\n"<<#a<<" :: ";for(int i=st;i<=en;++i)cerr<<a[i]<<" ";cerr<<"\n";}

#define LIM 100005

int main()
{
	ll t,tot;
	sc1(t);
	tot = t;
	while(t--)
	{
		ll z,z1,done = 0,n,k;
		sc2(n,k);
		map<ll,ll>mm;
		set<ll,greater<ll> > st;
		st.insert(n);
		mm[n] = 1;
		while(done<k)
		{
			ll x = *st.begin();
			st.erase(st.begin());
			ll y = mm[x];
			z = (x-1)/2;
			z1 = x - 1 - z;
			mm[z] += y;
			mm[z1] += y;
			done += y;
			st.insert(z);
			st.insert(z1);
		}
		printf("Case #%lld: %lld %lld\n",tot - t,z1,z);
	}
	return 0;
}