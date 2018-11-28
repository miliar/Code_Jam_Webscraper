#include"stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<assert.h>
#include<ctime>
#include<queue>
#include<fstream>
#include<string>
using namespace std;

const int maxn = 110;
int dis[maxn][maxn];
int md[maxn];
long long speed[maxn];
double dp[maxn][maxn];
const double inf = 1e18;
long long preS[maxn];

void solve(int n){
	for (int i = 0; i < n; i++) fill(dp[i], dp[i] + n + 1, inf);
	dp[0][0] = 0;
	preS[0] = 0;
	for (int i = 0; i < n-1; i++){
		preS[i + 1] = preS[i] + dis[i][i + 1];
	}

	for (int i = 1; i < n; i++){
		for (int j = 0; j < i; j++){
			if (md[j] >= preS[i] - preS[j]){
				dp[i][j] = min(dp[i][j], dp[j][j] + (preS[i] - preS[j])*1.0 / speed[j]);
				dp[i][i] = min(dp[i][i], dp[i][j]);
				//cout << i << " " << j << " " << dp[i][j] << endl;
			}
		}
	}
}



int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("C-small-attempt1.in");
	fin >> t;
	ofstream fout;
	fout.open("3.out");
	fout.precision(20);
	fout.setf(ios::fixed);

	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";

		int n, q;
		fin >> n >> q;
		for (int i = 0; i < n; i++){
			fin >> md[i] >> speed[i];
		}
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++) fin >> dis[i][j];
		}
		for (int i = 0; i < q; i++){
			int u, v;
			fin >> u >> v;
		}
		solve(n);
		fout << dp[n - 1][n - 1] << endl;

	}
	system("Pause");
	return 0;
}
