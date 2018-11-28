#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll TC, N, K;
deque<pair<ll, ll> > q;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> TC;

	for (ll tc = 1; tc <= TC; tc++) {
		cin >> N >> K;
		cout << "Case #" << tc << ": ";

		q.clear();
		q.push_back(make_pair(N, 1));
		while (K > 0) {
			auto f = q.front().first, c = q.front().second;
			if (K <= c) {
				//cout << f << " " << c << " " << K << "\n";
				cout << f/2 << " " << (f-1)/2 << "\n";
				break;
			}
			q.pop_front();
			f--;
			if (q.back().first == (f+1)/2) {
				q.back().second += c;
			}
			else {
				q.push_back(make_pair((f+1)/2, c));
			}
			if (q.back().first == f/2) {
				q.back().second += c;
			}
			else {
				q.push_back(make_pair(f/2, c));
			}

			K -= c;
		}
	}
	
	return 0;
}
