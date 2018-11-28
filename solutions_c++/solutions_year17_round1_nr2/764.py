#include <iostream>
#include <deque>
#include <algorithm>
#include <vector>

using namespace std;

int bSearch(int y, int x) {
	int lo = 1;
	int hi = 1e6;
	while(lo <= hi) {
		long mid = lo + (hi - lo) / 2;
		if(1.1 * x * mid < y) 
			lo = mid + 1;
		else if(0.9 * x * mid > y)
			hi = mid - 1;
		else {
			while(0.9 * x * (mid + 1) <= y)
				mid++;
			return mid;
		}
	}
	return -1;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int N, P;
		cin >> N >> P;
		vector<int> R(N);
		for(int i = 0; i < N; i++)
			cin >> R[i];
		vector<vector<int>> Q(N, vector<int>(P));
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < P; j++)
				cin >> Q[i][j];
			sort(Q[i].begin(), Q[i].end());
		}
		int result = 0;
		while(!Q[0].empty()) {
			int curr = Q[0].back();	
			Q[0].pop_back();
			int C = bSearch(curr, R[0]);
			while(curr <= 1.1 * C * R[0]) {
				bool valid = true;
				for(int i = 1; i < N; i++) {
					while(!Q[i].empty() and Q[i].back() > 1.1 * C * R[i])
						Q[i].pop_back();
					if(Q[i].empty() or Q[i].back() < 0.9 * C * R[i]) {
						valid = false;	
						break;
					}
				}
				if(valid) {
					result++;
					for(int i = 1; i < N; i++)
						Q[i].pop_back();
					break;
				}
				C--;
			}
		}
		printf("Case #%d: %d\n", t, result);
	}
}
