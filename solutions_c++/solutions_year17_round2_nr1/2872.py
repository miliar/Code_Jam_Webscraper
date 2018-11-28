#include <iostream>
#include <cstdio>
using namespace std;

double horses[1001][2];

int main(){
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";

		int D, N;
		cin >> D >> N;

		for(int i = 1; i <= N; i++){
			cin >> horses[i][0] >> horses[i][1];
		}
		double max_time = 0.0;
		for(int i = 1; i <= N; i++){
			double time = (D - horses[i][0]) / horses[i][1];

			if(max_time < time)
				max_time = time;
		}
		double res = D / max_time;

		printf("%6f\n", res);
		// cout << res << endl;
	}
	return 0;
}