#include "assert.h"
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>

using namespace std;

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

template<typename T> inline void swap(pair<T, T> &p) { swap(p.first , p.second ); }

#define all(v) v.begin(),v.end()

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) { if (i) os << ' '; os << v[i]; } os << endl; return os; }
template <typename T1, typename T2> ostream& operator << (ostream& os, const vector<pair<T1, T2>> &v) { for (int i = 0 ; i < v.size() ; i++) { os << v[i] << endl; } return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

void assert2(bool x) {
	if (!x) exit(0);
}

string solve() {
	next(int, n);

	next(int, r);
	next(int, o);
	next(int, y);
	next(int, g);
	next(int, b);
	next(int, v);

	map<char, int> count;
	count['R'] = r;
	count['O'] = o;
	count['Y'] = y;
	count['G'] = g;
	count['B'] = b;
	count['V'] = v;
	map<char, int> colors;
	colors['R'] = 1;
	colors['O'] = 3;
	colors['Y'] = 2;
	colors['G'] = 6;
	colors['B'] = 4;
	colors['V'] = 5;

	vector<char> present;
	for (auto kvp : count) if (kvp.second > 0) present.push_back(kvp.first);

	const string impossible = "IMPOSSIBLE";
	if (present.size() == 1) return impossible;
	if (present.size() == 2) {
		if (colors[present[0]] & colors[present[1]]) return impossible;
		if (count[present[0]] != count[present[1]]) return impossible;
		string result = "";
		FOR (i, 0, count[present[0]]) {
			result += present[0];
			result += present[1];
		}
		return result;
	}

	if (count['G'] > 0 && count['R'] <= count['G']) return impossible;
	if (count['V'] > 0 && count['Y'] <= count['V']) return impossible;
	if (count['O'] > 0 && count['B'] <= count['O']) return impossible;

	count['R'] -= count['G'];
	count['Y'] -= count['V'];
	count['B'] -= count['O'];

	if (count['R'] * 2 > count['R'] + count['Y'] + count['B']) return impossible;
	if (count['Y'] * 2 > count['R'] + count['Y'] + count['B']) return impossible;
	if (count['B'] * 2 > count['R'] + count['Y'] + count['B']) return impossible;


	vector<pair<int, char>> remains = {
		{ count['R'] , 'R' },
		{ count['Y'] , 'Y' },
		{ count['B'] , 'B' },
	};

	string result = "";
	sort(all(remains)); reverse(all(remains));
	while (remains[0].first) {
		string toppend = "";
		if (remains[2].first == remains[0].first && remains[1].first == remains[0].first) {
			toppend += remains[0].second;
			toppend += remains[1].second;
			toppend += remains[2].second;
			remains[0].first--;
			remains[1].first--;
			remains[2].first--;
		} else {
			int otherIndex = remains[1].first > remains[2].first ? 1 : 2;
			remains[0].first--;
			remains[otherIndex].first--;
			toppend += remains[0].second;
			toppend += remains[otherIndex].second;
		}

		for (auto c : toppend) {
			result += c;
			char other;
			for (auto kvp : colors) if ((kvp.second | colors[c]) == 7) other = kvp.first;
			while (count[other]) {
				result += other;
				result += c;
				count[other]--;
			}
		}
	}

	return result;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	fixed(cout); cout << setprecision(10);
	
	next(int, n);
	FOR (i, 0, n) {
		auto res = solve();
		cout << "Case #" << (i + 1) << ": ";
		// if (res == -1) cout << "IMPOSSIBLE" << endl;
		// else 
			cout << res << endl;
	}

	cerr << "Done" << endl;
}