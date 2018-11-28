#include <bits/stdc++.h>

using namespace std;


int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int N;
		long long D;
		cin >> D >> N;
		pair<long long, int> horses[N];
		for(int i=0; i<N; i++){
			cin >> horses[i].first >> horses[i].second;
		}
		sort(horses, horses+N);
		reverse(horses, horses+N);

		double in_time = (D - horses[0].first) / ((double) horses[0].second);
		for(int i=1; i<N; i++){
			double new_time = (D - horses[i].first) / ((double) horses[i].second);
			in_time = max(new_time, in_time);
		}
		double vel = D/in_time;
		cout << "Case #" << t << ": " << setprecision(7) << fixed << vel << endl;
	}

	return 0;
}

