#include <bits/stdc++.h> // PLEASE

using namespace std;
typedef long long ll;
typedef pair <int, int> pp;
#define MAXN 200005
#define MAXM 101
#define MAXP 25
#define INF 2000000000
#define HAX 10000000 
#define A first
#define B second
#define MP make_pair
#define PB push_back
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define re(i, n) FOR(i, 1, n)
#define rep(i, n) for(int i = 0; i<(n); ++i)
#define fore(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
int N, P;
int dp1[MAXM][MAXM][3];
int dp2[MAXM][MAXM][MAXM][4];
void print(int t, int x)
{
	printf("Case #%d: %d\n", t, x);
	return;
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> N >> P;
		vector <int> v;
		int ans = 0;
		int cnt[MAXP];
		memset(cnt, 0, sizeof(cnt));
		for(int i=0; i<N; i++) {
			int x;
			cin >> x;
			if((x%P) == 0) {
				ans++;
				continue;
			} 
			v.PB(x);
			cnt[x%P]++;
		}
		N = (int)v.size();
		if(N == 0) {
			print(t, ans);
			continue;
		}
		if(P == 2) {
			ans = ans + (N+1)/2;
			print(t, ans);
		}
		if(P == 3) {
			memset(dp1, 0, sizeof(dp1));
			dp1[0][0][0] = 0;
			for(int i=0; i<=cnt[1]; i++) {
				for(int j=0; j<=cnt[2]; j++) {
					for(int k=0; k<=2; k++) {
						int add = 0;
						if(k == 1) add = 1;
						if(i > 0) dp1[i][j][k] = max(dp1[i][j][k], dp1[i-1][j][(k-1+3)%3] + add);
						add = 0;
						if(k == 2) add = 1;
						if(j > 0) dp1[i][j][k] = max(dp1[i][j][k], dp1[i][j-1][(k-2+3)%3] + add);
					}
				}
			}
			int x = 0;
			for(int i=0; i<=2; i++) x = max(x, dp1[cnt[1]][cnt[2]][i]);
			print(t, ans+x);
		}
		if(P == 4) {
			memset(dp2, 0, sizeof(dp2));
			dp2[0][0][0][0] = 0;
			for(int i=0; i<=cnt[1]; i++) {
				for(int j=0; j<=cnt[2]; j++) {
					for(int k=0; k<=cnt[3]; k++) {
						for(int l=0; l<=3; l++) {
							int add = 0;
							if(l == 1) add = 1;
							if(i > 0) dp2[i][j][k][l] = max(dp2[i][j][k][l], dp2[i-1][j][k][(l-1+4)%4] + add);
							add = 0;
							if(l == 2) add = 1;
							if(j > 0) dp2[i][j][k][l] = max(dp2[i][j][k][l], dp2[i][j-1][k][(l-2+4)%4] + add);
							add = 0;
							if(l == 3) add = 1;
							if(k > 0) dp2[i][j][k][l] = max(dp2[i][j][k][l], dp2[i][j][k-1][(l-3+4)%4] + add);
						}
					}
				}
			}
			int x = 0;
			for(int i=0; i<=3; i++) x = max(x, dp2[cnt[1]][cnt[2]][cnt[3]][i]);
			print(t, ans+x);
		}
	}
   
}
