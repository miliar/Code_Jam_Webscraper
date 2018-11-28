// bathroom2

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <iomanip>
#include <sstream>
#include <map>
#include <queue>

using namespace std;

int main(){
	int q;
	cin >> q;
	for (int z = 0; z < q; z++){
		long long n, k;
		cin >> n >> k;
		
		priority_queue <int> stall;
		stall.push(n);
		
		long long mini, maxi;
		for (int i = 0; i < k; i++){
			long long s = stall.top();
			stall.pop();
			long long d = s/ 2;
			stall.push(d);
			stall.push(d - 1 + s%2);
			if (i == k-1){
				maxi = d;
				mini = d - 1 + s % 2;
			}
		}
		cout << "Case #" << z+1 << ": " << maxi << " " << mini << endl;
	}
}