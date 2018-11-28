#include <iostream>
#include <string>


using namespace std;

int solve() {

	string S;
	cin >> S;

	int K;
	cin >> K;

	bool b[1000];
	int len = S.length();

	for (int i = 0; i < len;i++) {
		b[i] = S.at(i) == '+' ? true : false;
	}

	int count = 0;
	for (int i = 0;i < len - K + 1; i++) {
		if (b[i] == false) {
			for (int j = 0; j < K; j++) {
				b[i+j] = ! b[i+j];
			}
			count ++;
		}
	}

	for (int i = 0; i < len; i++) {
		if (b[i] == false) {
			return -1;
		}
	}
	return count;
}



int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int result = solve();

		cout << "Case #" << i + 1 << ": "; 
		if (result == -1) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		cout << result << endl;

	}


	return 0;
}