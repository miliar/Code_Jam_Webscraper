#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <limits.h>
#include <assert.h>
#include <stack>
#include <cmath>
#include <iomanip>
using namespace std;

int main () {
	long long t;
	cin >> t;
	for(long long tcase = 0; tcase < t; ++tcase) {
		long long result = 0;
		string S;
		long long K;
		cin >> S;
		cin >> K;
		for(int i = 0; (i + K - 1) < S.length(); ++i) {
			if(S[i] != '+') {
				for(int j = 0; j < K; ++j) {
					if(S[i + j] == '+') {
						S[i + j] = '-';
					} else {
						S[i + j] = '+';
					}
				}
				++result;
			}
		}
		string all_plus_s = string(S.length(), '+');
		bool all_plus = all_plus_s.compare(S) == 0;

		cout << "Case #" << tcase + 1 << ": ";
		if(all_plus)
			cout << result << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}
}
