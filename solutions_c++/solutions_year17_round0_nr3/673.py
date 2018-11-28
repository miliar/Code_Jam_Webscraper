#include <bits/stdc++.h>
#define ll long long
#define int ll
#define mod 1000000007
using namespace std;

main(){
	ios::sync_with_stdio(0);
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
	
	int cases, n, k;
	
	cin >> cases;
	for(int t = 1; t <= cases; t++) {
		cin >> n >> k;
		cout << "Case #" << t << ": ";
		map <int, int> c;
		c[n] = 1;
		
		for(map<int, int>::reverse_iterator it = c.rbegin(); it != c.rend(); it++) {
			if(it->second < k) {
				c[it->first / 2] += it->second;
				c[it->first / 2 - (1 - (it->first % 2))] += it->second;
				k -= it->second;
			} else {
				cout << it->first / 2 << " " << it->first / 2 - (1 -(it->first % 2)) << endl;
				break;
			}
		}
		
	}
}

