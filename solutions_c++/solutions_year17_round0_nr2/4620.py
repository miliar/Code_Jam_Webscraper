#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <queue>


using namespace std;

bool good(int n) {
	stringstream ss;
	ss << n;
	string s;
	ss >> s;
	for (int i = 0; i + 1 < s.length(); i++) {
		if (s[i] > s[i + 1])return false;
	}
	return true;
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tcs;
	cin >> tcs;
	for (int i = 1; i <= tcs; ++i) {
		int k;
		cin >> k;
		while (!good(k))k--;
		cout << "Case #" << i << ": " << k << endl;
	}


	return 0;
}

