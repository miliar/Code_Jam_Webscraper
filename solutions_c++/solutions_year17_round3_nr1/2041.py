#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
#define ALL(A) A.begin(), A.end()

using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<double,double> DD;
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; ++t){
		int N, K; cin >> N >> K;
		vector<P> RH(N);
		rep (i, N){
			cin >> RH[i].first >> RH[i].second;
		} // end rep
		double res = 0.;
		for (int i = 0; i < (1<<N); ++i){
			vector<int> used; used.clear();
			for (int j = 0; j < N; ++j){
				if (i & (1<<j)){
					used.push_back(j);
				} // end if
			} // end for
			if (used.size() == K){
				double area = 0.;
				vector<P> curr; curr.clear();
				set<int> sameR; sameR.clear();
				for (int j = 0; j < K; ++j){
					curr.push_back(RH[used[j]]);
					sameR.insert(RH[used[j]].first);
				} // end for
			
				sort(ALL(curr));
				rep (j, K){
					area += 2. * M_PI * (curr[j].first) * (curr[j].second); // side area
				
				} // end rep
				int maxR = 0;
				set<int>::iterator it = sameR.begin();
				for (; it != sameR.end(); ++it){
					maxR = max(maxR, (*it));
				} // end for
				area += (double)maxR * maxR * M_PI;
				res = max(res, area);
			} // end if
		} // end for
		printf("Case #%d: %.6lf\n", t, res);
	} // end for
					
	return 0;
}
