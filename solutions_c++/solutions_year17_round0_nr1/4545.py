#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <ctime>
#include <string>
#include <cstring>
#include <random>
#define mp make_pair
#define pb push_back
#define NAME ""
#define y1 y1_423
#define list lista

using namespace std;

typedef long long ll;
typedef long double ld;

template<typename T>
ostream& operator << (ostream& cout, const vector<T> &a) {
	if ((int)a.size() == 0) {
		return (cout << "()");
	}
	cout << "(" << a[0];
	for (int i = 1; i < (int)a.size(); i++) {
		cout << "; " << a[i];
	}
	return (cout << ")");
}

template<typename T>
ostream& operator << (ostream& cout, const set<T> &a) {
	if ((int)a.size() == 0) {
		return (cout << "{}");
	}
	auto it = a.begin();
	cout << "{" << *it;
	++it;
	for (; it != a.end(); ++it) {
		cout << "; " << *it;
	}
	return (cout << "}");
}

template<typename T>
ostream& operator << (ostream& cout, const multiset<T> &a) {
	if ((int)a.size() == 0) {
		return (cout << "{}");
	}
	auto it = a.begin();
	cout << "{" << *it;
	++it;
	for (; it != a.end(); ++it) {
		cout << "; " << *it;
	}
	return (cout << "}");
}

template<typename T1, typename T2>
ostream& operator << (ostream& cout, const pair<T1, T2> &a) {
	return cout << "(" << a.first << "; " << a.second << ")";
}

random_device gen;
mt19937 rnd(gen());

const int nmax = 2000 * 1000;
const int inf = 2000 * 1000 * 1000;
const ll infl = 1000ll * 1000ll * 1000ll * 1000ll * 1000ll * 1000ll;
const int mod = 1000 * 1000 * 1000 + 7;
const ld pi = acos(-1.0);

int tests, k;
string s;

int main() {
	//freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	//freopen(NAME".in", "r", stdin);freopen(NAME".out", "w", stdout);
	cin >> tests;
	getline(cin, s);
	for (int test = 1; test <= tests; test++) {
		cin >> s >> k;
		int answer = 0;
		for (int j = 0; j < (int)s.length() - k + 1; j++) {
			if (s[j] == '-') {
				for (int q = j; q < j + k; q++) {
					s[q] = (s[q] == '-' ? '+' : '-');
				}
				answer++;
			}
		}
		bool f = true;
		for (int j = 0; j < (int)s.length(); j++) {
			if (s[j] == '-') f = false;
		}
		if (!f) {
			printf("Case #%d: IMPOSSIBLE\n", test);
		} else {
			printf("Case #%d: %d\n", test, answer);
		}
	}
	return 0;
}

