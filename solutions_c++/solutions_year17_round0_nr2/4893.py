/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>
//#include "sort.h"

#define ll long long
#define ld double
#define pii pair <int, int>
#define mp make_pair

using namespace std;

const int maxn = (int)1010;
char s[maxn];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	for (int it = 1; it <= t; it++) {
		printf("Case #%d: ", it);
		ll n;

		cin >> n;

		vector <int> a;

		while (n != 0) {
			a.push_back(n % 10);
			n /= 10;
		}

		reverse(a.begin(), a.end());

		for (int pos = (int)a.size(); pos >= 0; pos--) {
			bool fl = true;

			for (int j = 0; j < pos - 1; j++) {
				if (a[j] > a[j + 1]) {
					fl = false;
					break;
				}
			}

			if (!fl) {
				continue;
			}

			if (pos == (int)a.size()) {
				for (int j = 0; j < (int)a.size(); j++) {
					cout << a[j];
				}
				cout << endl;
				break;
			}

			if (pos == 0) {
				a[0]--;

				if (a[0] != 0) {
					cout << a[0];
				}

				for (int j = 1; j < (int)a.size(); j++) {
					cout << 9;
				}

				cout << endl;
				break;
			}

			if (a[pos] <= a[pos - 1]) {
				continue;
			}

			a[pos]--;

			for (int j = 0; j <= pos; j++) {
				printf("%d", a[j]);
			}

			for (int j = pos + 1; j < (int)a.size(); j++) {
				printf("9");
			}

			cout << endl;
			break;
		}
	}			

	return 0;
}
