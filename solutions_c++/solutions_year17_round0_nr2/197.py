#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		string S;
		cin >> S;
		int N = S.size();
		for (int s = N-2; s >= 0; --s) { // tidy from end
			if (S[s] <= S[s+1]) continue; // nothing to do
			S[s]--;
			for (int k = s+1; k < N; ++k) S[k] = '9';
		}
		
		long long num = 0;
		for (int x = 0; x < N; ++x) {
			num *= 10;
			num += S[x] - '0';
		}
		
		cout << "Case #" << i << ": " << num << endl;
	}
}