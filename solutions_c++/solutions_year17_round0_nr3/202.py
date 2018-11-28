#include <map>
#include <iostream>

using namespace std;

template <typename K, typename V>
pair<K, V> last(map<K, V>& m) {
	return *(m.rbegin());
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		long long N, K;
		cin >> N >> K;
				
		map<long long, long long> intervals;
		intervals[N] = 1;
		
		pair<long long, long long> top = last(intervals);
		long long half1 = (top.first-1ll)/2ll, half2 = top.first - 1ll - (top.first-1ll)/2ll;
		while (top.second < K) {
			K -= top.second;
			intervals.erase(top.first);
			intervals[half1] += top.second;
			intervals[half2] += top.second;
			top = last(intervals);
			half1 = (top.first-1ll)/2ll, half2 = top.first - 1ll - (top.first-1ll)/2ll;
		}
		cout << "Case #" << i << ": " << half2 << " " << half1 << endl;		
	}
}