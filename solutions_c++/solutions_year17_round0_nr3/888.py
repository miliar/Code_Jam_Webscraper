#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

ll n, k;

void solve (){
	map<ll,ll> q;
	q[-n] = 1;
	ll a = 0, b;

	while (k>0) {
		auto x = *q.begin();
		ll u = x.fi; 
		ll qx = x.se;
		u *= -1;
		q.erase(q.begin());
		if (qx >= k) {
			a = u/2;
			b = (u-1)/2;
			break;
		}
		k -= qx;

		ll ua = u/2;
		ll ub = (u-1)/2;
		
		q[-ua] += qx;
		q[-ub] += qx;
	}
	cout << a << " " << b << endl;
}


int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	For(tt,1,T+1) {
		cin >> n >> k;
		cout << "Case #" << tt <<": ";
		if (n == k) {
			cout << "0 0\n";
			continue;
		}
		solve();
		 continue;

		for (int x = 0; x<=n; x++) {
			int kl=(n-x)/(x+1);

			//cout << x << " " << kl << "#\n";

			if (kl < k) {

				int y = kl;
				while (x <= n && (n-x) / (x+1) == y) x++;
				--x;
				//cout << x << "##\n";
				y = x;
				//y = (n-x) / (x+1);
				//cout << y << "#\n";
				kl = (n-y) / (y+1);
				if ( (n-kl) % (kl+1) != 0) y++;
				int a = (y-1)/2;
				int b = y/2;

				//cout << kl << "----> " << n-kl << " " << kl + 1 << "##\n";

				cout << b << " " << a << endl;
				break;
			}
		}
	}

	
	
	return 0;
}
