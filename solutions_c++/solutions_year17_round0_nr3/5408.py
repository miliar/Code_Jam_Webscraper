#include <set>
#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; ++i) {
		long long N, K, max, min;
		cin >> N >> K;
		if (N == K) {
			cout << "Case #" << (i+1) << ": 0 0" << endl;
			continue;
		}
		multiset<long long> parts;
		parts.insert(N);
		for (long long j=0; j<K; ++j) {
			multiset<long long>::const_reverse_iterator max_it = parts.rbegin();
			long long max_part = *max_it;
			//cout << "max_part=" << max_part << endl;
			++max_it;
			parts.erase(max_it.base());
			if (max_part % 2 == 0) {
				min = (max_part - 1) / 2;
				max = min + 1;
			}
			else {
				min = max = max_part / 2;
			}
			//cout << "min=" << min << " max=" << max << endl;
			parts.insert(min);
			parts.insert(max);
		}
		cout << "Case #" << (i+1) << ": " << max << " " << min << endl;
	}
}