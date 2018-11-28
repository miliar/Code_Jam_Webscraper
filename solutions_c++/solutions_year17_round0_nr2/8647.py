#include <fstream>
#include <iostream>
#include <string>

using namespace std;

string ans;

void process(string s, string result, int x) {
	if (x == -1) {
		if (ans.compare(result) < 0) {
			ans = result;
		}
		return;
	}
	string newResult1 = result;
	string newResult2 = result;
	string newS1 = s;

	if (((x < s.size() - 1 && result[x + 1] >= '9') || x == s.size() - 1) && x != 0) {
		newResult1[x] = '9';
		if (s[x] != '9') {
			int idx = x - 1;
			while (idx > -1) {
				if (newS1[idx] != '0') {
					newS1[idx]--;
					break;
				} else {
					newS1[idx] = '9';
					idx--;
				}
			}
		}
		process(newS1, newResult1, x - 1);
	}
	if ((x < s.size() - 1 && result[x + 1] >= s[x]) || x == s.size() - 1) {
		newResult2[x] = s[x];
		process(s, newResult2, x - 1);
	}
}

int main() {
	ifstream in("input.in");
	ofstream out("output.out");
	int c = 1, C;
	in >> C;
	while (c <= C) {
		string s, S;
		in >> s;
		ans = "";
		for (int i = 0; i < s.size(); i++) {
			S += "0";
			ans += "0";
		}
		process(s, S, s.size() - 1);
		if (ans[0] == '0') {
			ans = ans.substr(1, s.size() - 1);
		}
		cout << "Case #" << c << ": " << ans << endl;
		c++;
	}
	return 0;
}