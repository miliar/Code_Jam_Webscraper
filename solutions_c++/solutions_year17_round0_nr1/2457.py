#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define SREP(s,i,m) for(unsigned int i = s; i < m; ++i)
#define REP(i,m) SREP(0,i,m)

using namespace std;

#ifdef _MSC_VER
using LONG = __int64;
using ULONG = unsigned __int64;
#else
using LONG = long long int;
using ULONG = unsigned long long int;
#endif

void solve(string str, int size) {
	vector<bool> state(str.size());
	REP(i, str.size()) {
		state[i] = str[i] == '+';
	}
	int cnt = 0;
	REP(i, state.size() - (size - 1)) {
		if (!state[i]) {
			REP(j, size) {
				state[i + j].flip();
			}
			cnt++;
		}
	}
	bool ok = all_of(state.begin(), state.end(), [](bool x) { return x; });
	if (ok) {
		cout << cnt << endl;
	}
	else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main(void) {
	int T;
	cin >> T;
	REP(i, T) {
		string state;
		int S;
		cin >> state >> S;
		cout << "Case #" << (i + 1) << ": ";
		solve(state, S);
	}
	return 0;
}