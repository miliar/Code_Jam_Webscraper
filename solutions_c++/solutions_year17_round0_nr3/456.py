#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> PLL;

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";
		ll n, k;
		cin >> n >> k;
		// (segment_size -> segment_count);
		map<ll, ll> segs_count;
		segs_count[n] = 1;
		while (k > 1) {
			ll seg = (segs_count.rbegin())->first;
			if (k - segs_count[seg] <= 0) break;
			k -= segs_count[seg];
			ll left_half = (seg-1LL)/2LL;
			ll right_half = seg/2LL;
			segs_count[left_half] += segs_count[seg];
			segs_count[right_half] += segs_count[seg];
			segs_count.erase(seg);
		}
		ll seg = (segs_count.rbegin())->first;
		ll left_half = (seg-1LL)/2LL;
		ll right_half = seg/2LL;
		cout << right_half << " " << left_half << '\n';
	}
}