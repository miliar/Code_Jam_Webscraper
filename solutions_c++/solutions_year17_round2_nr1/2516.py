#include <bits/stdc++.h>

using namespace std;


typedef long long			ll;
typedef vector<int > 		vi;
typedef pair<int, int > 	pii;
typedef vector<pii> 		vii;
typedef set<int > 			si;
typedef map<string, int> 	msi;
typedef pair<ll,ll> 		pll;
typedef vector<ll>			vll;

#define fast ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0)
#define f first
#define s second
#define pi 2*acos(0.0)
#define rep2(i,b,a) for(int i = (int)b, _a = (int)a; i >= _a; i--)
#define rep1(i,a,b) for(int i = (int)a, _b = (int)b; i <= _b; i++)
#define rep(i,n) for(int i = 0, _n = (int)n ; i < _n ; i++)
#define TRvi(c,it) for(vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c,it) for(vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c,it) for(msi::iterator it = (c).begin; it != (c).end(); it++
#define mp make_pair
#define pb(a) push_back(a)
#define mem(a,val) memset(a,val,sizeof(a))

const ll inf =  1e18;
const int mod = 1e9+7;
const int Lim = 1e5+1e3;
const double eps = 1e-15;

int main()
{
	int t;
	cin>>t;
	rep(xxx, t) {
		int d, n;
		cin>>d>>n;
		int dist[n], speed[n];
		double time=-inf;
		rep(i, n) {
			cin>>dist[i]>>speed[i];
			double temp=(d-(double)dist[i])/speed[i];
			// cout<<temp<<" ";
			time=max(time, temp);
		}

		cout<<fixed<<setprecision(7)<<"Case #"<<xxx+1<<": "<<d/time<<endl;
	}
	return 0;
}