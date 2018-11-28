#include<bits/stdc++.h>

#define PB push_back
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(), (c).end()
#define CONTAINS(c, x) ((c).find(x) != (c).end())
#define REP(i, n) for(int i=1; i<=n; i++)
#define WAIT cout<<flush, system("PAUSE");
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<pii, int> ppi;
const int MAX = 1100;

int T, N, C;
bool A[MAX];
ppi sol;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	REP(tc, T){
		cin >> N >> C;
		memset(A, 0, sizeof(A));
		
		REP(c, C){
			sol = ppi( pii(-1, -1), 0);
			REP(I, N) if (!A[I]) {
				int tl = 0;
				int tr = N+1;
				REP(K, I-1) if (A[K])
					tl = max(tl, K);
				REP(K, N) if (A[K] && K>I)
					tr = min(tr, K);
					
				tl = I-tl-1;
				tr = tr-I-1;
				if (tr < tl) swap(tl, tr);
				
				sol = max(sol, ppi( pii(tl, tr), -I));
			}
			A[-sol.second] = true;
		}
		
		cout << "Case #" << tc << ": ";
		cout << sol.first.second << " " << sol.first.first << "\n";
	}
}

















