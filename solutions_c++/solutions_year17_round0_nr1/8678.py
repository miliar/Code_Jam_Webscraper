#pragma comment(linker, "/STACK:100000000")
#define _SCL_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#pragma GCC optimize ("O2")
#define _USE_MATH_DEFINES
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <iterator>
#include <ostream>
#include <iomanip>
#include <cstring>
#include <sstream>
#include <cassert>
#include <cstdlib>
#include <istream>
#include <fstream>
#include <climits>
#include <complex>
#include <memory>
#include <string>
#include <bitset>
#include <vector>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef complex <ld> cd;

const bool db = false;

#define fs first
#define sd second
#define mp make_pair
#define pb push_back
#define ppb pop_back

#define inf 1000000007
#define nmax 100100
#define mmax 100100
#define eps 1e-12

unordered_map<string,int> ds;

int main() {
#ifdef Ahoma
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif // Ahoma
	int tests, count = 0, k, steps, n;
	cin >> tests;
	string s, new_s;
	set<pair<int, string > > my_queue;
	while (tests--) {
		count++;
		cin >> s >> k;
		n = s.size();
		ds.clear();
		ds[s] = 0;
		my_queue.insert({ 0,s });
		while (my_queue.size()) {
			s = my_queue.begin()->second, steps = my_queue.begin()->first;
			my_queue.erase(my_queue.begin());
			for (int pos = 0; pos + k - 1 < n; pos++) {
				new_s = s;
				for (int pos1 = pos; pos1 <= pos + k - 1; pos1++) {
					if (new_s[pos1] == '+')
						new_s[pos1] = '-';
					else new_s[pos1] = '+';
				}
				if (!ds.count(new_s) || ds[new_s] > steps + 1)
				{
					my_queue.erase({ ds[new_s],new_s });
					ds[new_s] = steps + 1;
					my_queue.insert({ ds[new_s],new_s });
				}
			}
		}
		s = "";
		for (int i = 0; i < n; i++)
			s += "+";
		cout << "Case #" << count << ": ";
		if (ds.count(s))
			cout << ds[s] << '\n';
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}