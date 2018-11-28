#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int t;
string s;
int k, len;
int cnt;
int main() {
	scanf("%d", &t);
	for (int test = 0; test < t; test++) {
		s = "";
		cnt = 0;
		cin >> s;
		scanf("%d", &k);
		bool succ = true;
		len = s.length();
		for (int i = 0; i <= len - k; i++) {
			if (s[i] == '-') {
				cnt++;
				for (int g = 0; g < k; g++) { //k°¹¼ö¸¸Å­ ¹Ù²ãÁØ´Ù
					if (s[i + g] == '-') {
						s[i + g] = '+';
					}
					else {
						s[i + g] = '-';
					}
				}
			}
		}
		for (int i = 0; i < len; i++) {
			if (s[i] == '-') {
				succ = false;
				break;
			}
		}
		if (succ) {
			cout << "Case #" << test + 1<< ": " << cnt << "\n";
		}
		else {
			cout << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << "\n";
		}
	}

	return 0;
}