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


vi to_vec(ll x){
	vi ret;
	while(x){
		ret.push_back(x % 10);
		x /= 10;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}
ll from_vec(vi v){
	ll ret = 0;
	for(int i = 0; i < v.size(); i ++){
		ret *= 10;
		ret += v[i];
	}
	return ret;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "r+", stdout);
#endif
	int case_num = 1;
	int t; cin >> t;
	while(t--){
		ll n; cin >> n;
		vi old_digits = to_vec(n);
		vi new_digits = old_digits;
		if(!is_sorted(new_digits.begin(), new_digits.end())){
			int m = old_digits.size();
			int point_of_disjunction = 0;
			for(int i = m - 1; i > 0 && point_of_disjunction == 0; i --){
				int max_to_come = *max_element(old_digits.begin(), old_digits.begin() + i);
				if(old_digits[i] > max_to_come && is_sorted(old_digits.begin(), old_digits.begin() + i)){
					point_of_disjunction = i;
				}
			}
			new_digits[point_of_disjunction]--;
			for(int i = point_of_disjunction + 1; i < m; i ++){
				new_digits[i] = 9;
			}
		}
		cout << "Case #" << case_num ++ << ": " << from_vec(new_digits) << endl;
	}
	return 0;
}
