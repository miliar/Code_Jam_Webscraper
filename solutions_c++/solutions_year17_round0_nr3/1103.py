#include <iostream>
#include <map>
using namespace std;

int main() {
	int T;
	long long n, k;

	cin >> T;

	for (int t=1 ; t<=T ; ++t) {
		cin >> n >> k;

		map <long long, long long> MAP;
		map <long long, long long> :: reverse_iterator rit;

		MAP[n]++;

		long long y, z;
		while (k > 0) {
			rit = MAP.rbegin();
			long long val = rit -> first, count = rit -> second;

			MAP.erase(val);

			MAP[val-1 >> 1] += count;
			MAP[val >> 1] += count;

			k -= count;

			if (k <= 0) {
				y = val >> 1;
				z = val - 1 >> 1;
				break;
			}
		}

		cout << "Case #" << t << ": " << y << ' ' << z << endl;
	}

	return 0;
}