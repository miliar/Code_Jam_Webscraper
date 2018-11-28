#include <iostream>
#include <string>
using namespace std;
int main() {
	int T;
	cin >> T;
	for (int a = 1; a <= T; a++) {
		string S;
		int A[1000];
		int K;
		cin >> S >> K;
		for (int i = 0; i < S.length(); i++) {
			if (S[i] == '-') A[i] = -1;
			if (S[i] == '+') A[i] = 1;
		}
		int ans = 0;
		for (int i = 0; i + K <= S.length(); i++) {
			if (A[i] == -1) {
				for (int j = i + K - 1; j >= i; j--) {
					A[j] *= -1;
				}
				ans++;
			}
		}
		for (int i = 0; i < S.length(); i++) {
			if (A[i] == -1) {
				ans = -1;
				break;
			}
		}
		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", a);
		}
		else {
			printf("Case #%d: %d\n", a, ans);
		}
	}
}