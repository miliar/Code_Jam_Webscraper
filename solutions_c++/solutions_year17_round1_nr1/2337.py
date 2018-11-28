#include <bits/stdc++.h>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef	long long			ll;
typedef unsigned long long	ull;
typedef unsigned int		ui;
typedef unsigned short		us;
typedef pair<int, int>		ii;
typedef pair<int, ii>		iii;
typedef vector<int>			vi;
typedef vector<ii>			vii;
typedef vector<iii>			viii;
typedef vector<vi>			vvi;
typedef complex<double>		point;

int tc, t, r, c;
string str;
vector<string> v;
char ch;
bool b;

int main() {
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		v.clear();
		cin >> r >> c;
		for (int i = 0; i < r; ++i) {
			cin >> str;
			b = false;
			for (int j = 0; j < c; ++j)
				if (str[j] != '?') {
					b = true, ch = str[j];
					for (int k = j - 1; k >= 0 && str[k] == '?'; --k)
						str[k] = ch;
				}
			if (b)
				for (int j = c - 1; str[j] == '?'; --j)
					str[j] = ch;
			v.push_back(str);
		}
		for (int i = 0; i < r; ++i)
			if (v[i][0] != '?') {
				str = v[i];
				for (int j = i - 1; j >= 0 && v[j][0] == '?'; --j)
					v[j] = str;
			}
		for (int i = r - 1; v[i][0] == '?'; --i)
			v[i] = str;
		cout << "Case #" << t << ": " << endl;
		for (int i = 0; i < r; ++i)
			cout << v[i] << endl;
	}
	return 0;
}