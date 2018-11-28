#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int n, cas, k, i, ans;
	string s;

	cin >> n;
	cas = 1;
	while (n) {
		cin >> s >> k;
		i = 0;
		ans = 0;
		while (i < s.length()) {
			while (i < s.length() && s[i] == '+') i++;
			if (i == s.length()) continue;
			else if (i > s.length()-k) {
				ans = -1;
				break;
			}
			else {
				for (int j = i; j < i+k; j++)
					if (s[j] == '+') s[j] = '-';
					else s[j] = '+';
				ans++;
			}
		}
		cout << "Case #" << cas++ << ": ";
		if (ans != -1) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
		n--;
	}

	return 0;
}