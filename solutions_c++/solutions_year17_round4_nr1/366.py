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
	ios::sync_with_stdio(0); cin.tie(0);
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n,p;
		cin >> n >> p;
		cout << "Case #" << t << ": ";
		if(p == 4) {
			int a[4]={0};
			for(int i = 0; i < n; ++i) {
				int g;
				cin >> g;
				++a[g%4];
			}
			int ans = a[0];
			ans += a[2]/2;
			a[2]&=1;
			int k = min(a[1],a[3]);
			ans += k;
			a[1]-=k;
			a[3]-=k;
			if(a[1] < a[3])
				swap(a[1],a[3]);
			int md = 0;
			while(a[1]) {
				if(md==0) ++ans;
				if(a[2] && md == 2) {
					--a[2];
					md = (md+2)%4;
				} else {
					md = (md+1)%4;
					--a[1];
				}
			}
			if(a[2]) {
				if(md==0) ++ans;
			}
			cout << ans << "\n";
		} else if(p == 3) {
			int a[3] = {0};
			for(int i = 0; i < n; ++i) {
				int g;
				cin >> g;
				++a[g%3];
			}
			int ans = a[0];
			int k = min(a[1],a[2]);
			ans += k;
			a[1]-=k;
			a[2]-=k;
			ans += (a[1]+a[2]+2)/3;
			cout << ans << "\n";
		} else if(p == 2) {
			int a[2] = {0};
			for(int i = 0; i < n; ++i) {
				int g;
				cin >> g;
				++a[g%2];
			}
			int ans = a[0] + (a[1]+1)/2;
			cout << ans << "\n";
		}
		
	}


	return 0;
}