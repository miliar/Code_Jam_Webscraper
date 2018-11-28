#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>

using namespace std;
typedef long long ll;
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) x.begin(), x.end()
typedef pair<int, int> pii;
typedef tuple<int, int, int> t3;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef tuple<int, int, int, int> t4;

int d3[110][110], d4[102][102][102];

void solve(){
	int n, p, g[110];
	scanf("%d%d", &n, &p);
	rep(i, n)scanf("%d", g+i);
	int A[4] = {};
	rep(i, n)A[g[i] % p]++;
	
	if(A[0] == n){
		printf("%d\n", n);
		return;
	}
	
	if(p == 2){
		printf("%d\n", A[0] + 1 + (A[1] - 1) / 2);
	}
	else if(p == 3){
		for(int i=0;i<=100;i++)for(int j=0;j<=100;j++){
			d3[i][j] = 0;
			if(i || j)d3[i][j] = 1;
			if(i >= 3)d3[i][j] = max(d3[i-3][j] + 1, d3[i][j]);
			if(j >= 3)d3[i][j] = max(d3[i][j], d3[i][j-3] + 1);
			if(i >= 1 && j >= 1)d3[i][j] = max(d3[i][j], d3[i-1][j-1] + 1);
		}
		printf("%d\n", A[0] + d3[A[1]][A[2]]);
	}
	else{
		for(int i=0;i<=100;i++)for(int j=0;j<=100;j++)for(int k=0;k<=100;k++){
			d4[i][j][k] = 0;
			if(i || j || k) d4[i][j][k] = 1;
			int &a = d4[i][j][k];
			if(i >= 4) a = max(a, d4[i-4][j][k] + 1);
			if(j >= 4) a = max(a, d4[i][j-4][k] + 1);
			if(k >= 4) a = max(a, d4[i][j][k-4] + 1);
			if(i >= 1 && k >= 1) a = max(a, d4[i-1][j][k-1] + 1);
			if(i >= 2 && j >= 1) a = max(a, d4[i-2][j-1][j] + 1);
			if(k >= 2 && j >= 1) a = max(a, d4[i][j-1][k-2] + 1);
		}
		printf("%d\n", A[0] + d4[A[1]][A[2]][A[3]]);
	}
}

int main(){
	int Tc = 1; scanf("%d", &Tc);
	for(int tc=1; tc<=Tc; tc++){
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}

