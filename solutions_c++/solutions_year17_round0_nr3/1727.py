#include <bits/stdc++.h>
using namespace std;

const long long MAXN=1007; 
const long long MOD=1000000007; 
const long long INF=2147483647;
const double EPS=1e-8;

long long i,j,k,n,m,p,t,x,y,z,ans,cnt,tcase,xcase;
string s;
long long a[MAXN]; 

int main()
{
#ifdef Smile
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	while (cin>>tcase)
	{
		xcase=0;
		while (xcase<tcase)
		{
			xcase++;
			cout<<"Case #"<<xcase<<": ";
			cin>>n>>k;
			if (k==1) x=n;
			else
			{
				t=0;
				while((1LL<<t)<=k) t++;t--;
				m=(1LL<<t)-1;
				n-=m;
				// cout<<t<<" "<<m<<" "<<n<<" "<<k<<" "<<m+1<<endl;
				if (k-m<=n%(m+1))
				{
					x=n/(m+1)+1;
				}
				else
				{
					x=n/(m+1);
				}
			}
			if (x%2)
			{
				cout<<x/2<<" "<<x/2<<endl;
			}
			else
			{
				cout<<x/2<<" "<<x/2-1<<endl;
			}
		}	
	}
	return 0;
}