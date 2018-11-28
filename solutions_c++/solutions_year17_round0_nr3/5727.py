#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>
#include <sstream>
#pragma comment(linker, "/STACK:133217728")

using namespace std;

multiset <pair<int, pair<int, int>>> s;

void add_segment(int len) {
	if (len < 1) return;
	if (len == 1) {
		s.insert({ 0, {0, 0} });
		return;
	}
	int a = (len + 1) >> 1;
	s.insert({ a - 1, {len - a, a - 1} });
}
int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, k;
		cin >> n >> k;
		s.clear();
		add_segment(n);

		for (int i = 0; i < k - 1; i++) {
			auto x = *(--s.end());
			//cout << x.first << " " << x.second.first << " " << x.second.second << endl;
			s.erase(--s.end());
			add_segment(x.second.first);
			add_segment(x.second.second);
		}

		auto x = *(--s.end());
		cout << "Case #" << t << ": " << x.second.first << " " << x.second.second << endl;
		
	}
	return 0;
}
