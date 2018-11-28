#include <iostream>
#include <cstdio>

using namespace std;
// int a[1010][1010];
int s[1010],ss[1010];;

int main() {
	freopen("B.in","r",stdin);
	freopen("B.txt","w",stdout);
	int tt,t,x,b, p,n,c,m, ans, total;

	cin >> t ;
	for(int aa=0;aa<t;aa++) {
		cin >> n >> c >> m;

		// for(int i=1;i<=c;i++) for(int j=1;j<=n;j++) {
		// 	a[i][j] = 0;
		// }
		for(int i=1;i<=c;i++) s[i] = 0;
		for(int i=1;i<=n;i++) ss[i] = 0;

		for(int i=0;i<m;i++) {
			cin >> p >> b;
			// a[b][p] ++;
			s[b]++;
			ss[p]++;
		}

		ans = 0;
		for(int i=1;i<=c;i++) {
			ans = max(ans, s[i]);
		}

		for(int i=1;i<=n;i++) {
			ans = max(ans, (ss[i] - 1) / i + 1);
		}

		total = 0;
		for(int i=1;i<=n;i++) {
			if(ss[i] > ans) {
				total += ss[i] - ans;
			}
		}











		cout << "Case #" << aa+1 << ": " << ans << " " << total << endl;


	}
	
	return 0;
}