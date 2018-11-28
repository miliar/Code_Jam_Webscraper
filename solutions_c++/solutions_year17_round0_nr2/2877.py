#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;
ll n;

int main() {
	int t;
	char s[1000];
	cin >> t; for (int u = 0; u < t; u++) {
		cin >> s;
		int i = 0;
		for (i = 1; s[i] && s[i] >= s[i - 1]; i++);
		if (s[i] != 0) {
			for (i--; i && s[i] <= s[i-1]; i--);
			s[i]--;
			for (i++; s[i]; i++) s[i] = '9';
		}
		i = 0;
		while (s[i] && s[i] == '0') i++;
		if (s[i] == 0) i--;
		cout<< "Case #" << (u + 1) << ": " << (s+i) << endl;
	}
	return 0;
}
