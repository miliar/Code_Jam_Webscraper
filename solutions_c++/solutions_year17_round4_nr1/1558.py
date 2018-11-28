#include <iostream>
#include <cstdio>

using namespace std;
int a[1000];
int main() {
	freopen("A.in","r",stdin);
	freopen("A.txt","w",stdout);
	int t,x,p,n, ans;

	cin >> t;
	for(int aa=0;aa<t;aa++) {
		cin >> n >> p;
		for(int i=0;i<=p;i++) a[i] = 0;
		for(int i=0;i<n;i++) {
			cin >> x;
			a[x % p] ++;
		}

		if(p==2) {
			ans = n - a[1] / 2;
		} else if(p==3) {
			int xx = min(a[1], a[2]);
			int yy = max(a[1],a[2]) - xx;
			ans = a[0] + xx + (yy + 2) / 3;
		}
		// else if(p==4) {
		// 	int xx = 
		// }

		cout << "Case #" << aa+1 << ": " << ans << endl;


	}
	
	return 0;
}