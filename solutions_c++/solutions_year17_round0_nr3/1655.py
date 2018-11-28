#include <iostream>
#include <queue>
#include <map>

#define mp make_pair

using namespace std;

typedef pair<long, long> entry;

int main() {
	int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		long n, k, p = 1, kc = 0;
		long ans_min, ans_max;
		cin >> n >> k;
		priority_queue<entry> pq;
		pq.push(mp(n, 1));
		while (kc < k) {
			map<long, long> m;
			while (pq.size() > 0) {
				entry e = pq.top();
				pq.pop();
			
				// cout << e.first << ":" << e.second << " ";
			
				long val = e.first;
				long count = e.second;
			
				long n1 = val / 2;
				long n2 = val - val / 2 - 1;
				
				if (n1 > 0) m[n1] += count;
				if (n2 > 0) m[n2] += count;
			
				kc += count;
			
				if (kc >= k) {
					ans_min = val - val / 2 - 1;
					ans_max = val / 2;
					break;
				}
			
			}
		
			for (auto it = m.begin(); it != m.end(); ++it) {
				pq.push(*it);
			}
		}
	
		cout << "Case #" << _t << ": " << ans_max << " " << ans_min << endl;
	}
	
	return 0;
}
