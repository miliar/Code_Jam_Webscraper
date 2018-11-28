#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <bitset>
#include <random>
#include <stack>
#include <list>
#include <unordered_set>
#include <unordered_map>
#include <ctime>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define sc second
#define fs first
#define mp make_pair
#define all(x) x.begin(), x.end()
#define re(x) x.rbegin(), x.rend()

template<class T> T sqr(T x) { return x*x; }
ld pi = 3.1415926535897932384626433832795;

ll mod = 1e9 + 7;

ll gcd(ll a, ll b) {
	return b ? gcd(b, a % b) : a;
}

ll _gcd(ll a, ll b, ll & x, ll & y) {
	if (a == 0) {
		x = 0; y = 1;
		return b;
	}
	ll _x1, _y1;
	ll d = _gcd(b%a, a, _x1, _y1);
	x = _y1 - (b / a) * _x1;
	y = _x1;
	return d;
}

ld binpow(ld a, ll n) {
	ld res = 1;
	while (n) {
		if (n & 1)
			res *= a;
		a *= a;
		n >>= 1;
		//a %= mod;
		//res %= mod;
	}
	return res;
}

const int N = 1e3 + 10;

char get_lower(char c) {
	if (c == '0') return '9';
	else return c - 1;
}

void solve(int test) {
	string s;
	cin >> s;
	int changed = -1;
	for (int i = 0; i < s.size() - 1; i++) {
		if (s[i] > s[i + 1]) {
			changed = i;
			s[i] = get_lower(s[i]);
			for (int j = i + 1; j < s.size(); j++)
				s[j] = '9';
		}
	}
	if (changed != -1) {
		for (int i = changed; i >= 0; i--) {
			if (s[i] > s[i + 1]) {
				s[i] = get_lower(s[i]);
				for (int j = i + 1; j < s.size(); j++)
					s[j] = '9';
			}
		}
	}
	int start = 0;
	while (s[start] == '0') start++;
	printf("Case #%d: ", test);
	for (; start < s.size(); start++) cout << s[start];
	cout << endl;
}

int main() {
	FILE *f1, *f2;
	freopen_s(&f1, "B-large.in", "r", stdin);
	freopen_s(&f1, "B-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) solve(i + 1);
	return 0;
}