#include <iostream>
#include <vector>

using namespace std;

//g++ -std=c++11 stable_neighbors.cpp -o main && ./main < test.in

int mod(int n, int m) {
	if(m < 0) m*=-1;
	int ans = n%m;
	if(n < 0) ans += m;
	return ans;
}

int main () {
	int t;
	cin >> t;

	for(int i=1; i<=t; i++) {
		int n,r,o,y,g,b,v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		if (r > n/2 || y > n/2 || b > n/2) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
		else {
			vector<char> ans;
			while(r--) {
				ans.push_back('R');
			}
			while(y--){
				ans.push_back('Y');
			}
			while(b--){
				ans.push_back('B');
			}

			for(int l=0; l<3;l++) {
				for(int idx=0; idx<n; idx++) {
					if(ans[idx] == ans[mod(idx+1,n)]) {
						// find the first element which can be inserted in between
						int j = idx;
						while(ans[mod(j, n)] == ans[mod(idx,n)]) j++;
						swap(ans[mod(j,n)], ans[mod(idx+1,n)]);
					}
				}
			}

			string res = "";
			for(auto a: ans) res+= a;

			cout << "Case #" << i << ": " << res << endl;
		}
		
	}
	return 0;
}
