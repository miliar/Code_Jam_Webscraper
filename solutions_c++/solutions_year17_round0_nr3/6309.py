#include <iostream>
#include <fstream>
#include <cstring>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <stack>
#include <list>	
#include <algorithm>
#include <limits.h>
#include <queue>

using namespace std;

ifstream f("pbC.in");
ofstream g("pbC2.out");

pair<int, int> maxMin(int n, int k){
	priority_queue<int> spaces;
	spaces.push(n);
	int lastLS = -1, lastRS = -1;
	
	while(k > 0){
		int space = spaces.top();
		spaces.pop();
		if(space % 2 == 1){
			lastLS = space / 2;
			lastRS = space / 2;
		}
		else {
			lastLS = space / 2;
			lastRS = space / 2 - 1;
		}
		if(lastLS != 0){
			spaces.push(lastLS);
		}
		if(lastRS != 0){
			spaces.push(lastRS);
		}
		k--;
	}
	return pair<int, int>(max(lastLS, lastRS), min(lastLS, lastRS));
}


int main(){
	int t;
	f >> t;

	for(int i = 1; i <= t; i++){
		int n, k;
		f >> n >> k;
		pair<int, int> res = maxMin(n, k);
		g << "Case #" << i << ": " << res.first << " " << res.second << endl;
	}

	return 0;
}