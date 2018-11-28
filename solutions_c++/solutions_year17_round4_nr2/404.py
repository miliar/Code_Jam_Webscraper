										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL
#define NN 1010

int n, m, c;
int cnt[1010];
int per[1010];

int main(){
	std::ios::sync_with_stdio(false);
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		memset(cnt, 0, sizeof cnt);
		memset(per, 0, sizeof per);

		cin >> n >> c >> m;
		cerr << n << ' ' << c << ' ' << m << endl;
		int p, b;
		for(int i = 0; i < m; i++){
			cin >> p >> b;
			cnt[p]++;
			per[b]++;
		}

		int k = 0, tot = 0;
		for(int i = 1; i <= c; i++)
			k = max(k, per[i]);

		for(int i = 1; i <= n; i++){
			tot += cnt[i];
			k = max(k, (tot + i - 1) / i);
		}

		int opp = 0;
		for(int i = 1; i <= n; i++)
			opp += max(0, cnt[i] - k);
		cout << "Case #" << ++test << ": " << k << ' ' << opp << endl;
	}
	return 0;
}
