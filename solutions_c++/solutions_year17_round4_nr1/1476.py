#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>
#include <math.h>
#include <iomanip>
#include <utility>

using namespace std;

int T, n, p;
int a[4];

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		cin>>n>>p;
		for (int i = 0; i < 4; i++)
			a[i] = 0;
		for (int i = 0; i < n; i++) {
			int k;
			cin>>k;
			a[k % p] += 1;
		}
		int ans;
		if (p==1) {
			ans = a[0];
		}
		else if (p==2) {
			ans = a[0]+(int)((a[1]+1)/2);
		}
		else if (p==3) {
			int small = min(a[1], a[2]), large = max(a[1], a[2]);
			ans = a[0]+small+(int)((large-small)/3);
			if ((large-small)%3!=0)
				ans += 1;
		}
		else {
			ans = 0;
			for (int i13 = 0; i13 <= min(a[1], a[3]); i13++) {
				int i1 = a[1]-i13, i3 = a[3]-i13;
				for (int i112 = 0; i112 <= min((int)(i1/2), a[2]); i112++) {
					int i2 = a[2]-i112;
					for (int i233 = 0; i233 <= min((int)(i3/2), i2); i233++) {
						int now = a[0]+i13+i112+i233;
						int r1 = a[1]-i13-i112*2, r2 = a[2]-i112-i233, r3 = a[3]-i13-i233*2;
						now += (int)(r1/4)+(int)(r2/2)+(int)(r3/4);
						int rr = (int)(r1%4+(r2%2)*2+(r3%4)*3);
						if (rr!=0)
							now += 1;
						if (now>ans)
							ans = now; 
					}
				}
			}
		}
		cout<<"Case #"<<tt+1<<": "<<ans<<endl;
	}
	return 0;
}