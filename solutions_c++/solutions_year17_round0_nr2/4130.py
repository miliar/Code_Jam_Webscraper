//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

typedef long long ll;

int a[55], b[55];

int ln;

inline void transform(ll x) {
	ln = 0;
	while (x) {
		a[++ln] = x % 10;
		x /= 10;
	}
	reverse (a + 1, a + ln + 1);
}

inline bool compare() {
	for (int i = 1; i <= ln; i++) {
		if (a[i] < b[i]) {
			return 0;
		}
		if (a[i] > b[i]) {
			return 1;
		}
	}
	return 1;
}

inline void fast() {
	ll n;
	cin >> n;
	transform(n);
	for (int i = 1; i <= ln; i++) {
		b[i] = a[1];
	}
	if (a[1] == 1 && !compare()) {
		for (int i = 1; i < ln; i++) {
			cout << 9;
		}
		cout << endl;
		return ;
	}
	for (int i = 1; i <= ln; i++) {
		for (int j = i; j <= ln; j++) {
			b[j] = a[i];
		}
		if (!compare()) {
			b[i]--;
			for (int j = i + 1; j <= ln; j++) {
				b[j] = 9;
			}
			for (int j = 1; j <= ln; j++) {
				cout << b[j];
			}
			cout << endl;
			return ;
		}
	}
	for (int i = 1; i <= ln; i++) {
		cout << b[i];
	}
	cout << endl;
}

int main() {
	// B-small-attempt0.in.txt
	freopen (fname"B-large.in.txt", "r", stdin);
	freopen (fname"out2.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		fast();
	}
	return 0;
}
