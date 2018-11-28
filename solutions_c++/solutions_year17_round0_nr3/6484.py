#include <iostream>
#include <cstdio>
#include <string>
#include <queue>

using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		int maxLR = 0, minLR = 0;
		
		priority_queue<int> intervals;
		int N, K;

		cin >> N >> K;
		intervals.push(N);
		for (int c = 0; c < K; c++) {
			int currLen = intervals.top();
			intervals.pop();
			minLR = (currLen-1)/2;
			maxLR = currLen - minLR - 1;
			if (minLR > 0) {
				intervals.push(minLR);
			}
			if (maxLR > 0) {
				intervals.push(maxLR);
			}
		}

		cout << "Case #" << cc << ": " << maxLR << " " << minLR << endl;
	}


	return 0;
}