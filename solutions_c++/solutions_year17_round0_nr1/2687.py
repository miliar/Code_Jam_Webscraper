#include <iostream>

using namespace std;

int main() {
	int tc;
	cin >> tc;
	for(int t = 0; t < tc; ++t) {
		string S;
		int K;
		cin >> S >> K;
		S = "+" + S + "+";
		string X;
		for(int i = 1; i < (int)S.size(); ++i) {
			if(S[i - 1] != S[i]) {
				X.push_back('x');
			} else {
				X.push_back(' ');
			}
		}
		bool possible = true;
		int ret = 0;
		for(int d = 0; d < K; ++d) {
			bool a = false;
			for(int i = d; i < (int)X.size(); i += K) {
				if(a) ++ret;
				if(X[i] == 'x') {
					a = !a;
				}
			}
			if(a) {
				possible = false;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if(possible) {
			cout << ret << '\n';
		} else {
			cout << "IMPOSSIBLE" << '\n';
		}
	}
	
	return 0;
}