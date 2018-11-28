#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iomanip>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;
typedef long long ll;

int a[110];
int tots[10];

void solve() {
	REP(i, 10) tots[i] = 0;
	int N, P;
	cin >> N >> P;
	REP(i, N) {
		cin >> a[i];
		a[i] %= P;
		tots[a[i]]++;
	}
	int res = tots[0];
	int ones = tots[1];
	int twos = tots[2];
	int threes = tots[3];
	if (P == 2) {
		res += tots[1] / 2;
		res += tots[1] % 2;
	}
	if (P == 3) {
		int ma = min(ones, twos);
		res += ma;
		ones -= ma;
		twos -= ma;
		if (twos > 0) ones = twos;
		res += ones / 3;
		if (ones % 3) res ++;
	}
	if (P == 4) {
		res += twos / 2;
		twos %= 2;
		int ma = min(ones, threes);
		res += ma;
		ones -= ma;
		threes -= ma;
		if (threes) ones = threes;
		if (twos) {
			if (ones >= 2) {
				twos --;
				ones -= 2;
				res++;
			}
		}
		res += ones / 4;
		if (ones % 4 || twos) res ++;
	}
	cout << res;
}

int main() {
	int t;
	cin >> t;
	cout << fixed << setprecision(10);
	REP(i, t) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}
}