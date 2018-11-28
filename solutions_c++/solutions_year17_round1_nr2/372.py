#include <bits/stdc++.h>

using namespace std;

int Slow(int Q, int R) {
	return (10*Q+11*R-1)/(11*R);
}
int Shigh(int Q, int R) {
	return (10*Q)/(9*R);
}

void doCase(int t) {
	int N, P;
	cin >> N >> P;
	
	vector<int> R(N);
	for (int i=0; i<N; i++) cin >> R[i];
	
	vector<vector<int>> Q(N, vector<int>(P));
	for (int i=0; i<N; i++)
		for (int j=0; j<P; j++)
			cin >> Q[i][j];
	
	for (int i=0; i<N; i++)
		sort(Q[i].begin(), Q[i].end());
	
	vector<int> indx(N,0);
	
	int count = 0;
	while (true) {
		bool isEnd = false;
		for (int i=0; i<N; i++) {
			if (indx[i] == Q[i].size()) isEnd = true;
		}
		if (isEnd) break;
		
		int maxL = 0;
		int minH = 10000000;
		for (int i=0; i<N; i++) {
			maxL = max(maxL, Slow(Q[i][indx[i]], R[i]));
			minH = min(minH, Shigh(Q[i][indx[i]], R[i]));
		}
		if (maxL <= minH) {
			count++;
			for (int i=0; i<N; i++) {
				indx[i]++;
			}
		} else {
			for (int i=0; i<N; i++) {
				if (Shigh(Q[i][indx[i]],R[i]) < maxL)
					indx[i]++;
			}
		}
	}
	
	cout << "Case #" << t << ": " << count << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
