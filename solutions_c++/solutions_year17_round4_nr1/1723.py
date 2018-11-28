#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define FOR2(i, s, n) for (int i = (s); i <= (n); ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int N, P;
int G[110];
int cnt[5];

int ans2() {
	int sol = 0;
	int left = cnt[1];
	while(left > 0) {
		sol++;
		left -= 2;
	}
	return sol;
}

int ans3() {
	int sol = 0;
	int g = min(cnt[1], cnt[2]);
	sol += g;
	cnt[1] -= g;
	cnt[2] -= g;

	int left = max(cnt[1], cnt[2]);

	while(left > 0) {
		sol++;
		left -= 3;
	}
	return sol;
}

void solve()
{    
	cin >> N >> P;
	REP(i, 5) cnt[i] = 0;
	REP(i, N) {
		int x;
		cin >> x;
		cnt[x % P]++;	
	}
	int sol = cnt[0];

	if (P == 2) {
		sol += ans2();
	}
	else if (P == 3) {
		sol += ans3();
	}
	cout << sol << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}