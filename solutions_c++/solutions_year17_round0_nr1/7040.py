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
		string array;
		cin>>array;
		int n=array.size();
		int arr[n];
		rep(i, n) {
			if(array[i] == '+')	arr[i] = 1;
			else				arr[i] = 0;
		}
		int k, ans=0;
		cin>>k;
		rep(i, n-k+1) {
			if(!arr[i]) {
			// cout<<i<<" ";
				ans++;
				rep(j, k) {
					arr[i+j] = (arr[i+j]+1)%2;
				}
			}
		}

		int flag = 0;
		rep(i, n) {
			if(!arr[i]) {
				flag=1;
				break;
			}
		}

		if(flag)	cout<<"Case #"<<xxx+1<<": "<<"IMPOSSIBLE"<<endl;
		else		cout<<"Case #"<<xxx+1<<": "<<ans<<endl;
	}
	return 0;
}