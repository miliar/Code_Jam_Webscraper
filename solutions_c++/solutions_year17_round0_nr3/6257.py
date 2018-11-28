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

int ma,mi;

void recur(int n,int k)
{
	if(n==1){ma=max(ma,0);mi=max(mi,0);re ;}
	if(k==0){ma=max(n/2,ma);mi=max((n-1)/2,mi); re ;}

	if(k%2==1 && n%2==1)
	{
		recur(n/2,k/2);
	}
	else if(k%2==1 && n%2==0)
	{
		recur((n-1)/2,k/2);
		recur(n/2,k/2);

	}
	else if(k%2==0 && n%2==0)
	{
		recur((n-1)/2,(k-1)/2);
		recur(n/2,k/2);
	}
	else
	{
		recur(n/2,(k-1)/2);
		recur(n/2,k/2);
	}

}

int main()
{

	//freopen("test.txt","r",stdin);
	freopen("csmall2.in","r",stdin);
	freopen("cs2out.txt","w",stdout);
	ioS;
	int t;
	cin>>t;

	fr(x,1,t+1)
	{
		ll n,k;
		cin>>n>>k;
		ma=0;mi=0;
		recur(n,k-1);

		cout<<"Case #"<<x<<": ";

		coutd(ma,mi);

	}

}



