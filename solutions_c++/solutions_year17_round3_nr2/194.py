#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>

#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define iinf 2000000000
#define linf 2000000000000000000LL
#define MOD (1000000007)
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)

const string IMPOSSIBLE = "IMPOSSIBLE\n";
inline void case_print() {
	static int it = 0;
	it += 1;
	cout << "Case #" << it << ": ";
}


int dp[720*2 + 10][3][725]= {0};
#define inf 1000000

int main() {
	ios_base::sync_with_stdio(0);
	freopen("B-large.in", "r",stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	int DAY = 720 * 2;
	
	while (T --> 0) {
		int ac, aj;
		cin >> ac >> aj;
		vector<pair<int,int> > a(ac + 1), b(aj + 1);
		
		for (int i = 1; i <= ac; i ++)
			cin >> a[i].first >> a[i].second;
		for (int i = 1; i <= aj; i ++)
			cin >> b[i].first >> b[i].second;
		sort(a.begin() + 1, a.end(), greater<pair<int,int> >());
		sort(b.begin() + 1, b.end(), greater<pair<int,int> >());
		
		for (int t = 0; t <= DAY; t ++) {
			for (int r = 0; r <= 1; r ++)
				for (int s = 0; s <= 720; s ++)
					dp[t][r][s] = inf;
		}
		
		
		dp[0][0][0] = 0;
		dp[0][1][0] = 0;
		
		for (int time = 1; time <= DAY; time ++) {
			while (a.size() > 0 && a.back().second <= time) a.pop_back();
			while (b.size() > 0 && b.back().second <= time) b.pop_back();
			bool busy_0 = 0, busy_1 = 0;
			if (a.size() > 0 && a.back().first <= time) busy_0 = 1;
			if (b.size() > 0 && b.back().first <= time) busy_1 = 1;
			
			//cout << time << " " << busy_0 << " " << busy_1 << endl;
			
			assert((!busy_1) || (!busy_0));
			for (int s = 1; s <= time; s ++) {
				if (!busy_0) {
					dp[time][0][s] = dp[time - 1][0][s -  1];
					dp[time][0][s] = min(dp[time][0][s], dp[time - 1][1][time - s] + 1);
				}	
				if (!busy_1) {
					dp[time][1][s] = dp[time - 1][1][s - 1];
					dp[time][1][s] = min(dp[time][1][s], dp[time - 1][0][time - s] + 1);
				}
			}
		}
		
		cerr << dp[DAY][0][720] << " " << dp[DAY][1][720] << endl;
		int answer0 = dp[DAY][0][720] + (dp[DAY][0][720] % 2);
		int answer1 = dp[DAY][1][720] + (dp[DAY][1][720] % 2);
		case_print();
		cout << min(answer0, answer1) << endl;
	}
	
	return 0;
}
