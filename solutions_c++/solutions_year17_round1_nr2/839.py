#include <iostream>
#include <string>
#include <queue>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <climits>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

int n, p;
int amounts[1005];
int packages[1005][1005];
bool taken[1005][1005];
bool can_make(int actual, int required){
	return 90*required <= 100 * actual && 100*actual <= 110*required;
}
int get_lower(int amount, int required){
	return amount / (required * 1.1);
}
int get_upper(int amount, int required){
	return ceil(amount / (required * 0.9));
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "r+", stdout);
#endif

	int t; cin >> t;
	int case_num = 1;
	while(t--){
		memset(taken, false, sizeof taken);
		cin >> n >> p;
		int max_num_servings = -1;
		set<int> ks;
		ks.insert(1);
		for(int i = 0; i < n; i ++) cin >> amounts[i];
		for(int i = 0; i < n; i ++){
			for(int j = 0; j < p; j ++){
				cin >> packages[i][j];
				ks.insert(get_lower(packages[i][j], amounts[i]));
				ks.insert(1 + get_lower(packages[i][j], amounts[i]));
				ks.insert(1 + get_upper(packages[i][j], amounts[i]));
				ks.insert(-1 + get_lower(packages[i][j], amounts[i]));
				ks.insert(-1 + get_upper(packages[i][j], amounts[i]));
				ks.insert(get_upper(packages[i][j], amounts[i]));
				max_num_servings = max(max_num_servings,int(packages[i][j] * 1.1 / amounts[i])) + 1;
			}
			sort(packages[i], packages[i] + p);
		}
		int ans = 0;
		for(auto k : ks){
			
			int num_packages = INT_MAX;
			for(int i = 0; i < n; i ++){
				int num_ingredient = 0;
				for(int j = 0; j < p; j ++){
					if(can_make(packages[i][j], amounts[i] * k) && !taken[i][j])
						num_ingredient++;
				}
				num_packages = min(num_packages, num_ingredient);
			}
			ans += num_packages;
			for(int i = 0; i < n; i ++){
				int num_ingredient = 0;
				for(int j = 0; j < p && num_ingredient < num_packages; j ++){
					if(can_make(packages[i][j], amounts[i] * k) && !taken[i][j]){
						num_ingredient++;
						taken[i][j] = true;
					}
				}
			}
		}
		cout << "Case #" << case_num ++ << ": " << ans << endl;
	}
	return 0;
}
