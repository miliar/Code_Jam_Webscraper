#include <bits/stdc++.h>

#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef long long ll;

int minute[1445];
int dp[1445][725][2][2];
int mark[1445][725][2][2];
int pass;

int f(int t, int m1, int m2, int player, int start){
	if(t == 1440){
		return start != player;
	}
	if(mark[t][m1][player][start] == pass)
		return dp[t][m1][player][start];

	int ret = 1e9;
	mark[t][m1][player][start] = pass;
	if(minute[t] == player){
		if(player == 1){
			if(m2 == 720) return dp[t][m1][player][start] = 1e9;
			return dp[t][m1][player][start] = f(t+1,m1,m2+1,2,start)+1;
		}
		if(m1 == 720) return dp[t][m1][player][start] = 1e9;
		else return dp[t][m1][player][start] = f(t+1,m1+1,m2,1,start)+1;
	}

	if(player == 1){
		if(m1 == 720){
			if(minute[t] == 2) return dp[t][m1][player][start] = 1e9;
			return dp[t][m1][player][start] = f(t+1,m1,m2+1,2,start)+1;
		}
		if(m2 == 720 || minute[t] == 2) return dp[t][m1][player][start] = f(t+1,m1+1,m2,1,start);
		ret = min(f(t+1,m1+1,m2,1,start), f(t+1,m1,m2+1,2,start) + 1);
		return dp[t][m1][player][start] = ret;
	}

	if(m2 == 720){
		if(minute[t] == 1) return dp[t][m1][player][start] = 1e9;
		return dp[t][m1][player][start] = f(t+1,m1+1,m2,1,start)+1;
	}
	if(m1 == 720 || minute[t] == 1) return dp[t][m1][player][start] = f(t+1,m1,m2+1,2,start);
	ret = min(f(t+1,m1+1,m2,1,start)+1, f(t+1,m1,m2+1,2,start));
	return dp[t][m1][player][start] = ret;
}

int main(){
	int T;

	scanf("%d", &T);

	for(int t = 1; t <= T; t++){
		pass++;
		int c,j,st,ed;

		scanf("%d%d", &c,&j);
		memset(minute,0,sizeof minute);

		for(int i = 0; i < c; i++){
			scanf("%d%d", &st, &ed);
			for(int k = st; k < ed; k++)
				minute[k] = 1;
		}

		for(int i = c; i < c+j; i++){
			scanf("%d%d", &st, &ed);
			for(int k = st; k < ed; k++)
				minute[k] = 2;
		}

		int ans = 1e9;
		if(minute[0] != 1) ans = f(0,0,0,1,1);
		if(minute[0] != 2) ans = min(ans,f(0,0,0,2,2));
		// if(minute[1] != 2) ans = min(ans,f(1,0,0,2));

		printf("Case #%d: %d\n",t,ans);
	}
	
	return 0;
}