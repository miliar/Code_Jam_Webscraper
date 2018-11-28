#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
	/* code */
	int T;
	cin >> T;
	cout.precision(6);
	cout << std::fixed;
	int D, N;
	int daCase = 0;
	while( daCase < T){
		
		++daCase;
		cout << "Case #" << daCase << ": ";
		cin >> D >> N;

		double t = 0;

		int si, ki;
		for(int i=0; i<N; ++i){
			cin >> ki >> si;

			t = max(t, (D-ki+0.0) / si);
		}
		
		double ans = D / t;

		cout << ans << endl;
		
	} 
	return 0;
}