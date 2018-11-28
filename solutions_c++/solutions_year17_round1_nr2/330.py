#include <bits/stdc++.h> // PLEASE

using namespace std;
typedef long long ll;
typedef pair <int, int> pp;
#define MAXN 55
#define MAXM 1005
#define MAXP 25
#define MAXV 1000005
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
int X[MAXN];
int Y[MAXN][MAXN];
int cnt[MAXN];
int tmp[MAXN];
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> N >> P;
		for(int i=1; i<=N; i++) cnt[i] = 1;
		for(int i=1; i<=N; i++) cin >> X[i];
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=P; j++) cin >> Y[i][j];
			sort(Y[i]+1, Y[i]+P+1);
		}
		int ans = 0;
		for(ll k=1; k<=MAXV; k++) {
			bool f = 0;
			while(f == 0) {
			for(int i=1; i<=N; i++) tmp[i] = cnt[i];
			for(int i=1; i<=N; i++) {
				if(cnt[i] > P) {
					f = 1;
					break;
				}
				int tmp1 = cnt[i];
				while((ll)((ll)(9*X[i])*k) > (ll)(10*Y[i][cnt[i]])) {
					cnt[i]++;
					if(cnt[i] > P) break;
				}
				if(cnt[i] <= P) {
					if((ll)((ll)(11*X[i])*k) >= (ll)(10*Y[i][cnt[i]])) {
						cnt[i]++;
					}
					else {
						f = 1;
						cnt[i] = tmp1;
					}
				}
				else {
					f = 1;
					cnt[i] = tmp1;
				}
			}
			if(f == 0) {
				ans++;
			}
			else for(int i=1; i<=N; i++) cnt[i] = tmp[i];
			}
		}

		printf("Case #%d: %d\n", t, ans);
		
	}
   
}
