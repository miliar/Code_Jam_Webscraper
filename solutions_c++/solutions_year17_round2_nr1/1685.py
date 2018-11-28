#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define X first
#define Y second
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define forn(n) for(ll i=0;i<n;i++)
#define forin(n1,n2) for(ll i=n1;i<n2;i++)
using namespace std;
typedef pair<int,int>pii;
FILE *ptr1=freopen("in.txt","r",stdin);
FILE *ptr2=freopen("out.txt","w",stdout);
int main()
{
// 	ios_base::sync_with_stdio(false); cin.tie(NULL);
	ll tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		double d,n;
		cin>>d>>n;
		double ans=1e15;
		forn(n)
		{
			double a,b;
			cin>>a>>b;
			double temp=(double)(d*(b))/(double)(d-a);
//			cout<<temp<<"\n";
			ans=min(ans,temp);
		}
		cout<<"Case #"<<t<<": "<<std::fixed<<std::setprecision(6)<<ans<<"\n";
	}
	return 0;
}

