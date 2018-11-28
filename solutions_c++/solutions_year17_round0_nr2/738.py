#include <iostream>
using namespace std;

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		string N; cin >> N;
		for (int i = N.length() - 2; i >= 0; i--) {
			if (N[i] > N[i+1]) {
				N[i]--;
				for (int j = i + 1; j < N.length(); j++) {
					N[j] = '9';
				}
			}
		}
		int k = 0;
		for (int i = 0; i < N.length(); i++) {
			if (N[i] == '0') {
				k++;
			} else {
				break;
			}
		}
		string ans = N.substr(k);
		cout << "Case #" << No << ": " << ans << endl;
	}
	return 0;
}
