#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <cstdio>
#include <map>
#include <vector>

#define ST first
#define ND second
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;


void solve_case() {
	double d, pos, spd, t, tmax=0;
	int n;
	cin >> d >> n;
	for (int i=0; i<n; i++) {
		cin >> pos >> spd;
		t = (d - pos) / spd;
		tmax = max(tmax, t);
	}
	printf("%.6f\n", d / tmax);
}


int main () {
    int te;
	cin >> te;
	for (int tt=1; tt<=te; tt++) {
		cout << "Case #" << tt << ": ";
		solve_case();
	}
}
