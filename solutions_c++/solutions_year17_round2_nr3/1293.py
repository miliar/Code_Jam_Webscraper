#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define reps(i,x,n) for(int i=x; i<(n); i++)
#define rrep(i,n) for(int i=(n)-1; i>=0; i--)
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second
#define pb push_back
#define eb emplace_back

using namespace std;
typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }

template<class A, size_t N, class T> void Fill(A (&a)[N], const T &v){ fill( (T*)a, (T*)(a+N), v ); }

const ll INF = 0x3fffffff;


int main(){
	//ios_base::sync_with_stdio(0);
	int T, ans=0;

	cin >> T;
	for(int kase=1; kase <= T; kase++){
		int N, Q, U[105], K[105];
		ll E[105], S[105], D[105][105];

		cin >> N >> Q;
		rep(i,N) cin >> E[i] >> S[i];
		rep(i,N) rep(j,N) cin >> D[i][j];
		rep(i,Q) cin >> U[i] >> K[i];

		double dp[105];
		Fill( dp, (double)1e18 );
		dp[0] = 0;
		rep(i,N){
			ll len = 0;
			rep(j,N-i) if(j){
				len += D[i+j-1][i+j];
				if( len > E[i] ) break;
				double tm = (double)len / (double)S[i];
				chmin( dp[i+j], dp[i] + tm );
			}
		}

		//rep(i,N) cout << dp[i] << " "; cout << endl;

		cout << "Case #" << kase << ": ";
		printf("%.9f\n", dp[N-1]);
	}

	return 0;
}
