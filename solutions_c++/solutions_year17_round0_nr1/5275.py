#include<iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int i = 0; i < T;i++){
		int count = 0;
		string S; int K;
		cin >> S >> K;

		cout << "Case #" << i+1 << ": ";

		vector<bool> pancake(S.length());
		for (int j = 0; j < S.length();j++) {
			if (S[j] == '-') pancake[j] = false;
			else pancake[j] = true;
		}

		for (int j = 0; j <= S.length() - K;j++) {
			if (pancake[j] == false) {
				count++;
				for (int k = 0; k < K;k++) {
					pancake[j + k] = (!pancake[j + k]);
				}
			}
		}

		for (int j = S.length() - K; j < S.length();j++) {
			if (pancake[j] == false) {
				cout << "IMPOSSIBLE" << endl;
				break;
			}
			if (j == S.length() - 1) {
				cout << count << endl;
			}
		}
	}
}