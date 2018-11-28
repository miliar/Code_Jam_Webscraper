#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test) {
		unsigned n, k;
		cin >> n >> k;
		
		vector<unsigned> takenIndex;
		takenIndex.reserve(n+2);
		takenIndex.push_back(0);
		takenIndex.push_back(n+1);
		
		int bestMin, bestMax;
		for (int currK = 0; currK < k; ++currK) {
			
			bestMin = -1;
			bestMax = -1;
			unsigned bestStall = -1;
			
			for (int i = 1; i < takenIndex.size(); ++i) {
				unsigned left = takenIndex[i-1];
				unsigned right = takenIndex[i];
				unsigned dist = right - left - 1;
				
				int max = dist/2;
				int min = max - ((dist%2) ? 0 : 1);
				//cout << "miedzy " << left << " a " << right << ": " << max << " " << min << " best: " << bestMax << " " << bestMin << endl;
				
				if (min > bestMin || (min == bestMin && max > bestMax)) {
					bestMin = min;
					bestMax = max;
					bestStall = (left+right)/2;
				}
				
			}
			takenIndex.push_back(bestStall);
			sort(takenIndex.begin(), takenIndex.end());
			//cout <<"K=" << currK << "zajal " << bestStall << endl;
		}
		cout << "Case #" << test << ": " << bestMax << " " << bestMin << endl;
		
	}
}
