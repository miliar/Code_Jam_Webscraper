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

#include <cstdint>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

int main(void) {
	int T;

	ifstream fin("B-small-attempt0.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T) {
		uint64_t num, ans;

		fin >> num;
		ans = num;

		int lastFail = -1;
		while (lastFail != 0) {
			lastFail = 0;
			int totalSigns = 0;
			int digit, prevDigit = 11;
			num = ans;
			while (num > 0) {
				digit = num % 10;
				if (digit > prevDigit) {
					lastFail = totalSigns;
				}
				prevDigit = digit;
				totalSigns++;
				num /= 10;
			}
			if (lastFail > 0) {
				uint64_t pwr = pow(10, lastFail);
				ans = ans - ans % pwr;
				ans--;
			}
		}

		fout << "Case #" << t + 1 << ": " << ans << endl;
	}
	fout.close();
	fin.close();
	return 0;
}