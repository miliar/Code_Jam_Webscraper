#include <bits/stdc++.h>
using namespace std;

int T, K, N;
string s;

int main() {
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> s >> K;
		int ans = 0;
		int N = s.length();
		for (int i=0; i<=N-K; i++)
			if (s[i] == '-') {
				ans++;
				for (int j=0; j<K; j++)
					s[i+j] = '-' + '+' - s[i+j];
			}

		cout << "Case #" << t << ": ";
		if (s.find('-') != string::npos)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}
