#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int k;

void flip(string& line, int i) {
	for(int j = 0; j < k; j++) {
		line[i + j] = 0 + '+' + '-' - line[i + j];
	}
}

bool possible(string& line) {
	int cnt = 0;
	for(int i = 0; i < line.size(); i++)
		if(line[i] == '-') {
			cnt++;
		}
	return cnt == 0;
}

int solve(string& line) {
	int target = line[0];
	int flips = 0;
	for(int i = 0; i <= line.size() - k; i++) {
		if(line[i] != '+') {
			flip(line, i);
			//cout << "flip at " << i << endl;
			flips++;
		}
	}
	if(possible(line)) {
		return flips;
	}
	return -1;
}

int main() {
	int t;
	ios::sync_with_stdio(0);
	string line;
	cin >> t;
	for(int cas = 0; cas < t; cas++) {
		cin >> line >> k;
		//cout << line << " " << k << endl;
		int sol = solve(line);
		//cout << line << " " << k << endl;
		cout << "Case #" << cas + 1 << ": ";
		if(sol == -1)
			cout << "IMPOSSIBLE";
		else cout << sol;
		cout << '\n';

	}
}