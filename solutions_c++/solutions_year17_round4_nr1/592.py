#include <bits/stdc++.h>
  
using namespace std;
  
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
  
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
 
const int INF = 1e9;
const ll MOD = 1e9 + 7;
double EPS = 1e-8;

int main(){
	int mCase;
	scanf("%d", &mCase);
	
	for(int Case = 1; Case <= mCase; Case++){
		int n, p;
		cin >> n >> p;
		vi v(p);
		rep(i, n) {
			int a;
			cin >> a;
			v[a%p]++;
		}
		int loss = 0;
		if(p == 2) {
			loss = v[1]/2;
		}
		else if(p == 3) {
			int k = min(v[1], v[2]);
			loss += k;
			v[1] -= k;
			v[2] -= k;
			int rest = v[1] + v[2];
			loss += rest - (rest + p -1) / p;
		}
		else {
			loss += v[2] / 2;
			v[2] %= 2;
			int k = min(v[1], v[3]);
			loss += k;
			int rest = v[1] + v[3] - k * 2;
			if(v[2]) loss+= 2, rest-= 2;
			loss += rest - (rest + p -1) / p; 
		}
		printf("Case #%d: %d\n", Case, n - loss);
	}
}