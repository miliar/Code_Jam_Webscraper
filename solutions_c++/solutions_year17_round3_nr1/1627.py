#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
# define M_PI           3.14159265358979323846  /* pi */
int main(){
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		int N, K;
		double maxS = 0, rhSum = 0;
		cin >> N >> K;
		vector<pair<double, double> > ps(N);
		multiset<double> maxRH;
		for (int i = 0; i < N; i++) cin >> ps[i].first >> ps[i].second;
		sort(ps.begin(), ps.end());
		for (int i = 0; i < N; i++){
			double csum = ps[i].first*ps[i].first + rhSum, crh = 2 * ps[i].first*ps[i].second;
			csum += crh;
			rhSum += crh;
			if (maxRH.size() == K) csum -= *maxRH.begin();
			maxRH.insert(crh);
			if (maxRH.size() == K + 1){
				rhSum -= *maxRH.begin();
				maxRH.erase(maxRH.begin());
			}
			maxS = max(maxS, csum);
		}
		double ans = maxS*M_PI;
		cout << "Case #" << t + 1 << ": " << fixed << ans << endl;
	}
	int de;
	cin >> de;
}