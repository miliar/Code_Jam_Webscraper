#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

const int MM = 1e9 + 7;
const double eps = 1e-8;
const int MAXN = 333 + 10;

int n, m;

void prework(){

}

void read(){

}

ll e[MAXN], s[MAXN];
ll a[MAXN][MAXN], b[MAXN][MAXN];

double c[MAXN][MAXN];
const ll INF = 1ll << 60;

double ans[MAXN];

void solve(int casi){
	cout << "Case #" << casi << ": ";
	int Q;
	cin>>n>>Q;
	for(int i = 1; i <= n; i++){
		scanf("%lld%lld", &e[i], &s[i]);
	}
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			scanf("%lld", &a[i][j]);
			b[i][j] = a[i][j] == -1 ? INF : a[i][j];
		}
	}
	
	for(int k = 1; k <= n; k++)
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
				b[i][j] = min(b[i][k] + b[k][j], b[i][j]);
	
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++)
			if (i != j){
				if (b[i][j] <= e[i]){
					c[i][j] = b[i][j] * 1.0 / s[i];
				}
				else
					c[i][j] = 1e200;
			}
	
	for(int k = 1; k <= n; k++)
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
				c[i][j] = min(c[i][k] + c[k][j], c[i][j]);
	
	
	for(int i = 1; i <= Q; i++){
		int st, ed;
		scanf("%d%d", &st, &ed);
		printf("%.16f%c", c[st][ed], " \n"[i == Q]);
	}
	/*
	for(int i = 1; i <= n; i++)
		ans[i] = 1e200;
	ans[1] = 0;
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= i; j++){
			for(int k = i + 1, d = a[i][i+1]; k <= n && d <= e[i]; d += a[k][k + 1], k++){
				ans[k] = min(ans[k], ans[i] + d * 1.0 / s[i]);
			}
		}
	printf("%.16f\n", ans[n]);
	*/
}

void printans(){

}


int main(){
	//std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin>>T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}

