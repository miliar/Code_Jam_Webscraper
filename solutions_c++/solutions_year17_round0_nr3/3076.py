#include<bits/stdc++.h>

using namespace std;

#define ll long long int
#define pb push_back
#define f first
#define s second
#define mod 1e9+7
#define mp make_pair
#define PI 3.14159265
#define eps 0.000001

const int N = 1234567;

#define test
int main() {
	ios::sync_with_stdio(false); cin.tie(0);
#ifdef test
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
#endif
	int tt;
	cin >> tt;
	for(int ii = 1; ii <= tt; ii++) {
		cout << "Case #" << ii << ": ";
		ll n, k;
		cin >> n >> k;
		map<ll, ll, greater<ll> > m, m1;
		map<ll, ll, greater<ll> >::iterator it;
		m[n]++;
		ll level = 1;
		while(level < k) {
			k -= level;
			it = m.begin();
			m1.clear();
			while(it != m.end()) {
				m1[it->f / 2] += (m[it->f / 2] + it->s);
				m1[(it->f - 1) / 2] += (m[(it->f - 1) / 2] + it->s);
				it++;
			}
			m = m1;
			level *= 2;
		}
		it = m.begin();
		while(k > it->s) {
			k -= it->s;
			it++;
		}
		cout << it->f / 2 << " " << (it->f - 1) / 2 << endl;
	}
	return 0;
}