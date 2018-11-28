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

int n, p;
int a[5];
int dp[110][110][110][5];

int mem(int x, int y, int z, int rem){
	if(x + y + z == 0)
		return 0;

	int &ref = dp[x][y][z][rem];
	if(ref != -1)
		return ref;
	
	ref = 0;
	if(x > 0)
		ref = max(ref, mem(x - 1, y, z, (rem + 3) % 4) + (rem == 0 ? 1 : 0));
	if(y > 0)
		ref = max(ref, mem(x, y - 1, z, (rem + 2) % 4) + (rem == 0 ? 1 : 0));
	if(z > 0)
		ref = max(ref, mem(x, y, z - 1, (rem + 1) % 4) + (rem == 0 ? 1 : 0));
	return ref;
}

int main(){
	std::ios::sync_with_stdio(false);
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> p;
		memset(a, 0, sizeof a);
		for(int i = 0; i < n; i++){
			int tmp;
			cin >> tmp;
			a[tmp % p]++;
		}
		int ans;
		if(p == 2)
			ans = a[0] + (a[1] + 1) / 2;
		if(p == 3){
			int mn = min(a[1], a[2]);
			ans = a[0] + mn + (max(a[1], a[2]) - mn + 2) / 3;
		}
		if(p == 4){
			int mn = min(a[1], a[3]);
			memset(dp, -1, sizeof dp);
			ans = a[0] + mem(a[1], a[2], a[3], 0);
		}
		cout << "Case #" << ++test << ": " << ans << endl;
	}
	return 0;
}
