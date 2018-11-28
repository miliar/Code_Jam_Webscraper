#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>
#include <map>

using namespace std;

string flip(string s, int x, int y) {
	for (int i = x; i < y; i++) {
		s[i] = (s[i] == '-') ? '+' : '-';
	}
	return s;
}

bool isHappy(string s) {
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			return false;
		}
	}
	return true;
}

int process(string s, int k) {
	map<string, bool> v;
	queue<pair<string, int> > q;
	q.push(make_pair(s, 0));

	while (!q.empty()) {
		pair<string, int> cur = q.front();
		q.pop();
		int curCnt = cur.second;
		string curStr = cur.first;

		if (isHappy(curStr)) {
			return curCnt;
		}

		for (int i = 0; i < s.size() - k + 1; i++) {
			string nextStr = flip(curStr, i, i + k);
			if (v.find(nextStr) != v.end()) {
				continue;
			}
			v[nextStr] = true;
			q.push(make_pair(nextStr, curCnt + 1));
		}
	}
	return -1;
}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int c = 1, C;
	cin >> C;
	while (c <= C) {
		string s;
		int k;
		cin >> s >> k;
		int result = process(s, k);
		cout << "Case #" << c << ": ";
		if (result == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << result;
		}
		cout << endl;
		c++;
	}
	return 0;
}