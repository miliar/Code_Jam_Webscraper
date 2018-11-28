#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<LL, double> PII;
typedef set<int>::iterator SIT; 

const int maxn = 105;

int n, p, a[maxn], tt;
int rc[][3] = {
	{1, 0, 1},
	{2, 1, 0},
	{4, 0, 0},
	{0, 2, 0},
	{0, 1, 2},
	{0, 0, 4},
};

void dfs(int idx, int *tot, int sum){
	if(idx == 6){
		tt = max(tt, sum + 1);
		return;
	}
	for(int i = 0; ; ++i){
		int x = rc[idx][0] * i;
		int y = rc[idx][1] * i;
		int z = rc[idx][2] * i;
		if(x > tot[0] || y > tot[1] || z > tot[2]) break;
		tot[0] -= x;
		tot[1] -= y;
		tot[2] -= z;
		dfs(idx + 1, tot, sum + i);
		tot[0] += x;
		tot[1] += y;
		tot[2] += z;
	}
}

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cases = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &n, &p);
		for(int i = 0; i < n; ++i) scanf("%d", &a[i]);
		int ans = 0;
		if(p == 2){
			int cnt = 0;
			for(int i = 0; i < n; ++i){
				cnt += (a[i] & 1);
			}
			ans = n - (cnt >> 1);
		}
		else if(p == 3){
			int c1 = 0, c2 = 0;
			for(int i = 0; i < n; ++i){
				if(a[i] % 3 == 1) ++c1;
				else if(a[i] % 3 == 2) ++c2;
			}
			ans = n - c1 - c2 + min(c1, c2) + (abs(c1 - c2) + 2) / 3; 
		}
		else if(p == 4){
			int c[3] = {0};
			for(int i = 0; i < n; ++i){
				if(a[i] % 4){
					c[a[i] % 4 - 1]++;
				}
				else{
					++ans;
				}
			}
			tt = 0;
			dfs(0, c, 0);
			ans += tt;
		}
		printf("Case #%d: %d\n", ++cases, ans);
	}
	return 0;
} 
