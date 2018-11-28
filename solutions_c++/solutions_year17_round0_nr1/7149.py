#include <iostream>
#include <string>

using namespace std;

int t, n, res;
bool pos;
string s;

int main() {
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s >> n;
		res = 0;
		for (int j = 0; j <= s.size()-n; ++j)
			if (s[j] == '-') {
				res++;
				for (int k = 0; k < n; ++k)
					s[j+k] = (s[j+k] == '+' ? '-' : '+');
			}
		pos = true;
		for (int j = s.size()-1; j > s.size()-n && pos; --j)
			if (s[j] == '-')
				pos = false;
		cout << "Case #" << i << ": ";
		if (pos)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}