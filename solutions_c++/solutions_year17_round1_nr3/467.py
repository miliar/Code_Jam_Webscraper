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
#include <unordered_map>
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

unordered_map <ll, int> d;

inline ll encode(int hd, int ad, int hk, int ak) {
	return hd + 101ll * ad + 101ll * 101 * hk + 101ll * 101 * 101 * ak;
}

inline void decode(ll coding, int &hd, int &ad, int &hk, int &ak) {
	hd = coding % 101;
	coding /= 101;
	ad = coding % 101;
	coding /= 101;
	hk = coding % 101;
	coding /= 101;
	ak = coding % 101;
}

queue <ll> q;

inline void solve() {
	while (!q.empty()) {
		q.pop();
	}
	d.clear();
	int hD, aD, hK, aK, buff, deBuff;
	cin >> hD >> aD >> hK >> aK >> buff >> deBuff;
	int initialHD = hD;
	q.push(encode(hD, aD, hK, aK));
	d[encode(hD, aD, hK, aK)] = 0;
	ll state, newState;
	while (!q.empty()) {
		state = q.front();
		q.pop();
		decode(state, hD, aD, hK, aK);
//m		cout << hD << " " << aD << " " << hK << " " << aK << " " << d[state] << endl;
		if (hK - aD <= 0) {
			cout << d[state] + 1 << endl;
			return ;
		}
		if (hD - aK > 0) {
			newState = encode(hD - aK, aD, hK - aD, aK);
			if (!d.count(newState)) {
				d[newState] = d[state] + 1;
				q.push(newState);
			}
		}
		if (hD - aK > 0) {
			newState = encode(hD - aK, aD + buff, hK, aK);
			if (!d.count(newState)) {
				d[newState] = d[state] + 1;
				q.push(newState);
			}
		}		
		if (initialHD - aK > 0) {
			newState = encode(initialHD - aK, aD, hK, aK);
			if (!d.count(newState)) {
				d[newState] = d[state] + 1;
				q.push(newState);
			}
		}
		if (hD - (max(aK - deBuff, 0)) > 0) {
			newState = encode(hD - (max(aK - deBuff, 0)), aD, hK, max(aK - deBuff, 0));
			if (!d.count(newState)) {
				d[newState] = d[state] + 1;
				q.push(newState);
			}
		}
	}
	cout << "IMPOSSIBLE\n";
}

int main() {
	freopen (fname"C-small-attempt1.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();
	}
	return 0;
}
