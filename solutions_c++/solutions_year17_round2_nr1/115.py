#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	int tc;
	cin >> tc;
	for(int ti = 1; ti <= tc; ++ti) {
		int N;
		double D;
		cin >> D >> N;
		double time = 0.0;
		for(int i = 0; i < N; ++i) {
			double K, S;
			cin >> K >> S;
			time = max(time, (D - K) / S);
		}
		
		cout << "Case #" << ti << ": " << setprecision(20) << D / time << "\n";
	}
	
	return 0;
}
