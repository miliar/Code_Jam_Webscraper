# include <bits/stdc++.h>

using namespace std;

int cnt[4];

int f[120][120][120];

int calc(int k) {
	memset(f, 0, sizeof(f));
	queue<tuple<int,int,int,int> > q;
	f[cnt[1]][cnt[2]][cnt[3]] = 0;
	q.push({cnt[1], cnt[2], cnt[3], 0});
	while(!q.empty()) {
		int x, y, z, s; 
		tie(x, y, z, s) = q.front(); q.pop();
		if(x)if(f[x-1][y][z]==0) q.push({x-1,y,z,(s+1)%k});
		if(y)if(f[x][y-1][z]==0) q.push({x,y-1,z,(s+2)%k});
		if(z)if(f[x][y][z-1]==0) q.push({x,y,z-1,(s+3)%k});
		if(x)f[x-1][y][z] = max(f[x-1][y][z], f[x][y][z] + (s==0));
		if(y)f[x][y-1][z] = max(f[x][y-1][z], f[x][y][z] + (s==0));
		if(z)f[x][y][z-1] = max(f[x][y][z-1], f[x][y][z] + (s==0));
	}
	return cnt[0] + f[0][0][0];
}

int main() {
	int cas = 0;
	int T; scanf("%d", &T);
	while(T--) {
		int n, k;
		scanf("%d%d", &n, &k);
		for(int i = 0; i < 4; ++i) cnt[i] = 0;
		for(int i = 0; i < n; ++i) {
			int x; scanf("%d", &x);
			cnt[x % k] += 1;
		}
		if(cnt[0] == n) {
			printf("Case #%d: %d\n", ++cas, n);
		} else {
			printf("Case #%d: %d\n", ++cas, calc(k));
		}
	}
	return 0;
}

