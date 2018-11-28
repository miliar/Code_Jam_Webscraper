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
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";

		int d, n;
		cin >> d >> n;

		double maxarrivaltime = -1;
		for(int i = 0; i < n; ++i) {
			double position, speed;
			cin >> position >> speed;
			double time = (d - position) / speed;
			if(maxarrivaltime < 0 || time > maxarrivaltime) maxarrivaltime = time;
		}

		double speed = d / maxarrivaltime;
		cout << setprecision(15) << speed << endl;
	}
	return 0;
}
