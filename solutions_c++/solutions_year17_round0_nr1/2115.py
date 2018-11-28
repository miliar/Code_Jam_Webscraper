#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <limits> 
#include <queue>

using namespace std;

int solve(string& pancakes, int loc, int k, int num_flips);
void flip(string& pancakes, int loc);

int main() {
	int n; // number of test cases
	scanf("%d\n", &n);
	
	
	for (int i = 0; i < n; i++) {
		string line;
		getline(cin, line);

		int idx = line.find(" ");
		string pancakes = line.substr(0, idx);
		int k = stoi(line.substr(idx + 1));
	
		//cout << pancakes.length() << endl << "test: " << k << endl;
		int res = solve(pancakes, 0, k, 0);
		if (res == -1)
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i + 1 << ": " << res << endl;
	}
	

	return 0;
}

int solve(string& pancakes, int loc, int k, int num_flips) {
	for (int i = loc; i < pancakes.length(); i++) {
		//cout << pancakes << endl;
		if (pancakes[i] == '-') {
			if (i + k > pancakes.length()) {
				return -1;
			}

			for (int j = 0; j < k; j++) {
				flip(pancakes, i + j);
			}
			return solve(pancakes, i + 1, k, num_flips + 1);
		}
	}
	return num_flips;
}

void flip(string& pancakes, int loc) {
	if (pancakes[loc] == '-') 
		pancakes[loc] = '+';
	else
		pancakes[loc] = '-';
}