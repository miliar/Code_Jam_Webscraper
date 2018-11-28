#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

ll k, n;
	
void go () {
	set <ll> s;
	map <ll,ll> m;

	s.insert(n);
	m[n] = 1;

	while (k >= 0) {
		ll at = *(s.rbegin());

		if (k > m[at])
			k -= m[at];
		else {
			cout << at/2LL << " " << (at - 1)/2LL << endl;
			return;
		}

		m[at/2LL] += m[at];
		m[(at-1)/2LL] += m[at];

		s.erase(*s.rbegin());
		s.insert(at/2LL);
		s.insert((at-1)/2LL);
	}
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n >> k;

		cout << "Case #" << t << ": ";
		go ();
	}

	return 0;
}
