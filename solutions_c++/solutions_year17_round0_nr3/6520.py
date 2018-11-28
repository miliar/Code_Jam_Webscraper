#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int i=1; i<=t; i++) {
		int n,k;
		cin >> n >> k;

		vector<int> locs(n+2);
		locs[0] = locs[n+1] = 1;
		for(int j=1; j<n+1; j++) {
			locs[j] = 0;
		}

		// for(auto x: locs) 
		// 	cout << x;
		// cout << endl;

		// assign all but last pee-ers
		for(int p = 1; p < k; p++) {
			int mirl = 0, marl = 0, pos = 0;

			for(int j=1; j<n+1; j++){
				if(locs[j] != 1){
					int r=0, l=0, t=0;
					t=j-1;
					while(locs[t--] != 1) r++;
					t=j+1;
					while(locs[t++] != 1) l++;

					if (min(r,l) >= mirl) {
						mirl = min(r,l);
					}
				}
			}

			for(int j=1; j<n+1; j++){
				if(locs[j] != 1){
					int r=0, l=0, t=0;
					t=j-1;
					while(locs[t--] != 1) r++;
					t=j+1;
					while(locs[t++] != 1) l++;

					if (min(r,l) == mirl) {
						if (max(r,l) > marl) {
							marl = max(r,l);
							pos = j;
						}
					}
				}
			}

			locs[pos] = 1;
		}

		// for(auto x: locs) 
		// 	cout << x;
		// cout << endl;

		// now for last pee-er

		int maxrl = 0, minrl = 0;
		for (int j=1; j<n+1; j++) {
			if(locs[j] != 1){
					int r=0, l=0, t=0;
					t=j-1;
					while(locs[t--] != 1) r++;
					t=j+1;
					while(locs[t++] != 1) l++;

					if (min(r,l) > minrl) {
						minrl = min(r,l);
					}
			}
		}

		for(int j=1; j<n+1; j++){
			if(locs[j] != 1){
				int r=0, l=0, t=0;
				t=j-1;
				while(locs[t--] != 1) r++;
				t=j+1;
				while(locs[t++] != 1) l++;

				if (min(r,l) == minrl) {
					if (max(r,l) > maxrl) {
						maxrl =  max(r,l);
					}
				}
			}
		}

		cout << "Case #" << i << ": " << maxrl << " " << minrl << endl;
	}

	return 0;
}