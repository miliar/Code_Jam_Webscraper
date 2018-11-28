#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct one {
	int l,r,interval;
	one(int _l, int _r, int _interval) {
		l = _l;
		r = _r;
		interval = _interval;
	}
};
struct cmp {
	bool operator() (const one & a, const one & b) {
		return a.interval < b.interval;
	}
};

int main()
{
	int n, T, k, min_lr, max_lr;
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("Coutput_small2.txt","w",stdout);
	int ncase = 0;
	cin >> T;
	while(T--) {
		ncase++;
		cin >> n >> k;
		priority_queue <one,vector<one>, cmp> pqe;
		pqe.push(one(0,n+1,n));
		min_lr = max_lr = 0;
		for(int i = 1; i <= k; i++) {
			one u = pqe.top();
			if(u.interval == 0) {
				break;
			}
			else {
				int l = u.l;
				int r = u.r;
				int mid = (r+l)/2;
				pqe.pop();
				pqe.push(one(l,mid, mid-l-1));
				pqe.push(one(mid, r, r-mid-1));
				// cout << "l = " << l << " mid = " << mid << " r = " << r << endl;
				min_lr = min(mid-l-1, r-mid-1);
				max_lr = max(mid-l-1, r-mid-1);
			}
		}
		printf("Case #%d: %d %d\n",ncase, max_lr, min_lr);
	}
	return 0;
}