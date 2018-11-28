#include <bits/stdc++.h>
#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define mp make_pair
#define f first
#define s second
#define pb push_back
#define pf push_front
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef pair<ll,ll> LL;

const ll INF = 1e9;
const double EPS = 1e-9;
const ll MOD = 1e9 + 7;

ll t,n,c = 1;
vector<ll> v;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);cin.tie(0);
	cin >> t;
	while(t--){
		ll res = 0;
		v.clear();
		cin >> n;
		while(n != 0){
			v.pb(n%10);
			n /= 10;
		}
		reverse(v.begin(),v.end());
		n = v.size();
		bool bisa = 0;
		for(int i = n - 1;i >= 0;i--){
			ll mins = 10;
			FOR(j,i,n - 1)mins = min(mins,v[j]);
			if (mins != v[i]){
				v[i] -= 1;
				FOR(j,i + 1,n - 1)v[j] = 9;
			}
		}
		REP(i,v.size())res = 10 * res + v[i];
		cout << "Case #" << c++ << ": " << res << '\n';
	}
}
