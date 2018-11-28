#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

void find_splitting(long long n, long long k, long long& y, long long& z) {
	long long places_to_find = k;
	map<long long, long long> len2count;
	len2count.clear();
	len2count[n] = 1; // at start one range with length n

	while (places_to_find > 0) {
		// get currrent max range
		map<long long,long long>::reverse_iterator max_ranges = len2count.rbegin();
		long long max_range_size = max_ranges->first;
		long long max_range_count = max_ranges->second;

		
		long long count_to_split = min(places_to_find, max_range_count);
		places_to_find -= count_to_split;

		long long cur_left_range = (max_range_size - 1) / 2;
		long long cur_right_range = max_range_size - 1 - cur_left_range;

		if (count_to_split < max_range_count) {
			len2count[max_range_size] -= count_to_split;
		} else {
			len2count.erase(max_range_size);
			len2count[cur_left_range] += count_to_split;
			len2count[cur_right_range] += count_to_split;
		}
		y = max(cur_left_range, cur_right_range);
		z = min(cur_left_range, cur_right_range);
	}
}


int main() {
	int t;
	cin >> t;
	long long n, k;
	for (int i = 0; i < t; ++i) {
		cin >> n >> k;
		long long y, z;
		find_splitting(n, k, y, z);
		cout << "Case #" << i+1 << ": "<< y << " " << z << endl;
	}
	return 0;
}