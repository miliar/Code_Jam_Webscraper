#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	fori(kase, 1, t + 1) {
		ll n, k;
		cin >> n >> k;
		map<ll, ll> segments;
		segments[n] = 1;
		while(1) {
			pair<ll, ll> largest = *prev(segments.end());
			segments.erase(prev(segments.end()));
			ll size, how_many;
			tie(size, how_many) = largest;
			if(how_many >= k) {
				cout << "Case #" << kase << ": ";
				if(size & 1) {
					cout << size / 2 << " " << size / 2 << '\n';
				}
				else {
					cout << size / 2 << " " << size / 2 - 1 << '\n';
				}
				break;
			}
			if(size & 1) {
				segments[size / 2] += how_many * 2;
			}
			else {
				segments[size / 2] += how_many;
				segments[size / 2 - 1] += how_many;
			}
			k -= how_many;
		}
	}

	return 0;
}

