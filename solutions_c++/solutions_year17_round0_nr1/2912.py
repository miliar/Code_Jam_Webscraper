#include <iostream>
#include <string>
using namespace std;

int main() {
	int t, n; cin >> t; for (int u = 0; u < t; u++) {
		char s[1002]; cin >> s >> n;
		int i, c = 0; 
		for (i = 0; s[i + n-1]; i++) if (s[i] == '-') {
			c++;
			for (int j = 0; j < n; j++) s[i+j] = (char)((int)'+' + (int)'-' - (int)s[i+j]);
		}
		for (; s[i] && s[i] == '+'; i++);
		cout << "Case #" << (u + 1) << ": ";
		if (s[i]) cout << "IMPOSSIBLE" << endl;
		else cout << c << endl;
	}
	return 0;
}

