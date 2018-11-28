// gcj Pony Express.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<queue>
using namespace std;
typedef long long ll;
int t;
int n;
const int MAXN = 1e2 + 10;
const double INFD = 1e200;
const double tinf = 1e180;
const ll INF = 0x3f3f3f3f3f3f3f3f;
ll g[MAXN][MAXN];
double tt[MAXN][MAXN];
int vis[MAXN];
double time[MAXN];
void spfa(int st){
	for (int i = 1; i <= n; ++i){
		time[i] = INFD;
	}
	queue<int> tq;
	memset(vis, 0, sizeof vis);
	tq.push(st);
	time[st] = 0;
	while (!tq.empty()){
		int u = tq.front();
		tq.pop();
		vis[u] = 0;
		for (int i = 1; i <= n; ++i){
			if (i == u)continue;
			if (tt[u][i] < tinf){
				if (tt[u][i] + time[u] < time[i]){
					time[i] = tt[u][i] + time[u];
					if (!vis[i]){
						vis[i] = 1;
						tq.push(i);
					}
				}
			}
		}
	}
}
ll si[MAXN];
ll ei[MAXN];
int main(){
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	cin >> t;
	int kase = 0;
	while (t--){
		++kase;
		int q;
		cin >> n;
		cin >> q;
		for (int i = 1; i <= n; ++i){
			cin >> ei[i] >> si[i];
		}
		for (int i = 1; i <= n; ++i){
			for (int j = 1; j <= n; ++j){
				cin >> g[i][j];
				if (g[i][j] == -1)g[i][j] = INF;
			}
		}
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (g[i][j] > g[i][k] + g[k][j])
						g[i][j] = g[i][k] + g[k][j];
		for (int i = 1; i <= n; ++i){
			for (int j = 1; j <= n; ++j){
				tt[i][j] = INFD;
				if (g[i][j] <= ei[i]){
					tt[i][j] = g[i][j] * 1.0 / si[i];
				}
			}
		}
		printf("Case #%d:", kase);
		while (q--){
			int st, ed;
			cin >> st >> ed;
			spfa(st);
			cout << " ";
			printf("%.8f", time[ed]);
		}
		cout << endl;
	}
	return 0;
}
