#include <iostream>
#include <iomanip>
#include <vector>

#define INF 987654321987654321LL

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int it=1;it<=T;++it) {
		int n, q;
		cin >> n >> q;
		vector<long long> maxdist(n), speed(n);
		for (int i=0;i<n;++i) cin >> maxdist[i] >> speed[i];
		vector<vector<long long> > dist(n, vector<long long>(n));
		for (int i=0;i<n;++i) for (int j=0;j<n;++j) {
//			cout << i << " " << j << endl;
			cin >> dist[i][j];
			if (dist[i][j]==-1) dist[i][j]=INF;
		}

		/*for (int i=0;i<n;++i) {
			for (int j=0;j<n;++j) cout << dist[i][j] << " ";
			cout << endl;
		} cout << endl;*/


		for (int k=0;k<n;++k) for (int i=0;i<n;++i) for (int j=0;j<n;++j) if (dist[i][k] + dist[k][j] < dist[i][j]) dist[i][j] = dist[i][k] + dist[k][j];

		/*for (int i=0;i<n;++i) {
			for (int j=0;j<n;++j) cout << dist[i][j] << " ";
			cout << endl;
		} cout << endl;*/

		vector<vector<double> > dist2(n, vector<double>(n, (double) INF));



		for (int i=0;i<n;++i) for (int j=0;j<n;++j) if (dist[i][j]<=maxdist[i]) {
			dist2[i][j] = (double) dist[i][j]/speed[i];
		}

//		cout << "hej"; 

		for (int k=0;k<n;++k) for (int i=0;i<n;++i) for (int j=0;j<n;++j) if (dist2[i][k] + dist2[k][j] < dist2[i][j]) dist2[i][j] = dist2[i][k] + dist2[k][j];

		cout << "Case #" << it << ": ";
		while (q--) { 
			int u, v;
			cin >> u >> v;
			cout << setprecision(20) << dist2[u-1][v-1] << " ";
		}
		cout << endl;

	}
}