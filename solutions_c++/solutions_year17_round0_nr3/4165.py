#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

vector<pair<int,int>> t;

void recadd(int a, int b) {
	if (a == 0 && b == 0)
		return;
	t.push_back(make_pair(a,b));
	recadd(a/2, (a-1)/2);
	recadd(b/2, (b-1)/2);
}

int main() {
	
	int test;
	cin>>test;
	for (int testc = 1; testc <= test; testc++) {
		
		t = vector<pair<int,int>>();
		int n,k;
		cin >> n >> k;
		
		recadd(n/2, (n-1)/2);
		
		sort(t.begin(), t.end());
		reverse(t.begin(), t.end());
		
		
		pair<int,int> res = make_pair(0,0);
		if ((unsigned)k <= t.size()) {
			res = t[k-1];
		}
		
		cout << "Case #" << testc << ": " << res.first << " " << res.second << endl;
	}
	return 0;
}


