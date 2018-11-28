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

int tests, n, R, O, Y, G, B, V;
vector<pair<int, char> > a;
char answer[nmax];

int main() {
	//freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	//freopen(NAME".in", "r", stdin);freopen(NAME".out", "w", stdout);
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cin >> n >> R >> O >> Y >> G >> B >> V;
		int ind = 0;
		a.clear();
		for (int j = 0; j < n; j++) {
			answer[j] = 0;
		}
		a.pb(mp(R, 'R'));
		a.pb(mp(Y, 'Y'));
		a.pb(mp(B, 'B'));
		sort(a.begin(), a.end());
		bool f = true;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < a[i].first; j++) {
				while (answer[ind] != 0) {
					ind = (ind + 1) % n;
				}
				answer[ind] = a[i].second;
				ind = (ind + 2) % n;
			}
		}
		for (int i = 0; i < n; i++) {
			if (answer[i] == answer[(i + 1) % n]) f = false;
		}
		printf("Case #%d: ", test);
		if (f) {
			for (int i = 0; i < n; i++) {
				printf("%c", answer[i]);
			}
			printf("\n");
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}

