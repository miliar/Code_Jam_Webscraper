#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int T, K, N;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		cin >> N >> K;
		
		priority_queue<int> intervals;
		intervals.push(N);
		
		int longest_interval;
		int l_s;
		int r_s;
		for (int k = 0; k < K; k++) {
			longest_interval = intervals.top();
			intervals.pop();
			l_s = longest_interval/2;
			if (longest_interval % 2 == 1) {
				r_s = longest_interval/2;
			}
			else {
				r_s = longest_interval/2 - 1;
			}
			
			if (l_s > 0) {
				intervals.push(l_s);
			}
			if (r_s > 0) {
				intervals.push(r_s);
			}
		}
		
		cout << "Case #" << t << ": " << max(l_s, r_s) << " " << min(l_s, r_s) << endl;
	}
}