#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

ll r[51];
vector<ll> q[51];
ll n, p;
bool ok;

int test(ll val) {
	bool les = false;
	bool more = false;

	for(int i = 0; i < n; i++) {
		if (q[i].back() * 10 < 9 * r[i] * val ) {
			les = true;
			break;
		}
	}

	for(int i = 0; i < n; i++) {
		if (q[i].back() * 10 > 11 * r[i] * val ) {
			more = true;
			break;
		}
	}
	if(more and les) return -2;
	else if (more) return 1;
	else if (les) return -1;
	else return 0;
}

int bs() {
	ll lo = 1;
	ll hi = 10000000;
	bool hasans = false;
	while(lo < hi) {
		int mid = (lo+hi)/2;
		int ret = test(mid);
		if(ret == -2) {
			lo = mid;
			break;
		}
		if(ret == -1) {
			hi = mid - 1;
		} else if (ret == 0) {
			lo = mid;
			break;
		} else {
			lo = mid + 1;		
		}
	}

	if (test(lo) == 0) {
		for(int i = 0; i < n; i++) {
			q[i].pop_back();
			if(q[i].size() == 0) ok = false;
		}
		return 1;	
	} else 	{
		int mnpos = 0;
		double mn = 1e20;
		for(int i = 0; i < n; i++) {
			if((double)(q[i].back())/r[i] < mn) {
				mn = (double)(q[i].back())/r[i];
				mnpos = i;
			}
		}
		q[mnpos].pop_back();
		if(q[mnpos].size() == 0) ok = false;
		return 0;
	}
}

int main(void) {
	ios::sync_with_stdio(false);
	int T;	
	cin >> T;
	for(int t= 1; t<=T; t++) {
		cin >> n >> p;
		for(int i = 0; i < n; i++) {
			cin >> r[i];
			q[i].clear();
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < p; j++) {
				int aux;
				cin >> aux;
				q[i].pb(aux);
			}
			sort(q[i].rbegin(), q[i].rend());
		}

		ll ans = 0;
		ok = true;
		while(ok) {
			ans += bs();
		}
		cout<< "Case #" << t << ": " << ans << endl;


	}
	return 0;
}
