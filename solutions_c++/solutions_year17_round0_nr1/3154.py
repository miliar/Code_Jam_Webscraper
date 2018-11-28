#include <iostream>
#include <string>
using namespace std;

int solve(string& pan_cake_str, int fliper_size) {
	int ret = 0;
	int i = 0;
	for (; i + fliper_size <= pan_cake_str.size(); ++i) {
		if (pan_cake_str.c_str()[i] == '-') {
			++ret;
			for (int j = 0; j < fliper_size; ++j) {
				if (pan_cake_str.c_str()[i + j] == '+') {
					pan_cake_str.at(i + j) = '-';
				}
				else {
					pan_cake_str.at(i + j) = '+';
				}
			}
		}
	}
	for (; i < pan_cake_str.size(); ++i) {
		if (pan_cake_str.c_str()[i] == '-') {
			return -1;
		}
	}
	return ret;
}

int main() {
	int t;
	string pan_cake_str;
	int fliper_size;
	cin >> t;
	for (int tloop = 1; tloop <= t; ++tloop) {
		cin >> pan_cake_str;
		cin >> fliper_size;
		int ans = solve(pan_cake_str, fliper_size);
		if(ans == -1) cout << "Case #" << tloop << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << tloop << ": " << ans << endl;
	}
}