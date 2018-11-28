#include "stdafx.h"
#include <string>
#include <iostream>
#include <map>
#include <algorithm>

typedef std::map<int64_t, int64_t> Intervals;

Intervals split(const Intervals &source) {
	Intervals result;
	for (auto interval : source) {
		if (interval.first > 1) {
			auto next1 = interval.first / 2;			
			if (next1 > 0) {
				result[next1] += interval.second;
			}
			auto next2 = (interval.first - 1) / 2;
			if (next2 > 0) {
				result[next2] += interval.second;
			}
		}
	}
	return result;
}

int64_t intervalCount(const Intervals& list) {
	int64_t result = 0;
	for (auto &interval : list) {
		result += interval.second;
	}
	return result;
}

int main()
{
		int count = 0;
		std::cin >> count;

		for (auto k = 0; k < count; ++k) {
			int64_t N, K;
			std::cin >> N >> K;
			Intervals intervals;
			intervals[N] = 1;
			int64_t occupied = 0;
			while (true) {
				auto nextOccup = intervalCount(intervals);				
				if (intervals.empty() || occupied + nextOccup >= K) {
					break;
				}
				occupied += nextOccup;
				intervals = split(intervals);
			}
			if (intervals.empty()) {
				intervals[0] = 0;
			}

			int64_t longest = intervals.rbegin()->first;
			for (auto it = intervals.rbegin(); it != intervals.rend(); ++it) {
				occupied += it->second;
				if (occupied >= K) {
					longest = it->first;
					break;
				}
			}
			
			auto next1 = longest / 2;
			auto next2 = (longest - 1) / 2;
			if (next2 < 0) {
				next2 = 0;
			}

			std::cout << "Case #" << (k + 1) << ": " << next1 << " " << next2 << std::endl;
		}		
    return 0;
}

