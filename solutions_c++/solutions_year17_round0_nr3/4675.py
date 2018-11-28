#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <map>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define ll long long

void main() {
	int t;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int testCase = 1; testCase <= t; ++testCase) {
		ll N;
		ll K;
		cin >> N >> K;
		ll max = 0;
		ll min = 0;


		ll index = 1;
		map<ll, ll> counters;
		counters[N] = 1;
		ll ans = N;
		while (index < K) {
			map<ll, ll> nextCounters;
			for (auto iter : counters) {
				ll min = ((iter.first - 1) / 2);
				ll max = min + ((iter.first - 1) % 2);
				nextCounters[min] = nextCounters[min] + iter.second;
				nextCounters[max] = nextCounters[max] + iter.second;
			}
			counters = nextCounters;
			bool found = false;
			for (auto iter = counters.rbegin(); iter != counters.rend(); iter++) {
				if (index + iter->second >= K) {
					found = true;
					ans = iter->first;
					break;
				}
				index += iter->second;
			}
			if (found) {
				break;
			}
		}

		ans = ans - 1;
		cout << "Case #" << testCase << ": " << (ans / 2) + (ans % 2) << " " << (ans / 2) << endl;

	}
}
