#include <bits/stdc++.h>

using namespace std;

#define FOE(i, s, t) for (int i = s; i <= t; i++)
#define FOD(i, s, t) for (int i = s; i >= t; i--)
#define FOR(i, s, t) for (int i = s; i < t; i++)
#define mp make_pair
#define pb push_back
#define LL long long

int t;

#define K 1201

pair<int, int> A[K];
int n, k;

double dp[K][K];

#define pi acos(-1.0)
double area(double r){
	return r * pi * r;
}

double cir_area(double r, double h){
	return 2 * r * pi * h;
}

double max(double a, double b){if (a>b) return a; return b;}


bool cmp(pair<int, int> a, pair<int, int> b){
	if (a.first == b.first) return a.second < b.second;
	return a.first > b.first;
}

void solve(){
	scanf("%d%d", &n, &k);
	FOE(i, 1, n) scanf("%d%d", &A[i].first, &A[i].second);
	sort(A + 1, A + n + 1, cmp);
	
	memset(dp, 0.00, sizeof(dp));

	double sol = 0.00;

	FOE(i, 1, n){
//		printf("parm %d %d\n", A[i].first, A[i].second);
		dp[i][1] = max(dp[i - 1][1], area(A[i].first) + cir_area(A[i].first, A[i].second));
		FOE(j, 2, k){
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + cir_area(A[i].first, A[i].second));
		}
//		printf("dp[%d][1] = %.9f %.9f\n", i, dp[i][1], cir_area(A[i].first, A[i].second));
		sol = max(sol, dp[i][k]);
	}
	printf("%.9f\n", sol);
}

int main(){
	scanf("%d", &t);
	FOE(i, 1, t){
		printf("Case #%d: ", i);
		solve();
	}
}
