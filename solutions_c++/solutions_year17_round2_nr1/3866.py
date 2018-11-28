#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
#define ALL(A) A.begin(), A.end()
#define EPS 1e-8

using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<double,double> DD;

vector<int> K, S;

double solve(int D, int N){
	double lo = 0.;
	double hi = (double)1e10;
	
	double res = 0.;
	int cnt = 100;
	double mid = 0.;
	bool ok = false;
	while(lo < hi && cnt--){
		mid = (lo + hi) / 2.;	// D 点まで行く時間
//		cerr << "mid: " << mid << endl;
		vector<DD> dist(N);
		ok = true;
		bool used[1005] = {false};
		rep (i, N){
			used[i] = true;
			dist[i].first = (double)K[i];
			dist[i].second = (double)K[i] + (double)S[i] * mid;
		} // end rep

		for (int i = 0; i < N; ++i){
			if (!used[i]) continue;
			for (int j = i + 1; j < N; ++j){
				if (!used[j]) continue;
				// j番目の馬が i番目の馬に追いついたので j番目の馬は使わない
//				if (dist[j].first < dist[i].first && dist[j].second > dist[i].second){
				if (abs(dist[j].first - dist[i].first) > EPS
				&& abs(dist[j].second - dist[i].second) > EPS){
					
					if (dist[j].first < dist[i].first && dist[j].second > dist[i].second){
						used[j] = false;
					} // end if
				} // end if
			} // end for
		} // end for
//		rep (i, N) cerr << (used[i] ? "used." : "not used.") << endl;
		
		rep (i, N){
			if (!used[i]) continue;
			if (abs(dist[i].second - (double)D) > EPS){
				// annie が追い越した
				if (dist[i].second < (double)D){
					lo = mid;	// 減速
					ok = false;
					break;
				} // end if
			} // end if
		} // end rep
		if (ok){
//			cerr << "res: " << res << endl;
			res = max(res, (double)D/mid);
			hi = mid;	// 加速
		} // end if
	} // end while
	if (!ok){
		res = max(res, (double)D/mid);
	} // end if

	return res;
}
	
double solve2(int D, int N){
	double res = 0.;
	if (N == 1){
//		double t = (double)(D - K[0]) / (double)S[0];
//		res = (double)D / (double)t;
		res = (double) D* S[0] / (double)(D - K[0]); 
	}else{
		res = solve(D,N);
	} // end if
	return res;
}
		
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; ++t){
		int D, N; cin >> D >> N;
		K.clear(); K.resize(N, 0);
		S.clear(); S.resize(N, 0);
		rep (i, N){
			cin >> K[i] >> S[i];
		} // end rep
		double res = solve2(D,N);
		printf("Case #%d: %.6lf\n", t, res);
	} // end for
	
	return 0;
}
