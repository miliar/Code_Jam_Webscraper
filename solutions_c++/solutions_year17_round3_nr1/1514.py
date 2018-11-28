#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
using namespace std;
const int MaxN = 1e3;
const double eps = 1e-6;
const double PI = 3.1415926535898;
int n, k, T;
struct NODE{
	double r, h;
}box[MaxN + 5];
double dp[MaxN + 5][MaxN + 5];
bool cmp(NODE x, NODE y){
	if(fabs(x.r - y.r) <= eps) return x.h > y.h;
	else return x.r > y.r;
}
int main(){
	//freopen("A-small-attempt0.in.txt", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("gcj1c-A-large.in.txt", "r", stdin);
	freopen("gcj1c-A-large.out", "w", stdout);
	scanf("%d", &T);
	int Case = 0;
	while(T--){
		scanf("%d %d", &n, &k);
		memset(dp, 0, sizeof(dp));
		for(int i = 1; i <= n; i++)
			scanf("%lf %lf", &box[i].r, &box[i].h);
		sort(box + 1, box + 1 + n, cmp);
		for(int i = 1; i <= n; i++){
			for(int j  = 1; j <= i; j++){
				double s = PI * box[j].r * box[j].r + 2 * PI * box[j].r * box[j].h;
				dp[i][1] = max(dp[i][1], s);
			}
			for(int j = i; j > 1; j--){
				dp[i][j] = max((dp[i - 1][j - 1] + 2 * PI * box[i].h * box[i].r), dp[i - 1][j]);
			}
		}
		printf("Case #%d: ", ++Case);
		printf("%.9lf\n", dp[n][k]);
	}
	return 0;
}

