#include <bits/stdc++.h>
using namespace std;
#ifdef DEBUG
#include "debug.cpp"
// #include "testlib.h"
#else
#define deb(...)
#endif
#define X           first
#define Y           second
const double Pi   = acos(-1.0);//3.14159265358979323846;
const double Eps  = 1e-8;
const double Inf     = numeric_limits<double>::max();
const int Mod     = 1000000007;
template<typename T>
inline T Sqr(const T& x) { return x*x; }
// ----------

const size_t MaxN = 1000 + 10;
const size_t MaxK = MaxN;

int N, K;
double dp[MaxN][MaxK];
vector<pair<double, double>> p; // r, h

inline double cir_area(double r) {
	return Pi * r * r;
}

inline double side_area(double r, double h) {
	return 2 * Pi * r * h;
}

void build() {
	// initialization
	for(size_t i = 0; i < MaxN; ++i) fill(dp[i], dp[i]+MaxK, 0);
//	for(size_t i = 0; i < MaxN; ++i) {
//		dp[i][0] = -Inf;
//		for(size_t k = MaxK-1; k >= i+1; --k) dp[i][k] = -Inf;
//	}
	
	dp[0][1] = side_area(p[0].X, p[0].Y);
	for(int k = 1; k <= K; ++k) {
		double lft_max = dp[0][k-1];//, cur_max = dp[0][k];
		for(int i = 0; i < N; ++i) {
			if(i >= k-1)
				dp[i][k] = /*max(cur_max,*/ lft_max + side_area(p[i].X, p[i].Y);
//			cur_max = max(cur_max, dp[i][k]);
			lft_max = max(lft_max, dp[i][k-1]);
		}
	}
}
	

int main(int argc, char* argv[]) {
 	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;

	for(int tc = 1; tc <= T; ++tc) {
		//initialization
		p.clear();
		
		// input
		cin >> N >> K;
		for(int i = 0; i < N; ++i) {
			double r, h;
			cin >> r >> h;
			p.push_back({r, h});
		}
		sort(p.begin(), p.end());
		
		// main program
		build();
//		for(int i = 0; i < N; ++i)
//			for(int k = 0; k <= K; ++k)
//				cout << setprecision(9) << dp[i][k] << " \n"[k == K];

		// output
		double ans = -1;
		for(int i = 0; i < N; ++i) ans = max(ans, dp[i][K] + cir_area(p[i].X));
		cout << "Case #" << tc << ": ";
		cout << setprecision(15) << fixed << ans << endl;
	}

	return 0;
}
