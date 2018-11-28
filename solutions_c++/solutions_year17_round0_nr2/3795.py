#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <set>
#include <functional>
using namespace std;

#define sz(a) ((int)((a).size()))
#define fi(a,b) for(int i = (a); i < (b); ++i)
#define fj(a,b) for(int j = (a); j < (b); ++j)
#define all(a) (a).begin(), (a).end()
typedef long long ll;

bool check(ll & n) {
	bool b = true;
	vector<int> v;
	while(n) {
		v.push_back(n % 10);
		n /= 10;
	}
	reverse(all(v));
	int pos = -1;
	fi(1, sz(v)) {
		if(v[i] < v[i - 1]) {
			pos = i;
			b = false;
		}
	}
	if(!b) {
		if(v[pos - 1] > 0) {
			--v[pos - 1];
			fi(pos, sz(v)) {
				v[i] = 9;
			}
		} else {
			while(v[pos - 1] == 0) {
				--pos;
			}
			--v[pos - 1];
			fi(pos, sz(v)) {
				v[i] = 9;
			}
		}
	}
	fi(0, sz(v)) {
		n *= 10LL;
		n += v[i];
	}
	return b;
}

void solve() {
	ll n;
	cin >> n;
	while(!check(n));
	cout << n;
}

int main() {
#ifdef MY_DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif
	int nT;
	cin >> nT;
	fi(0, nT) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}