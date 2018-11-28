#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;

long long solve(string s, int k){
	long long flips = 0;

	for(int i = 0; i < s.size(); i++) {
		if(s[i] == '-') {
			if(i + k > s.size()) {
				return -1;
			}

			for(int j = 0; j < k; j++) {
				s[i + j] = s[i + j] == '-' ? '+' : '-';
			}
			flips++;
		}
	}

	return flips;
}

int main() {
	int t;
	string s;
	int k;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> s;
		cin >> k;
		long long sol = solve(s, k);
		if(sol >= 0)
			cout << "Case #" << (i + 1) << ": " << sol << endl;
		else
			cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
	}

	return EXIT_SUCCESS;
}
