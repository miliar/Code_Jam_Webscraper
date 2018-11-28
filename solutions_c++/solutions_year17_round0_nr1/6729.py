#include <bits/stdc++.h>

using namespace std;

int main (){

	freopen("in.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++){

		string s;
		int k, cnt, n, ans = 0;
		cin >> s >> k;
		n = s.size();

		for (int i = 0; i < n - k + 1; i++){
			cnt = -1;
			if (s[i] == '+')
				continue;

			for (int j = i; j < i+k; j++){
				if (s[j] == '-') s[j] = '+';
				else if (s[j] == '+' && cnt == -1){
					s[j] = '-';
					cnt = j;
				}
				else s[j] = '-';
			}
			if (cnt != -1) i = cnt - 1;
			++ans;

		}

		bool okay = 1;
		for (int i = 0; i < n; i++)
			if (s[i] == '-') okay = 0;

		cout << "Case #" << t << ": ";
		if (okay) cout << ans << endl;
		else cout << "IMPOSSIBLE\n";

	}


}
