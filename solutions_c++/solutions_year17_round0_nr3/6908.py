#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
#define SIZE  1010
using namespace std;

struct dist {
	bool oc = false;
	int l = -1;
	int r = - 1;
};
int T = 0;
int l;
int n, k;

dist arr[SIZE];
vector<int> max_dist;
vector<int> max_dist2;
int mind(int a, int b) {
	if(a == -1) return b;
	else if(b == -1) return a;
	else return min(a,b);
}
int calc_dist() {
	int m = -1;
	l = 0;
	for(int i=1; i <= n+1; i++) {
		arr[i].l = i - l-1;
		arr[l].r = i - l-1;
		if(arr[i].oc) {
			//cout << l << arr[l].r << endl;
			arr[l].r = i - l-1;
			for(int j=l+1; j <= i-1; j++) {
				arr[j].l = j-l-1;
				arr[j].r = i -j-1;
			}
			l = i;
		}
		// if(!arr[i].oc) {
		// 	cout << min(arr[l].l, arr[l].r))
		// 	m = max(m, min(arr[l].l, arr[l].r));
		// }
		// cout << m << endl;
	}
	return m;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
	cin >> T;
	int Ti = 1;
	while(T--) {

		int m = 0;
		cin >> n >> k;
		for(int i=0; i < SIZE; i++) {
			arr[i].l = -1; arr[i].r = -1; arr[i].oc = false;
		}
		arr[0].oc = true;
		// arr[2].oc = true;
		arr[n+1].oc = true;
		int last = -1;
		for(int x = 0; x < k; x++) {
			max_dist.clear();
			max_dist2.clear();
			m = calc_dist();
			// for(int i=0; i <= n+1; i++) {
			// 	cout << arr[i].l << " " << arr[i].r << endl;
			// }
			//cout << m << endl;
			m = -1;
			for(int i = 1; i < n+1; i++) {
				if(!arr[i].oc) {
					//cout << arr[i].l << " " << arr[i].r << endl;
					//cout << min(arr[i].l, arr[i].r) << endl;
					m = max(m, min(arr[i].l, arr[i].r));
				}
				//cout << min(arr[i].l, arr[i].r) << endl;
				// if(min(arr[i].l, arr[i].r) == m) {
				// 	max_dist.push_back(i);
				// }
			}
			//cout << m << endl;
			for(int i=1; i < n+1; i++) {
				if(!arr[i].oc) {
					if(min(arr[i].l, arr[i].r) == m) {
						max_dist.push_back(i);
					}	
				}
			}
			// for(int i=0; i < max_dist.size(); i++) {
			// 	cout << max_dist[i] << endl;
			// }
			if(max_dist.size() == 1) {
				arr[max_dist[0]].oc = true;
				
				last = max_dist[0];
				//cout << last << endl;
			}
			else {
				m = 0;
				for(int i=0; i < max_dist.size(); i++) {
					m = max(m, max(arr[max_dist[i]].l, arr[max_dist[i]].r));
				}
				for(int i=0; i < max_dist.size(); i++) {
					if(max(arr[max_dist[i]].l, arr[max_dist[i]].r) == m) {
						max_dist2.push_back(max_dist[i]);
					}
				}
				// for(int i=0; i < max_dist2.size(); i++) {
				// 	cout << max_dist2[i] << endl;
				// }
				arr[max_dist2[0]].oc = true;
				last = max_dist2[0];
				//cout << last << endl;
			}

		}
		//cout << endl;
		//for(int i=1; i < n+1; i++) if(arr[i].oc) cout << i << endl;
		//cout << last << endl;
		cout << "Case #" << Ti << ": " << max(arr[last].l, arr[last].r) <<  " " << min(arr[last].l, arr[last].r) << endl;
		Ti++;
	}
    return 0;
}