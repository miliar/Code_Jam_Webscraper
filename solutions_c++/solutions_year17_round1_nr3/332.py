#include <bits/stdc++.h> // PLEASE

using namespace std;
typedef long long ll;
typedef pair <int, int> pp;
#define MAXN 200005
#define MAXM 1005
#define MAXP 25
#define INF 20000
#define HAX 10000000 
#define A first
#define B second
#define MP make_pair
#define PB push_back
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define re(i, n) FOR(i, 1, n)
#define rep(i, n) for(int i = 0; i<(n); ++i)
#define fore(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
int N, K;
int H1, A1, H2, A2, B, D;
int tmpH1;
int tmpA1;
int tmpH2;
int tmpA2;
int tmpB;
int tmpD;
int c = 0;
bool go(int V)
{
	int M1 = 0;
	int M2 = 0;
	if(B != 0) {
		M1 = (H2-A1)/B;
		M1++;
	}
	if(M1 < 0) M1 = 0;
	if(D != 0) M2 = A2/D;
	M2++;
	for(int i=0; i<=M1; i++) {
		for(int j=0; j<=M2; j++) {
			int cntB = 0;
			int cntD = 0;
			H1 = tmpH1;
			A1 = tmpA1;
			H2 = tmpH2;
			A2 = tmpA2;
			B = tmpB;
			D = tmpD;
			for(int t=1; t<=V; t++) {
				if(H1 <= 0) break;
				if(H2-A1 <= 0) {
					H2 -= A1;
					break;
				} 
				if(H1-A2 <= 0) {
					if(cntD < j) {
						if(H1-(max(0, A2-D)) > 0) {
							cntD++;
							A2 -= D;
							A2 = max(A2, 0);
							H1 -= A2;
							continue;
						}
						else {
							H1 = tmpH1;
							H1 -= A2;
							continue;
						}
					}
					else {
						H1 = tmpH1;
						H1 -= A2;
						continue;
					}
				}
				else if(H1-A2 > 0) {
					if(cntD < j) {
						cntD++;	
						A2 -= D;
						A2 = max(A2, 0);
						H1 -= A2;
						continue;
					}
					if(cntB < i) {
						cntB++;
						A1 += B;			
						H1 -= A2;
						continue;
					}
					H1 -= A2;
					H2 -= A1;
					if(H2 <= 0) return true;
				}
			}
			if(H1 > 0) if(H2 <= 0) return true;
		}
	}
	return false;
	
}	
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> H1 >> A1 >> H2 >> A2 >> B >> D;
		c = 0;
		int l = 1;
		int r = INF;
		int ans = INF;
		tmpH1 = H1;
		tmpA1 = A1;
		tmpH2 = H2;
		tmpA2 = A2;
		tmpB = B;
		tmpD = D;
		while(l <= r) {
			H1 = tmpH1;
			A1 = tmpA1;
			H2 = tmpH2;
			A2 = tmpA2;
			B = tmpB;
			D = tmpD;
			int md = (l+r)/2;
			if(go(md)) {
				r = md-1;
				ans = min(ans, md);
			}
			else l=md+1;
		}
		if(ans != INF) printf("Case #%d: %d\n", t, ans);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
   
}
