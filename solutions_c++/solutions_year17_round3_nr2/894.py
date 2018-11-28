#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int getInterval(int from , int to) {
	if (from < to) {
		from += 1440;
	}
	return from - to;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int c;
		int j;
		vector <int> acfrom;
		vector <int> acto;
		vector <int> ajfrom;
		vector <int> ajto;
		cin >> c;
		cin >> j;
		for (int i = 0; i < c; i++) {
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
			acfrom.push_back(tmp1);
			acto.push_back(tmp2);
		}
		for (int i = 0; i < j; i++) {
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
			ajfrom.push_back(tmp1);
			ajto.push_back(tmp2);
		}

		int ret = 2;
		int maxInterval = -1;
		if (c > 1) {
			maxInterval = max(maxInterval, getInterval(acfrom[0], acto[1]));
			maxInterval = max(maxInterval, getInterval(acfrom[1], acto[0]));
		}
		if (j > 1) {
			maxInterval = max(maxInterval, getInterval(ajfrom[0], ajto[1]));
			maxInterval = max(maxInterval, getInterval(ajfrom[1], ajto[0]));
		}
		if (maxInterval >=0 && maxInterval < 720) {
			ret = 4;
		}

		cout << "Case #" << t << ": " << ret << endl;
	}
}

