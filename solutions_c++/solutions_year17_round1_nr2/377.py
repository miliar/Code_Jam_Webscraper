#include <bits/stdc++.h>
using namespace std;

int T;

int N, P;

int main(){
	cin >> T;
	for (int q = 1; q<=T; q++){
		cout << "Case #" << q << ": ";

		cin >> N >> P;

		int a[1000];


		vector<pair<int,int> > v[100];

		int Q[100][100];

		for (int i = 0; i<N; i++){
			cin >> a[i];
		}


		for(int i = 0; i<N; i++){
			for (int j = 0; j<P; j++){
				cin >> Q[i][j];
				int kmax = floor((Q[i][j]*((double)10.0)/((double)9.0))/a[i]);
				int kmin = ceil((Q[i][j]*((double)10.0)/((double)11.0))/a[i]);
				//cout << Q[i][j] << " vs. " << a[i] << endl;
				//cout << "kmin, kmax = " << kmin << " " << kmax << endl;
				v[i].push_back(make_pair(kmin, kmax));
			}
			sort(v[i].begin(), v[i].end());
		}

		int idx[1000] = {0};
		int ans = 0;
		bool done = false;
		while(!done){
			//cout << "iteration: ";
			int kmin = 0;
			int kmax = 99999999;
			for(int i = 0; i<N; i++){ // find max kmin, and min kmax.
				kmin = max(kmin, v[i][idx[i]].first);
				kmax = min(kmax, v[i][idx[i]].second);
			}
			//cout << "kmin, kmax = " << kmin << " " << kmax << endl;

			if (kmin > kmax){
				for(int i = 0; i<N; i++){ // find max kmin, and min kmax.
					while (idx[i] < P && v[i][idx[i]].second < kmin) idx[i]++;
				}
			}
			else{
				for(int i = 0; i<N; i++) idx[i]++;
				ans++;
			}

			for (int i = 0; i<N; i++){
				if (idx[i]==P) done = true;
			}
		}

		cout << ans << endl;

	}
}