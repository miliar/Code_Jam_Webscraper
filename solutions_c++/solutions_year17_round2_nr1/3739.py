#include<bits/stdc++.h>
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define mp make_pair
#define ord(v) sort(all(v))
using namespace::std;

const double PI = acos(-1);

typedef long long ll;
typedef pair<ll,ll> pll;
typedef pair<ll,pll> tll;
typedef pair<int,int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<string> vs;
typedef vector<pll> vpll;

int t,d,n;
vector<pll> v;
double ans;

bool can(double x){
	double tempo = d/x;
	double posact = d;
	for(int i = 0; i < n; ++i)
		posact = min(posact, v[i].first + tempo*v[i].second);
	return abs(posact - d) < 1e-9; 
}

bool f(ii a, ii b){
	return a.first < b.first;
}

int main(){
	ll k, s;
	scanf("%d",&t);
	for(int caso=1; caso<=t; caso++){
		v.clear();
		cin >> d >> n;
		for(int i=0; i<n; i++){
			cin >> k >> s;
			v.pb(mp(k,s));
		}
		sort(all(v),f);
		double lo = 0.000001, hi = 500000000000000.0;
		for(int i = 1; i <= 250; ++i){
			double mi = lo + (hi-lo)/2.0;
			if(can(mi)) lo = mi;
			else hi = mi;
		}
		ans = lo;
		printf("Case #%d: %.7f\n",caso,ans);
	}
	return 0;
}
