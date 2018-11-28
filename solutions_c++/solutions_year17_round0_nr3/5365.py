#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <functional>

#define D(x) x

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
	os << "[";
	for (int i = 0; i < vec.size(); i++) {
		if (i > 0) os << ", ";
		os << vec[i];
	}
	os << "]";
	return os;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
        long long N, K;
        cin >> N >> K;

        map<long long, long long, greater<long long>> ranges;
        ranges[N] = 1;

        long long size = 0;
        while (K > 0) {
            auto it = ranges.begin();
            size = it->first;
            long long count = it->second;
            ranges.erase(it);

            K -= count;
            ranges[size/2] += count;
            ranges[(size-1)/2] += count;
        }

        long long maxSpace = size / 2, minSpace = (size-1) / 2;

        cout << "Case #" << testCase << ": " << maxSpace << " " << minSpace << endl;
    }
}
