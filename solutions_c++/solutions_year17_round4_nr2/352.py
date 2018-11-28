#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

const int MM = 1e9 + 7;
const double eps = 1e-8;
const int MAXN = 2e6 + 10;

int n, m;

void prework(){

}

void read(){

}

int C;
vector<int> f[MAXN];

int cnt[MAXN];

int check(int k){
	for(int i = 1; i <= n; i++)
		cnt[i] = k;
	cnt[0] = m + 1;
	for(int i = 1; i <= C; i++){
		int now = n;
		for(int j = (int)(f[i].size()) - 1; j >= 0; j--){
			now = min(now, f[i][j]);
			while(cnt[now] == 0)
				now--;
			if (now == 0)
				return 0;
			cnt[now]--;
		}
	}
	return 1;
}

int g[MAXN];

void solve(int casi){
	cout << "Case #" << casi << ": ";
	cin >> n >> C >> m;
	for(int i = 1; i <= n; i++)
		g[i] = 0;
	for(int i = 1; i <= C; i++)
		f[i].clear();
	for(int i = 1; i <= m; i++){
		int x, y;
		cin >> x >> y;
		f[y].push_back(x);
		g[x]++;
	}
	for(int i = 1; i <= C; i++)
		sort(f[i].begin(), f[i].end());
	int l = 0, r = m, mid;
	for(int i = 1; i <= C; i++)
		l = max((int)f[i].size(), l);
	l--;
	while(l + 1 < r){
		mid = (l + r) / 2;
		if (check(mid))
			r = mid;
		else
			l = mid;
	}
	int ans1 = r, ans2 = 0;
	for(int i = 1; i <= n; i++)
		ans2 += max(0, g[i] - ans1);
	cout << ans1 << ' ' << ans2 << endl;
}

void printans(){

}

int main(){
	std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin >> T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}

