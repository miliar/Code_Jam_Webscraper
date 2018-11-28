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

set<pair<ll, ll> > now;

void add(ll a, ll b) {
	auto it = now.lower_bound({a, 0});
	if (it != now.end() && it->first == a) {
		b += it->second;
		now.erase(it);
	}
	now.insert(mp(a, b));
}

ll n, k;
int tests;

int main() {
	//freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	//freopen(NAME".in", "r", stdin);freopen(NAME".out", "w", stdout);
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cin >> n >> k;
		now.clear();
		now.insert({n, 1});
		ll answer = -1;
		while (k) {
			auto it = prev(now.end());
			pair<ll, ll> a = *it;
			a.first--;
			now.erase(it);
			if (a.second >= k) {
				answer = a.first;
				break;
			} else {
				k -= a.second;
			}
			add(a.first - a.first / 2, a.second);
			add(a.first / 2, a.second);
		}
		printf("Case #%d: %lld %lld\n", test, answer - answer / 2, answer / 2);
	}
	return 0;
}

