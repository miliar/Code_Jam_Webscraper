#pragma warning (disable : 4996)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <string>

using namespace std;

typedef long double ld;
#define mp make_pair

int main() {
#ifdef MANO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int qn;
	cin >> qn;
	string s;
	getline(cin, s);
	for (int uu = 0; uu < qn; ++uu) {
		getline(cin, s);
		string res = s;
		for (int i = 0; i < s.size(); ++i) {
			if (i == (int)s.size() - 1) {
				break;
			}
			if (s[i + 1] < s[i]) {				
				int j = i;
				for (int k = j + 2; k < s.size(); ++k) {
					s[k] = '9';
				}
				while (j >= 0 && s[j + 1] < s[j]) {
					s[j]--;
					s[j + 1] = '9';
					j--;
				}
				if (s[0] == '0' && (int)s.size() > 1) {
					s = s.substr(1, (int)s.size() - 1);
				}
				break;
			}
		}
		cout << "Case #" << uu + 1 << ": " << s << '\n';
	}

	return 0;
}