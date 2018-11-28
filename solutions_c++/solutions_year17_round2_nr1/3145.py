/*Till Death do us Part......... */

#include <bits/stdc++.h>
using namespace std;
#define ff first
#define re return
#define ss second
#define pb push_back
#define mpk make_pair
#define couts(a) cout<<a<<"\n"
#define fr(i,a,b) for(int i=a;i<b;++i)
#define ioS ios_base::sync_with_stdio(0)
#define coutd(a,b) cout<<a<<" "<<b<<"\n"

//============================DEBUG==========================================
#define trace(a) cout<<#a<<": "<<a<<endl
#define trace2(a,b) cout<<#a<<": "<<a<<" | " <<#b<<": "<<b<<endl;
#define trace3(a,b,c) cout<<#a<<": "<<a<<" | " <<#b<<": "<<b<<" | "<<#c<<": "<<c<<endl;
//============================================================================

typedef long long int ll;
typedef long double ld;
typedef pair<ll,ll>pi;
typedef long long int ll;
typedef vector<int> vi;

const ll MAXN=1e6+10;
const int MOD=1e9+7;
ll dist[1002],sp[1002];

int main()
{

	//freopen("test.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("aout.txt","w",stdout);
	ioS;
	int t;
	cin>>t;

	fr(x,1,t+1)
	{
		ll d,n;
		cin>>d>>n;
		ld time=0;
		ld tmax=0;

		fr(i,0,n)
		{
			cin>>dist[i]>>sp[i];
			dist[i]=d-dist[i];
			ld time=(ld)dist[i]/((ld)sp[i]);
			tmax=max(time,tmax);

		}
		ld ans=d/tmax;

		cout<<"Case #"<<x<<": ";

		cout<<fixed<<setprecision(9)<<ans<<endl;


	}

}



