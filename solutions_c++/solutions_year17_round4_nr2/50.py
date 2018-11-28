#include<stdio.h>
#include<assert.h>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;

const double EPS = 1e-8;
const double PI = acos(-1);

int solve();

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
}

const int MX = 1005;

int solve()
{
	int N, M, C;
	scanf("%d%d%d", &N, &C, &M);
	int c1[MX] = {}, c2[MX] = {};
	for(int i = 1; i <= M; i++){
		int a, b;
		scanf("%d%d", &a, &b);
		c1[a]++, c2[b]++;
	}
	int mx = 0, t = 0, mv = 0;
	for(int i = 1; i <= N; i++){
		t += c1[i];
		mx = max(mx, (t+i-1)/i);
	}
	for(int i = 1; i <= C; i++) mx = max(mx, c2[i]);
	for(int i = 1; i <= N; i++) mv += (c1[i] - mx) > 0? c1[i]-mx : 0;

	printf("%d %d\n", mx, mv);
}
