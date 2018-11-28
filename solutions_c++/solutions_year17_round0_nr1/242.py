#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	string S; int K;
	cin >> S >> K;
	
	int L = S.length();
	int count = 0;
	for (int i=0; i<L-K+1; i++) {
		if (S[i] == '-') {
			count++;
			for (int j=0; j<K; j++) {
				if (S[i+j] == '-')
					S[i+j] = '+';
				else
					S[i+j] = '-';
			}
		}
	}
	
	cout << "Case #" << t << ": ";
	
	for (int i=L-K+1; i<L; i++) {
		if (S[i] == '-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	
	cout << count << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
