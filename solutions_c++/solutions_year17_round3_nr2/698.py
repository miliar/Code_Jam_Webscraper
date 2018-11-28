#include <bits/stdc++.h>
using namespace std;
bool ca[1500];
bool ja[1500];
int memo[725][2][2][1445];

int exch(int ct, bool isC, bool startC, int time) {
	int temp = isC ? 1 : 0;
	int temp2 = startC ? 1 : 0;
	if (ct > 720) return 100000;
	if (time - ct > 720) return 100000;
	if (time == 1440) {
		if (startC != isC) return 1;
		else return 0;
	}
	if (time > 1440) return 100000;
	if (ca[time] && isC) {
		return 100000;
	}
	if (ja[time] && !isC) {
		return 100000;
	}
	if (memo[ct][temp2][temp][time] != -1) {
		return memo[ct][temp2][temp][time];
	}
	if (isC) {
		return memo[ct][temp2][temp][time] = min( exch(ct + 1, true, startC, time+1), 1 + exch(ct + 1, false, startC, time+1) );
	}
	else {
		return memo[ct][temp2][temp][time] = min( 1 + exch(ct, true, startC, time+1), exch(ct, false, startC, time+1) );
	}
	 
	
}

int main() {
	int tc;
	freopen("B-large.in", "r", stdin);
	freopen("B-large-2.out", "w", stdout);
	cin >> tc;
	for (int q= 1; q <= tc; q++) {
		int c,j;
		memset(memo, -1, sizeof(memo));
		for (int i = 0; i <= 1440; i++) {
			ca[i] = false;
			ja[i] = false;
		}
		cin >> c >> j;
		for (int i =0; i < c; i++) {
			int a,b;
			cin >> a >> b;
			for (int j = a; j < b; j++) {
				ca[j] = true;
			}
		}
		for (int i =0; i < j; i++) {
			int a,b;
			cin >> a >> b;
			for (int j = a; j < b; j++) {
				ja[j] = true;
			}
		}
		int ans = min(exch(0,true,true, 0), exch(0,false,false,0));
		/*if (ans == 1) {
			ans = 2;
		}*/
		printf("Case #%d: %d\n", q, ans);
	}
}
