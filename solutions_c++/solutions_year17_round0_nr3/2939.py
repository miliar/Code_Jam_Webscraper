#include <iostream>
#include <string>
#include <map>

using namespace std;

typedef std::map<long long, long long>::iterator it_type;

int main() {
	if (fopen("C-large.in", "r")) {
		freopen("C-large.in", "r", stdin);
		freopen("C-large.out", "w", stdout);
	}
	long long T; cin >> T;
	// cout << T << endl;
	for (long long t = 1; t <= T; t++) {
		long long n, k; cin >> n >> k;
		// cout << n << k << endl;
		map<long long, long long> gaps;
		gaps[n] = 1;
		long long seated = 0;
		long long last_gap = -1;

		while (seated < k) {
			long long biggest_gap = -1;
			long long quantity = -1;
			for (it_type it = gaps.begin(); it != gaps.end(); it++) {
				if (it->first > biggest_gap) {
					biggest_gap = it->first;
					quantity = it->second;
				}
			}
			gaps.erase(biggest_gap);
			seated += quantity;
			gaps[biggest_gap / 2] += quantity;
			gaps[(biggest_gap - 1) / 2] += quantity;
			last_gap = biggest_gap;
		}

		cout << "Case #" << t << ": " << last_gap / 2 << " " << (last_gap - 1) / 2 << endl;
	}
	// cout << ans("980") << endl;
	// for (long long i = 1; i <= 1000; i++) {
	// 	cout << i << " " << ans(to_string(i)) << endl;
	// }
	return 0;
}

// 991 -> 989 -> 899