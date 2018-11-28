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

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "r+", stdout);
#endif

	int case_num = 1;
	int t; cin >> t;
	while(t--){
		ll n, k; cin >> n >> k;
		ll l = n, r = n;
		ll num_ls = 1;
		ll num_rs = 0;
		ll layer_number = 0;
		ll num_nodes = 0;
		ll current_layer_nodes = 1;
		while(num_nodes < k){
			num_nodes += current_layer_nodes;
			layer_number ++;
			current_layer_nodes *= 2LL;
		}
		layer_number --;
		num_nodes -= (current_layer_nodes / 2LL);
		ll min_num_rs = k - num_nodes;

		for(int i = 0; i < layer_number; i ++){
			if(l == r){
				num_ls = num_ls + num_rs;
				num_rs = 0;
			}
			if(l % 2 == 0){
				num_rs += num_rs;
				num_rs += num_ls;
			}
			else{
				num_ls += num_ls;
				num_ls += num_rs;
			}
			l = (l - 1LL) / 2LL;
			ll x = (r - 1LL) / 2LL;
			r = (r - 1LL) - x;
		}
		ll segment;
		if(num_rs >= min_num_rs){
			segment = max(r, 0LL);
		}
		else{
			segment = max(l, 0LL);
		}
		l = (segment - 1LL) / 2LL;
		r = (segment - 1LL) - l;

		cout << "Case #" << case_num ++ << ": " << max(r, 0LL) << " " << max(l, 0LL) << endl;
	}
	return 0;
}
