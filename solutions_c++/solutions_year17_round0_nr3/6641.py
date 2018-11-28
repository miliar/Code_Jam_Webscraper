#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef  vector<unsigned long long > vull;

#define pb push_back
#define mp make_pair
#define X first
#define Y second

#define rep(i,n) for(int i=0;i<(n);i++)
#define Rep(i,a,b) for(int i=(a);i<(b);i++)
#define repr(i,n) for(int i=(n-1);i>=0;i--)
#define wh(t) while(t--)
#define all(x) (x).begin(),(x).end()
#define sz(a) a.size()

#define MOD 1000000007
#define PI 3.14159265358979
#define endl '\n'

inline int sd()
{
	register char c=getchar_unlocked();
	ull n=0;
	while(c<'0'||c>'9') c=getchar_unlocked();
	for(;c>='0'&&c<='9';c=getchar_unlocked())
	n=(n<<1)+(n<<3)+(c-'0');
	return n;
}

inline void pd(ull n)
{
	char c[20];
	int i=0;
	do
	{
	c[i++]=n%10+'0';
	n/=10;
	}while(n!=0);

	i--;
	while(i>=0)
	putchar_unlocked(c[i--]);
	putchar_unlocked('\n');
}

int main()
{
	ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
		ll n,k,r,l,ans,mr,ml,foo,t,T;

		cin>>T;

		rep(t,T){

		cin>>n>>k;
		vll a(n+2);
		pair<ll,ll> p;
		std::vector<pair<ll,ll> > v;

		a[0]=1,a[n+1]=1;

		Rep(j,1,k+1){

			ll mx=INT_MIN,mxi=0;
			foo=INT_MIN;

			Rep(i,1,n+1){
	//			cout<<i<<endl;
				if(a[i]==1)
						continue;
						
				for(int t=i+1;t<=n+1;t++){
					if(a[t]==1){
						r=t-i-1;
						break;

					}
				}
				for(int t=i-1;t>=0;t--){
					if(a[t]==1){
						l=i-t-1;
						break;

					}
				}
				//cout<<l<<" "<<r<<endl;
				if(min(l,r)==mx){

					if(max(l,r)>foo){
					mx=min(l,r);
					mr=r;
					ml=l;	
					mxi=i;
					foo=max(l,r)	;
					}
				}
				else if(min(l,r)>mx){
					mx=min(l,r);
					mr=r;
					ml=l;	
					mxi=i;
					foo=max(l,r)	;
				}
				//cout<<"max "<<mx<<"  "<<mxi <<endl;
				
			}
			a[mxi]=1;
			//cout<<j<<"chooses"<<mxi<<"  "<<mx<<endl;

		}	
		cout<<"Case #"<<t+1<<": "<<max(ml,mr)<<" "<<min(ml,mr)<<endl;
}	
	return 0;

}
	