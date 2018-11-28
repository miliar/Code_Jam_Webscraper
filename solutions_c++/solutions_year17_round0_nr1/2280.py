#include <bits/stdc++.h>

using namespace std;

void ans(string s) {
	static int n = 1;
	cout << "Case #" << n++ << ": " << s << '\n';
}

int main() { ios_base::sync_with_stdio(false);
	int x;
	cin >> x;
	for (int i = 0; i < x; i++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		
		int total = 0;
		while (s.find('-') != -1) {
			int p = s.find('-');
			if (p > s.size() - k) {
				ans("IMPOSSIBLE");
				total = -1;
				break;
			}
			for (int j = 0; j < k; j++) {
				s[j + p] = s[j + p] == '-' ? '+' : '-';
			}
			total++;
			//~ cout << s << endl;
		}
		if (total >= 0) ans(to_string(total));
	}
	
	return 0;
}
