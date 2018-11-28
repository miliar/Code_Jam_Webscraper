#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>

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
		int N, K;
		vector<pair<double,double>> v;
		v.emplace_back(0, 0);

		cin >> N >> K;
		rep(i,N){
			double R, H;
			cin >> R >> H;
			v.emplace_back(R, H);
		}
		sort( all(v) );

		double dp[1005][1005];  // N, K
		Fill( dp, (double)0 );
		rep(k,K) rep(i,N+1) rep(j,i){
			double sur = 2.0 * M_PI * v[i].X * v[i].Y;
			chmax( dp[i][k+1], dp[j][k] + sur );
		}

		double ans = 0;
		rep(i,N+1){
			double sur = v[i].X * v[i].X * M_PI;
			chmax(ans, dp[i][K] + sur);
		}

		cout << "Case #" << kase << ": ";
		printf("%.9f\n", ans );
	}

	return 0;
}
