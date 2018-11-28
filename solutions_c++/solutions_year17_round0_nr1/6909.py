#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

int main(void) {
	int T;

	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T) {
		int K;
		string S;

		fin >> S >> K;
		int moves = 0;

		int end = S.size() - K;
		for (int i = 0; i <= end; i++) {
			if (S[i] == '-') {
				moves++;
				for (int j = i; j < i + K; j++) {
					if (S[j] == '-') {
						S[j] = '+';
					} else {
						S[j] = '-';
					}
				}
			}
		}
		bool good = true;
		for (auto& c : S) {
			if (c == '-') {
				good = false;
				break;
			}
		}
		if (good) {
			fout << "Case #" << t + 1 << ": " << moves << endl;
		}
		else {
			fout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		}
	}
	fout.close();
	fin.close();
	return 0;
}