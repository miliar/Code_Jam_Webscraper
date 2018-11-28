#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Interval {
	public:
		Interval(unsigned long long t_count, unsigned long long t_length) {
			count = t_count;
			length = t_length;
		};

		unsigned long long count;
		unsigned long long length;
};

int main() {
	unsigned cases;
	cin >> cases;

	unsigned long long one = 1;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
		unsigned long long n, k, lastMax = 0, lastMin = 0;
		cin >> n >> k;

		vector<Interval> intervals;
		intervals.reserve(3);
		intervals.push_back(Interval(1, n));


		while (k > 0) {
			unsigned long long length = intervals[0].length;
			unsigned long long times = std::min(k, intervals[0].count);
			k -= times;
			intervals[0].count -= times;
			if (intervals[0].count == 0)
				intervals.erase(intervals.begin());

			if ((length & one) == one) {
				lastMax = lastMin = length / 2;
			} else {
				lastMax = length / 2;
				lastMin = lastMax - 1;
			}

			bool flagMax = false;
			size_t indexMax = 0;
			for (; indexMax < intervals.size(); ++indexMax) {
				if (lastMax == intervals[indexMax].length) {
					flagMax = true;
					intervals[indexMax].count += times;
					break;
				} else if (lastMax > intervals[indexMax].length) {
					break;
				}
			}
			if (!flagMax)
				intervals.insert(intervals.begin() + indexMax, Interval(times, lastMax));
			
			bool flagMin = false;
			size_t indexMin = 0;
			for (; indexMin < intervals.size(); ++indexMin) {
				if (lastMin == intervals[indexMin].length) {
					flagMin = true;
					intervals[indexMin].count += times;
					break;
				} else if (lastMin > intervals[indexMin].length) {
					break;
				}
			}
			if (!flagMin)
				intervals.insert(intervals.begin() + indexMin, Interval(times, lastMin));
		}
		


		printf("Case #%u: %llu %llu\n", caseIndex, lastMax, lastMin);
	}
}

