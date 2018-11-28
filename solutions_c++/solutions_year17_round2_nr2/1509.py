#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define mse(x , y) memset(x , y , sizeof(x))
#define IOS do{ ios :: sync_with_stdio(0); cin.tie(NULL); }while(0) 

typedef long long ll;
typedef pair<int , int> pii;

const int maxn = 1005;
const int INF = 0x3f3f3f3f;
const int mod = 1000000007;
const double eps = 1e-9;

int __ = 1 , kase = 0;

/************default************/

int n , a[10];
char ans[1005];

void init() {}

void read() {
	cin >> n;
	for(int i = 0; i < 6; i++) {
		cin >> a[i];
	}
}

void solve() {
	int mx = max(max(a[0] , a[2]) , a[4]);
	if(mx > n / 2) {
		printf("Case #%d: IMPOSSIBLE\n" , ++kase);
		return ;
	} else {
		vector<pair<int , char> > v;

		v.pb(mp(a[0] , 'R'));
		v.pb(mp(a[2] , 'Y'));
		v.pb(mp(a[4] , 'B'));
		sort(v.begin() , v.end() , greater<pair<int , char> >());

		memset(ans , 0 , sizeof(ans));
		for(int i = 0; v[0].F > 0; i += 2) {
			ans[i] = v[0].S;
			v[0].F--;
		}
		int ok = 1;
		for(int i = n - 1; i >= 0; i--) {
			if(v[1].F == 0 || v[2].F == 0) break;
			if(ans[i] == v[0].S) continue;
			ans[i] = ok ? v[1].S : v[2].S;
			ok ? v[1].F-- : v[2].F--;
			ok = !ok;
		}
		for(int i = 0; i < n; i++) {
			if(ans[i] == 0) {
				ans[i] = v[1].F == 0 ? v[2].S : v[1].S;
			}
		}
		printf("Case #%d: " , ++kase);
		for(int i = 0; i < n; i++) {
			cout << ans[i];
		} cout << endl;
	}
}

int main() {
	scanf("%d" , &__);
	while(__--) {
		init();
		read();
		solve();
	}
	return 0;
}