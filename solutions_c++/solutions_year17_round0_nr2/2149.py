#define _CRT_SECURE_NO_WARNINGS
#include <iostream> 
#include <vector>
#include <algorithm>
#include <map> 
#include <string>
#include <set> 
#include <iterator> 
#include <deque>
#include <iomanip>
#include <string> 
#include <math.h> 
#include <time.h>
#include <queue> 
#include <stdio.h>
#include <valarray>
#include <stack>

#define mp(x, y) make_pair(x, y)
#define all(x) x.begin(), x.end() 
#define det(a, b, c, d) a*d - b*c

typedef long long ll;

using namespace std;

bool is_tidy(int n) {
	int prev = 9;
	while (n) {
		if (n % 10 > prev) {
			return false;
		}
		n /= 10;
	}
	return true;
}

bool is_tidy(string s) {
	int nn = s.length();
	for (int i = 1; i < nn; i++) {
		if (s[i - 1] > s[i]) {
			return false;
		}
	}
	return true;
}

void put_nines(string &s, int pos) {
	int nn = s.length();
	for (int i = pos; i < nn; i++) {
		s[i] = '9';
	}
}

void clear_leading_zeros(string &s) {
	int pos = 0;
	int nn = s.length();
	for (int i = 0; i < nn; i++) {
		if (s[i] != '0') {
			pos = i;
			break;
		}
	}
	s = s.substr(pos);
}

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string n;
		cin >> n;
		if (is_tidy(n)) {
			cout << "Case #" << i << ": " << n << endl;
			continue;
		}
		int nn = n.length();
		for (int i = nn - 1; i >= 0; i--) {
			if (n[i] > '0') {
				n[i]--;
				put_nines(n, i + 1);
			}
			if (is_tidy(n)) {
				break;
			}
		}
		clear_leading_zeros(n);
		cout << "Case #" << i << ": " << n << endl;
	}
	return 0;
}
