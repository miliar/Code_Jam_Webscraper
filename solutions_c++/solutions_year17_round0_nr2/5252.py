#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#define ll long long
using namespace std;
int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 1; t <= T;t++) {
		cout << "Case #" << t << ": ";

		string S; cin >> S;
		int f = 0;
		for (int i = 0; i < S.length() - 1;i++) {
			if (S[i] > S[i + 1]) {
				S[f]--;
				for (int j = f + 1; j < S.length();j++) {
					S[j] = '9';
				}
				break;
			}
			else if (S[i] < S[i + 1]) {
				f = i + 1;
			}
		}
		ll ans = 0;
		for (int i = 0; i < S.length(); i++) {
			ans *= 10;
			ans += S[i] - '0';
		}
		cout << ans << endl;
	}
}