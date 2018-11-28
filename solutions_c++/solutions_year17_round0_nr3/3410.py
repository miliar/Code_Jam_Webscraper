//Author: net12k44

#include <bits/stdc++.h>
using namespace std;


void solve(){
	int n, k;
	cin >> n >> k;
	priority_queue<int> q;
	q.push(n);
	int mmin, mmax;
	while (k-- > 0){
		n = q.top(); q.pop();
		mmax = n/2;
		mmin = n-1-mmax;
		if (mmin > 0) q.push(mmin);
		if (mmax > 0) q.push(mmax);
	}
	
	cout << mmax << " " << mmin << endl;
	
}

int main(){
	freopen("file.out","w",stdout);
	
	int test; cin >> test;
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}