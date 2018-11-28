#include <bits/stdc++.h>
using namespace std;

void code() {
	int N, P;
	cin >> N >> P;

	vector<int> R(N);
	for(int i = 0 ;i < N; i++) {
		cin >> R[i];
	}
	vector<int> idx(N, 0);
	vector<vector<int> > ing(N, vector<int>(P));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < P; j++) {
			cin >> ing[i][j];
		}
		sort(ing[i].begin(), ing[i].end());
	}

	int mul = 1;
	int total = 0;
	while(true) {
		for (int i = 0; i < N; i++) {
			while(idx[i] < P && ing[i][idx[i]] * 10 < R[i] * mul * 9) {
				idx[i]++;
			}
			if (idx[i] == P) goto end;
			if (ing[i][idx[i]] * 10 > R[i] * mul * 11) {
				mul++;
				goto next;
			}
		}
		total++;
		for (int i = 0; i < N; i++) {
			idx[i]++;
		}

		next:;
	}

	end:
	cout << total << endl;
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		code();
	}
}
