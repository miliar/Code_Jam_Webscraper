#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;


int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		
		int n, c, m;
		cin >> n >> c >> m;
		map<int, int> f;
		map<int, int> g;
		for(int i=0; i<m; i++){
			int x, y;
			cin >> x >> y;
			f[y]++;
			g[x]++;
		}
		int mn = 0;
		for(auto p : f){
			mn = max(mn, p.second);
		}
		int cnt = 0;
		for(int i=1; i<=n; i++){
			cnt+=g[i];
			mn = max(mn, (cnt-1)/i+1);	
		}
		int cnt2 = 0;
		for(int i=n; i>=1; i--){
			if(g[i]>mn){
				cnt2+=g[i]-mn;
			}
		}
		cout << "Case #" << i << ": " << mn << " " << cnt2 << endl;
		
		
		
	}	
}
