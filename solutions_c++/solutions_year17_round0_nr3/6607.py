#include<iostream>
#include<queue>
#include<vector>
#include<cmath>
using namespace std;

int main(){
	int t, n, k;
	cin >> t;
	for (int z = 1; z <= t; ++ z){
		cin >> n >> k;
		priority_queue<int> empty_intervals;
		empty_intervals.push(n);
		int small, large;
		for (int i = 0; i < k ; ++ i){
			int top = empty_intervals.top();
			empty_intervals.pop();
			large = top/2;
			small = large - (top%2 == 0);
			if (large != 0){
				empty_intervals.push(large);
				if (small != 0){
					empty_intervals.push(small);
				}
			}
		}
		cout << "Case #" << z << ": " << large << ' ' << ((small < 0)? 0 : small) << endl;
	}
	return 0;
}