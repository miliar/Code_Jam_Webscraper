#include<bits/stdc++.h>
using namespace std;
string s;

int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	unsigned long long int cases = 1, count1, t, n, l, i, j;
	//string s;
	cin >> t;
	while (cases <= t) {
		count1 = 0;
		cout << "Case #" << cases++ << ": ";
		cin >> s >> n;
		l = s.length();
		for (i = 0; i < l - n; i++) {
			if (s[i] == '-') {
				count1++;
				for (j = 0; j < n; j++)
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
			}
		}
		int flag = 1;
		for (j = i + 1; j < l; j++)
			if (s[j] != s[j - 1])
				flag = 0;
		if (flag) {
			if (s[i + 1] == '-')
				count1++;
			cout << count1 << endl;
		} else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
