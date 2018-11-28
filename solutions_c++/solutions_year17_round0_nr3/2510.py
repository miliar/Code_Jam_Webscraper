#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<climits>
using namespace std;

long long n, m, x, y, z, a, b, c, maxans, minans;

void cal(long long x, long long y) {
	if (y == 1) {
		maxans = x/2;
		minans = x - x/2 - 1;
		return ;
	}
	cal(x - x/2 - 1, y - y/2 - 1);
}

void get(long long a, long long b, long long x, long long y) {
	long long a1 = 0, b1 = 0, x1 = 0, y1 = 0;
	if (m == 0) {
		cout<<max(a, b)/2<<' '<<max(a, b) - 1 - max(a, b)/2<<endl;
		return ;
	}
	if (x > 0) {
		if (((a - 1) / 2) % 2 == 0) {
			y1 += x * 2;
			b1 = (a - 1) / 2;
		} else {
			x1 += x * 2;
			a1 = (a - 1) / 2;
		}
	}
	if (y > 0) {
		if ((b/2) % 2 == 0) {
			b1 = b/2;
			a1 = b - 1 - b1;
			x1 += y;
			y1 += y;
		} else {
			a1 = b/2;
			b1 = b - 1 - a1;
			y1 += y;
			x1 += y;
		}
	}
	// cout<<a1<<' '<<b1<<' '<<x1<<' '<<y1<<endl;
	if (m <= x1 + y1) {
		if (a1 < b1) {
			if (m <= y1) {
				cout<<b1/2<<' '<<b1 - b1/2 - 1<<endl;
			} else {
				cout<<a1/2<<' '<<a1 - a1/2 - 1<<endl;
			}
		} else {
			if (m <= x1) {
				cout<<a1/2<<' '<<a1 - a1/2 - 1<<endl;
			} else {
				cout<<b1/2<<' '<<b1 - b1/2 - 1<<endl;
			}
		}
		return ;
	} else {
		m -= x1 + y1;
	}
	get(a1, b1, x1, y1);
}

int main() {
	int T;
	freopen("C-large.in", "rb", stdin);
	freopen("out.txt", "wb", stdout);
	cin>>T;
	for (int cas = 1; cas <= T; ++ cas) {
		cout<<"Case #"<<cas<<": ";
		cin>>n>>m;
		// maxans = 0;
		// minans = LLONG_MAX;
		// cal(x, y);
		// cout<<maxans<<' '<<minans<<endl;
		m --;
		if (n % 2 == 0) {
			get(0, n, 0, 1);
		} else {
			get(n, 0, 1, 0);
		}
	}
	return 0;
}