#include <iostream>
#include <string>

using namespace std;

char flip(char c) {
	if (c == '+') return '-';
	else return '+';
}

int flipPancake(string S, int K) {
	int n = S.size();
	int sum = 0;
	for (int i = 0; i <= n - K; i ++) {
		if (S[i] == '-') {
			for (int j = 0; j < K; j ++)
				S[i + j] = flip(S[i + j]);
			sum ++;
		}
	}
	for (int i = n - K + 1; i < n; i++) {
		if (S[i] == '-') return -1;
	}
	return sum;
}

int main() {
	int T;
	cin >> T;

	string S;
	int K;
	for (int i = 0; i < T; i ++) {
		cin >> S >> K;
		cout << "Case #" << i + 1 << ": ";
		int result = flipPancake(S, K);
		if (result < 0) cout << "IMPOSSIBLE" << endl;
		else cout << result << endl;
	}
	return 0;
}
