#include <bits/stdc++.h>
#define MAX 100001
#define ll long long
#define M 1000000007
#define INF 1000000000000000
#define PI 3.14159265358979323
using namespace std;

int n,k;
struct node{
	long double r,h;
}a[MAX];

bool operator <(node x,node y){
	return x.r>y.r;
}

long double dp[1001][1001];

long double DP(int i,int left){
	if (!left) return 0;
	if (i==n) return -INF;
	if (dp[i][left]) return dp[i][left];
	dp[i][left] = DP(i+1,left);
	if (left==k){
		dp[i][left] = max(dp[i][left],PI*a[i].r*a[i].r+2*PI*a[i].r*a[i].h+DP(i+1,left-1));
	}
	else dp[i][left] = max(dp[i][left],2*PI*a[i].r*a[i].h+DP(i+1,left-1));
	return dp[i][left];
}

int main(){
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int t,cs = 1;
	cin >> t;
	while(t--){

		cin >> n >> k;
		for (int i=0;i<n;i++) cin >> a[i].r >> a[i].h;
		sort(a,a+n);
		cout << "Case #" << cs++ << ": ";
		printf("%.10Lf\n",DP(0,k));
		for (int i=0;i<=1000;i++){
			for (int j=0;j<=1000;j++) dp[i][j] = 0;
		}
	}
	return 0;
}