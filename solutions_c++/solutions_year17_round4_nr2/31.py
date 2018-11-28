#define HEADER_H
//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ull          = unsigned long long;
using ll           = long long;
using ld           = long double;
using vi           = vector<ll>;
using vvi          = vector<vi>;
using vb           = vector<bool>;
using ii           = pair<ll, ll>;
constexpr bool LOG = true;
void Log() {
	if(LOG) cerr << "\n";
}
template <class T, class... S>
void Log(T t, S... s) {
	if(LOG) cerr << t << "\t", Log(s...);
} /* ============== END OF HEADER ============== */

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for(int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";

		// seats, customers, tickets sold
		int n, c, m;
		cin >> n >> c >> m;

		vi position_count(n);
		vi customer_count(c);
		for(int i = 0; i < m; ++i) {
			int pos, buyer;
			cin >> pos >> buyer;
			--pos, --buyer;
			++position_count[pos];
			++customer_count[buyer];
		}

		// every customer must make at least customer_count[i] rides
		int rides = *max_element(customer_count.begin(), customer_count.end());

		// do we have enough 'good' positions?
		int needed = 0;
		for(int i = 0; i < n; ++i) {
			needed += position_count[i];
			// we must have:
			// rides * (i+1) >= needed
			if(rides * (i + 1) < needed) {
				// rides = ceil(needed/(i+1))
				rides = (needed + i) / (i + 1);
			}
		}

		int promotions = 0;
		for(int i = 0; i < n; ++i) {
			if(position_count[i] > rides) {
				promotions += position_count[i] - rides;
			}
		}

		cout << rides << ' ' << promotions << endl;
	}

	return 0;
}
