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
	for (int uu = 0; uu < qn; ++uu) {
		int len;
		int cnt = 0;
		cin >> s >> len;
		for (int i = 0; i < (int)s.size() - len + 1; ++i) {
			if (s[i] == '-') {
				cnt++;
				for (int j = i; j < i + len; ++j) {
					if (s[j] == '+') {
						s[j] = '-';
					}
					else {
						s[j] = '+';
					}
				}
			}
		}
		bool flag = true;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] == '-') {
				flag = false;
				break;
			}
		}
		cout << "Case #" << uu + 1 << ": ";
		if (!flag) {
			cout << "IMPOSSIBLE\n";
		}
		else {
			cout << cnt << '\n';
		}
	}

	return 0;
}