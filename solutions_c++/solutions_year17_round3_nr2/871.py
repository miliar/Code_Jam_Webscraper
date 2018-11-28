#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int N=1500;
int T, ac, aj;
int dp[N][N][2][2];
pii a[N], b[N];
int upd(int a, int b){
	if(a<0&&b<0)
		return a;
	if(a<0)
		return b;
	if(b<0)
		return a;
	return min(a, b);
}
int main() {
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=0; cas<T; cas++){
		scanf("%d%d", &ac, &aj);
		for(int i=0; i<ac; i++){
			int c, d;
			scanf("%d%d", &c, &d);
			a[i]=mp(c, d);
		}
		for(int i=0; i<aj; i++){
			int c, d;
			scanf("%d%d", &c, &d);
			b[i]=mp(c, d);
		}
		sort(a, a+ac);
		sort(b, b+aj);
		a[ac]=mp(1500, 1500);
		b[aj]=mp(1500, 1500);
		int p1=0, p2=0;
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				for(int k=0; k<2; k++)
					for(int l=0; l<2; l++)
						dp[i][j][k][l]=-2;

		dp[0][0][0][0]=dp[0][0][1][1]=0;
		for(int i=0; i<=1441; i++){
			for(int j=0; j<=min(i, 720); j++){
				while(p1<ac&&a[p1].se<i)p1++;
				while(p2<aj&&b[p2].se<i)p2++;
				if(i+1<=a[p1].fi||i+1>a[p1].se){
					dp[i+1][j+1][0][0]=upd(dp[i+1][j+1][0][0], dp[i][j][0][0]);
					dp[i+1][j+1][0][0]=upd(dp[i+1][j+1][0][0], dp[i][j][1][0]+1);
					dp[i+1][j+1][0][1]=upd(dp[i+1][j+1][0][1], dp[i][j][1][1]+1);
					dp[i+1][j+1][0][1]=upd(dp[i+1][j+1][0][1], dp[i][j][0][1]);
				}
				if(i+1<=b[p2].fi||i+1>b[p2].se){
					dp[i+1][j][1][0]=upd(dp[i+1][j][1][0], dp[i][j][0][0]+1);
					dp[i+1][j][1][0]=upd(dp[i+1][j][1][0], dp[i][j][1][0]);
					dp[i+1][j][1][1]=upd(dp[i+1][j][1][1], dp[i][j][1][1]);
					dp[i+1][j][1][1]=upd(dp[i+1][j][1][1], dp[i][j][0][1]+1);
				}
			}
		}
		printf("Case #%d: %d\n", cas+1, upd(upd(dp[1440][720][1][1], dp[1440][720][1][0]+1), upd(dp[1440][720][0][1]+1, dp[1440][720][0][0])));
	}
	return 0;
}
