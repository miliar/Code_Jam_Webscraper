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
		int n, c, m;
		cin >> n >> c >> m;
		vi p(m), b(m);
		rep(i, m) {
			cin >> p[i] >> b[i];
			p[i]--;
			b[i]--;
		}

		vector<vi> seet(n);
		vector<vi> cstmr(c);
		rep(i, m) {
			seet[p[i]].pb(b[i]);
			cstmr[b[i]].pb(p[i]);
		}
		int day = 0, change = 0;
		int sum = 0;
		rep(i, n) {
			sum += seet[i].size();
			//day = max(day, (sum + i) / (i+1));
			if(day < (sum + i) / (i+1)) {
				int tmp = 0;
				day = (sum + i) / (i+1);
				rep(j, i+1) tmp += max(0, (int)seet[j].size()-day);
				change = tmp;
			}else change += max(0, (int)seet[i].size()-day);
		}
		rep(i, c) {
			//day = max(day, (int)cstmr[i].size());
			if(day < cstmr[i].size()) {
				day = cstmr[i].size();
				int tmp = 0;
				rep(j, n) tmp += max(0, (int)seet[j].size()-day);
				change = tmp;
			}
		}


		
		
		printf("Case #%d: %d %d\n", Case, day, change);
	}
}