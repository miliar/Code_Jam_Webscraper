#include <bits/stdc++.h>
using namespace std;

vector<int> nums;

void pre() {
	int auxj, auxi;
	for(int i = 1; i <= 9; i++) {
		nums.push_back(i);
		auxi = i *10;
		for(int j = i; j <= 9; j++) {
			auxj = auxi + j;
			nums.push_back(auxj);
			auxj*= 10;
			for(int k = j; k <= 9; k++) {
				nums.push_back(auxj + k);
			}
		}
	}
	sort(nums.begin(), nums.end());
}

int bs(int n) {
	int fr = 0;
	int ls = nums.size();
	int m, ans = 1;
	while(fr <= ls) {
		m = (fr + ls)/2;
		if(nums[m] <= n) {
			ans = nums[m];
			fr = m + 1;
		} else {
			ls = m - 1;
		}
	}
	return ans;
}

int main() {
	pre();
	int t, n, c = 0;
	cin >> t; 
	while(c < t) {
		c++;
		cin >> n;
		cout << "Case #" << c <<": " << bs(n) << "\n";
	}
	return 0;
}