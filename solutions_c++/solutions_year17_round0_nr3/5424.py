#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
#define INF 100000000;
int main() {
	int tc;
	cin >> tc;
	int N; int K;
	vector<int> left, right; vector<bool> occuped; int cont = 0;
	while (tc--) {
		cont++;
		left.clear(); right.clear(); occuped.clear();
		cin >> N >> K;
		left.push_back(0);
		for (int i = 0; i < N; i++) left.push_back(i);
		left.push_back(N);
		right.push_back(N);
		for (int j = N - 1; j >= 0; j--) right.push_back(j);
		right.push_back(0);
		occuped.assign (N + 2, false); occuped[0] = true; occuped[N + 1] = true;
		int occupedIndex = 0;
		for (int i = 0; i < K; i++) {
			
			int minMaxDist = -1; int maxMaxDist = -1;
			for (int j = 1; j < N + 1; j++) {
				if (occuped[j]) continue;
				if (min(right[j], left[j]) > minMaxDist) {
					minMaxDist = min(right[j], left[j]); occupedIndex = j;
					maxMaxDist = max(right[j], left[j]);
					//cout << j << "-" << minMaxDist << "-" << maxMaxDist << endl;
				}
				else if (min(right[j], left[j]) == minMaxDist) {
					if (max(right[j], left[j]) > maxMaxDist) {
						//cout << j << "~" << maxMaxDist << "~" << max(right[i], left[i]) << endl;
						maxMaxDist = max(right[j], left[j]);
						occupedIndex = j;
					}
				}
			}
			occuped[occupedIndex] = true;
			for (int j = 0; j < N + 2; j++) {
				if (j == occupedIndex) continue;
				if (occupedIndex < j) {
					left[j] = min(left[j], j - 1 - occupedIndex);
				} else {
					right[j] = min (right[j], occupedIndex - 1 - j);
				}
			}/*
			if (i == K - 1) {
				for (int t = 0; t < N + 2; t++)
					if (occuped[t]) cout << 'x';
					else cout << ".";
				cout << endl;
			}*/
		}
		cout << "Case #" << cont << ": " << max(left[occupedIndex], right[occupedIndex]) << " " << min(left[occupedIndex], right[occupedIndex]) << endl;
	}


}		