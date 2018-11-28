#include <iostream>
#include<stdio.h>
#include <string>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	//int n; scanf("%d", &n);
	int n; cin >> n;
	string output;

	for (int i = 1; i < n + 1;i++) {
		string s; //int k;
		cin >> s; //>> k;
		string output_str = "";
		string help_s;
		int j = 0;

		while (j < (int)s.size() - 1) {

			if (s[j] == s[j + 1]) {
				j += 1;
			}
			else if ((s[j] - '0') < (s[j + 1] - '0')) {
				output_str.append(s.substr(0, j + 1));
				s = s.substr(j + 1, s.size() - j - 1);
				j = 0;
				continue;
			}
			else {
				if (s[0] == '1') {
					s = string(s.size() - 1, '9');
					j = 0;
				}
				else {
					help_s = string(s.size(), '9');
					help_s[0] = s[0] - 1;
					s = help_s;
					j = 0;
					continue;
				}
			}
		}
		output_str.append(s);

		output = "Case #" + to_string(i) + ": " + output_str;
		cout << output << endl;
	}
}