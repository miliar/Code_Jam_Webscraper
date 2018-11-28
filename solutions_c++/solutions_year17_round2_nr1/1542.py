#include <bits/stdc++.h>
#define isNum(c) c<='9' && c>='0'
#define islettre(c) c<='z' && c>='a'
#define isLETTRE(c) c<='Z' && c>='A'
#define MS0(x) memset(x,0,sizeof(x))
#define MS(x,s) memset(x,s,sizeof(x))
#define rep(i,n) for(i=0;i<n;i++)
#define rev(i,n) for(i=n;i>=0;i--)
#define repv(i,v) for(i=0;i<v.size();i++)
#define repa(i,a,n) for(i=a;i<n;i++)
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define NOT_VISITED 0
#define IS_VISITED 1
#define MOD 1000000009
#define INF 1000000009
#define COL 100002
#define trMap(c,i) for(map<char,int>::iterator i = (c).begin(); i != (c).end(); i++)
#define trSet(c,i) for(set< pair <int,char> >::iterator i = (c).begin(); i != (c).end(); i++)
#define PB(val) push_back(val)
#define MP(f,s) make_pair(f,s)
#define abs(i) (i<0)?-i:i
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;
const double EPS = 1e-7;
vector< pair<ll, ll> > v;
long long D;

double can(){
	double tmax = 0;
	for( auto p : v ){
		double t =  ((double) (D-p.first)) / p.second;
		tmax = max(t,tmax);
	}
	return tmax;
}

void solve(int t){
	printf("Case #%d: ",t);
	int N;
	cin >> D >> N;
	v = vector<pair<long long, long long> >(N);
	for(int i = 0; i < N; i++) cin >> v[i].first >> v[i].second;
	printf("%.6f\n",D/can());
}

int main(){
	int T;
	cin >> T;
	int i = 1;
	while(T--) solve(i++);
}
