#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

double tim[105];
int g[105][105];
int e[105], s[105];
int inq[105];
int n;
int vis[105];

void dfs(int cur, int dis, double newtime, double speed, queue<int>&q){
	for(int i = 0; i < n; i++){
		// if(cur == 0 && i == 1)
		// 	cout << g[cur][i] << endl;
		if(g[cur][i] != -1 && g[cur][i] <= dis){
			// if(tim[i] > newtime + g[cur][i] * 1.0 / speed){
			if(!vis[i]){
				vis[i] = 1;
				if(tim[i] > newtime + g[cur][i] * 1.0 / speed){
					tim[i] = newtime + g[cur][i] * 1.0 / speed;
					if(!inq[i])
						q.push(i);
				}
				dfs(i, dis - g[cur][i], newtime + g[cur][i] * 1.0 / speed, speed, q);
			}
		}
	}
}

double get(int f, int t){
	for(int i = 0 ; i < n; i++)
		tim[i] = 1e33, inq[i] = 0;
	tim[f] = 0;
	inq[f] = 1;
	queue<int>q;
	q.push(f);
	while(!q.empty()){
		int cur = q.front();
		inq[cur] = 0;
		q.pop();
		// cout << cur << endl;
		for(int i = 0 ; i < n; i++)
			vis[i] = 0;
		vis[cur] = 1;
		dfs(cur, e[cur], tim[cur], s[cur], q);
	}
	return tim[t];
}

int main(){
	int T;
	cin >> T;
	for(int _t = 1; _t <= T; _t++){
		printf("Case #%d:", _t);
		int q;
		cin >> n >> q;
		for(int i =0 ; i < n; i++)
			cin >> e[i] >> s[i];
		for(int i =0 ; i < n; i++)
			for(int j=0;j<n;j++)
				cin >> g[i][j];
		for(int i = 0; i < q; i++){
			int f, t;
			cin >> f >> t;
			printf(" %lf", get(f-1,t-1));
		}
		cout << endl;
	}
	return 0;
}