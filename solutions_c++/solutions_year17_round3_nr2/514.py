#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<iomanip>
#include <cassert>
#include<algorithm>
#include <map>
#include<string>
#include<sstream>
#include<vector>
#include<set>
#include <queue>
#include <string.h>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())
#define mp make_pair
typedef long long li;

const int K = 1000;
const int N = 1450;
const int INF = 1e9;

int day[N];
int z[2][2][N][K];

int calc(int p, int f, int idx, int need){
	if (z[p][f][idx][need] != -1) return z[p][f][idx][need];
	
	if (idx == 1440) {	
		if (p == f && need == 0)
			return z[p][f][idx][need] = 0;
		return z[p][f][idx][need] = INF;
	}
	z[p][f][idx][need] = INF;
	if (p != day[idx] && calc(p, f, idx + 1, need - p) < INF) {
		z[p][f][idx][need] = min(z[p][f][idx][need], calc(p, f, idx + 1, need - p));
	}
	if (1 - p != day[idx] && 1 + calc(1 - p, f, idx + 1, need - (1 - p)) < INF) {
		z[p][f][idx][need] = min(z[p][f][idx][need], 1 + calc(1 - p, f, idx + 1, need - (1 - p)));
	}
	return z[p][f][idx][need];
}


void solve() {
	int test;
	cin >> test;
	for (int k = 1; k <= test; k++) {
		memset(day, -1, sizeof day);
		memset(z, -1, sizeof z);

		int n1, n2;
		cin >> n1 >> n2;
		for (int i = 0; i < n1; i++) {
			int c, d;
			cin >> c >> d;
			for (int j = c; j < d; j++) {
				day[j] = 0;
			}
		}
		for (int i = 0; i < n2; i++) {
			int c, d;
			cin >> c >> d;
			for (int j = c; j < d; j++) {
				day[j] = 1;
			}
		}
		cout << "Case #" << k << ": " << min(calc(0, 0, 0, 720), calc(1, 1, 0, 720)) << endl;
	}
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin.tie(0);
	cout.sync_with_stdio(false);
	
	solve();
	return 0;
}