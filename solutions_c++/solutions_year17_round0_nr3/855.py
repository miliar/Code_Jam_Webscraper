#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define ll long long int
#define ld long double
#define pb push_back
#define mkp make_pair
#define pii pair<int, int> 
#define pll pair<long long int, long long int>
#define sci(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)

set <ll> se, se1;
set <ll> :: iterator it;
map <ll, ll> mp, mp1;
ll pow_[62];

int main()
{
	ll t, tc, n, m, i, j, k, a, b, c, x, y, z;

	pow_[0] = 1ll;
	for (i = 1; i < 62; ++i) {
		pow_[i] = (pow_[i-1] << 1ll);
	}

	cin >> t;
	tc = 0;
	while (t--) {
		cout << "Case #" << ++tc << ": ";
		cin >> n >> m;
		se.insert(n);
		mp[n] = 1;
		k = m-1;
		x = 0;
		while (pow_[x+1]-1ll <= k) {
			mp1.clear();
			se1.clear();
			for (it = se.begin(); it != se.end(); ++it) {
				se1.insert(*it);
				mp1[*it] = mp[*it];
			}
			mp.clear();
			se.clear();
			for (it = se1.begin(); it != se1.end(); ++it) {
				a = *it;
				if (a&1) {
					b = a/2;
					if (b >= 0) {
						mp[b] += mp1[a]; se.insert(b);
						mp[b] += mp1[a]; se.insert(b);
					}
				} else {
					b = a/2;
					if (b >= 0) {
						mp[b] += mp1[a]; se.insert(b);
					}
					b -= 1;
					if (b >= 0) {
						mp[b] += mp1[a]; se.insert(b);	
					}
				}
			}
			x++;
		}
		c = pow_[x]-1ll;
		se1.clear();
		for (it = se.begin(); it != se.end(); ++it) {
			se1.insert(-(*it));
		}		
		se.clear();
		for (it = se1.begin(); it != se1.end(); ++it) {
			se.insert(*it);
		}
		it = se.begin();
		while (c < m && it != se.end()) {
			a = *it;
			a *= -1;
			b = mp[a];
			if (c+b < m) {
				c += b;
			} else {
				if (a&1) {
					cout << a/2 << " " << a/2 << endl;
				} else {
					cout << a/2 << " " << max(0ll, a/2-1) << endl;
				}
				break;
			}
			++it;
		}
	}

	return 0;
}
