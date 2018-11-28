#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	long long t, n, k;
	cin >> t;
	for(int tt = 0; tt < t; tt++) {
		cin >> n >> k;
		long long max, min;
		vector<int> pos;
		long long pot = 1; 
		while(pot <= k) {
			pot *= 2;
		}
		pot/=2;
		if(k == 1) {
			max = n/2;
			if (n%2 == 0)
				min = n/2 -1;
			else
				min = n/2;
		}
		else {
			if(pot == 1) {
				if(k == 2)
					pos.push_back(1);
				else
					pos.push_back(2);
			}
			else {
				while(k > 1) {
					if(k >= pot + pot/2) {
						pos.push_back(2);
						k -= pot;
					}
					else {
						pos.push_back(1);
						k -= pot/2;
					}
					pot/=2;
				}
			}
			max = n/2;
			if (n%2 == 0)
				min = n/2 -1;
			else
				min = n/2;
			for(int i = pos.size()-1; i >=0; i--) {
				if(pos[i] == 1)
					n = max;
				else
					n = min;
				max = n/2;
				if (n%2 == 0)
					min = n/2 -1;
				else
					min = n/2;
			}
		}
		cout << "Case #" << tt+1 << ": " << max << " " << min << endl;
	}
	return 0;
}