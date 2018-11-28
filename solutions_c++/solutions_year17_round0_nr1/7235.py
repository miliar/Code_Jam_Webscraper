#include <bits/stdc++.h>
using namespace std;
vector < bool > vi;
string s;
int n;

int solve(int k) {
	int moves = 0;
	queue < int > q;
	for(int i=0;i<k;i++) {
		while(!q.empty() && q.front() <= i-n) q.pop();
		if(q.size()&1) {	// flip it
			if(vi[i]==1) {	// after flipping it will be 0 , therefore mask window
				if(i > k-n) return -1;
				moves++;
				q.push(i);
			}
		}
		else {				// no flip needed
			if(vi[i]==0) {	// it will remain 0 therefore mask window
				if(i > k-n) return -1;
				moves++;
				q.push(i);
			}
		}
	}
	return moves;
}

int main() {
	//freopen("inputA.txt" , "r" , stdin);
	//freopen("output.txt" , "w" , stdout);

	int t;
	cin >> t;
	for(int i=1;i<=t;i++) {
		cin >> s >> n;
		int k = s.size();
		vi.clear();
		for(int i=0;i<k;i++) {
			if(s[i]=='+') vi.push_back(1);
			else vi.push_back(0);
		}
		int ans = solve(k);
		if(ans==-1) cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}