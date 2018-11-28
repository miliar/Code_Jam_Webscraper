#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

vector<int> v[2000];
int cnt[2000];

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; ++cc){
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; i < 1000; ++i) v[i].clear();
		int n, c, m;
		scanf("%d%d%d", &n, &c, &m);
		int ans = 0;
		for(int i = 0; i < m; ++i){
			int x, y;
			scanf("%d%d", &x, &y);
			x--;
			y--;
			v[y].push_back(x);
			cnt[x]++;
		}
		for(int i = 0; i < c; ++i){
			ans = max(ans, (int)v[i].size());
		}
		int tot = 0;
		for(int i = 0; i < n; ++i){
			tot += cnt[i];
			if(tot) ans = max(ans, (tot - 1) / (i + 1) + 1);
		}
		tot = 0;
		int ans2 = 0;
		for(int i = 0; i < n; ++i){
			if(cnt[i] > ans) ans2 += cnt[i] - ans;
		}
		printf("Case #%d: %d %d\n", cc, ans, ans2);
	}
	return 0;
}

