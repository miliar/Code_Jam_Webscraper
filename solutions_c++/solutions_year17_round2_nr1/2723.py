/* 
Name: Mohit Khare
B.Tech 2nd Year
Computer Science and Engineering
MNNIT Allahabad
*/
#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define ALL(x) x.begin(), x.end()
#define boost ios_base::sync_with_stdio(false);

#define mem(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair
#define X first
#define Y second

#define rep(i,n) for(int i=0;i<n;i++)
#define repr(i,a,b) for(int i=a;i<b;i++)
#define revr(i,a,b) for(int i=a;i>b;i--)
#define pr1(a) cout<<a<<endl;
#define pr2(a,b) cout<<a<<" "<<b<<endl;

//const int dx[4]={0,1,0,-1};
//const int dy[4]={1,0,-1,0};
#define linf 99999999999999999ll	
#define PI 3.1415926535897932384626
#define mod 1000000007
const int maxn=1e5+1;

int main()
{
	freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
	boost
	int t;
	cin>>t;
	vector<long double> v;
	rep(i,t)
	{
		ll d,n;
		cin>>d>>n;
		rep(j,n)
		{
			ll dis,sp;
			cin>>dis>>sp;
			long double p= ((long double)(d-dis))/(long double)sp;
			v.pb(p);
			//cout<<p<<endl;
		}
		sort(v.begin(),v.end(),greater<long double>());
		cout<<setprecision(6)<<fixed;
		cout<<"Case #" <<i+1<<": "<< ((long double)d/v[0])<<endl;
		v.clear();
	}
	return 0;	
}