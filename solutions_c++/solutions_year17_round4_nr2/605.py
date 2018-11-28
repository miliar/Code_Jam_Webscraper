#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <queue>
#include <map>
#include <stack>
#include <set>
#define maxn 1009
#define maxm 100000
using namespace std;
int n, C, m;
vector<int>G[maxn];
int cnt[maxn];
set<int>st;
int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round2/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round2/A.out", "w", stdout);
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		cin >> n >> C >> m;
		for(int i = 1; i <= n; i++)
			G[i].clear();
		memset(cnt, 0, sizeof(cnt));
		for(int i = 1; i <= m; i++){
			int p, c;
			cin >> p >> c;
			G[p].push_back(c);
			cnt[c]++;
		}
		int ans = 0;
		for(int i = 1; i <= C; i++)
			ans = max(ans, cnt[i]);
		//st.clear();
		for(int i = 1; i <= n; i++){
			//for(auto x: G[i])
				//st.insert(x);
			int sz = G[i].size();
			ans = max(ans, (sz + i - 1) / i);
		}
		int num = 0;
		for(int i = 1; i <= n; i++){
			int sz = G[i].size();
			int cur = max(0, sz - ans);
			num += cur;
		}
		printf("Case #%d: %d %d\n", cot++, ans, num);
	}
	return 0;
}