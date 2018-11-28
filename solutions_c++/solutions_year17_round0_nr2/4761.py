#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int T;

int main() {

	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		int64_t n, low, high, mid;
		cin>>n;
		low = 0;
		high = n+1;
		while (low+1<high) {
			mid = (low+high)/2;
			int64_t x = mid, y = 1;
			while (y*10<=x)
				y *= 10;
			while (y>=10) {
				y /= 10;
				int z1 = x/(y*10)%10, z2 = x/y%10;
				if (z1>z2)
					x = x - x % y + (z1-z2)*y;
			}
			if (x<=n)
				low = mid;
			else
				high = mid;
		}
		/*
		int ans = 0;
		for (int i = n; i > 0; i--) {
			int t = i, s = 9;
			bool flag = true;
			while (t>0) {
				if (t%10>s) {
					flag = false;
					break;
				}
				s = t%10;
				t /= 10;
			}
			if (flag) {
				ans = i;
				break;
			}
		}
		*/
		cout<<"Case #"<<tt+1<<": "<<low<<endl;
	}
	return 0;
}