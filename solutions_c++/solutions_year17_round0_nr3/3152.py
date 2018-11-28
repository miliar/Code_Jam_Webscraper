#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string.h>

#include <vector>
#include <limits>
#include <queue>
#include <cstdlib>
#include <map>
#include <math.h>
#include <limits>
#include <time.h>
#include <bitset>
#include <set>
#include <stack>
#include <complex>
#include <ctime>
using namespace std;
#define ll long long

#define endl '\n'

ll n, k;
map<ll, ll> lista[2];
map<ll, ll>::iterator it;

bool now;

void solve() {
	cin >> n >> k;
	if (n == k) {
		cout << "0 0" << endl;
		return;
	}

	now = false;
	lista[0].clear();
	lista[0][n] = 1;

	lista[1].clear();

	ll last = -1;
	while (k > 0) {
		it = lista[now].end();
		lista[now ^ 1].clear();
		it--;
		while (true) {
			ll mid = it->first / 2;

			if (it->second >= k) {

				if (it->first % 2 == 1)
					lista[now ^ 1][ mid  ] += k * 2LL;
				else {
					lista[now ^ 1][ mid ]     += k;
					if (mid > 1)
						lista[now ^ 1][ mid - 1 ] += k;
				}

				last = it->first;

				it->second -= k;
				k = 0;
				break;

			} else {
				if (it->first % 2 == 1)
					lista[now ^ 1][ mid  ] += it->second * 2LL;
				else {
					lista[now ^ 1][ mid ]     += it->second;
					if (mid > 1)
						lista[now ^ 1][ mid - 1 ] += it->second;
				}

				k -= it->second;
				it->second = 0;
			}

			if (it == lista[now].begin()) break;
			it--;
		}

		now ^= 1;
	}

	ll a = -1, b = 0;

	if (last % 2 == 1)
		a = b = last / 2;
	else
		a = last / 2, b = max(0LL, last / 2 - 1);

	cout << a << " " << b << endl;
}

int main(){
	//freopen("/Users/jcfernandez/Downloads/CodeJam/input.txt", "r", stdin);
	//freopen("/Users/jcfernandez/Downloads/CodeJam/output.txt", "w", stdout);

	int cas, caso = 1;
	cin >> cas;
	while(cas--) {
		cout << "Case #" << caso++ << ": ";
		solve();
	}
	return 0;
}
