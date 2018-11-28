#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <climits>
#include <set>
#include <cmath>
#define ll long long

using namespace std;

struct aa {
    int x, y;
    bool operator < (const aa &b) {
        if (x != b.x) return x < b.x;
        return y < b.y;
    }
};

bool cmp(int a, int b) {return a > b;}
int bsearch(int *a, int n, int k);

ll a[10001], b[10001];
int main() {
	int T;
	cin >> T;
	for(int nm=1;nm<=T;nm++){
		long long m,n;
		scanf("%lld%lld",&m,&n);
		for(int i=0;i<n;i++){
			scanf("%lld%lld",&a[i],&b[i]);
		}
		double speed=m / ((double)(m-a[0]) / b[0]);
		for(int i=1;i<n;i++){
			double speed2=m / ((double)(m-a[i]) / b[i]);
			if(speed2<speed){
				speed=speed2;
			}
		}
		printf("Case #%d: %f\n",nm,speed);
	}
	return 0;
}

int bsearch(int *a, int n, int k) {
    int l = 0, h = n;
    while (l < h) {
        int m = (l + h) / 2;
        if (a[m] == k) return m;
        else if (a[m] > k) h = m;
        else l = m + 1;
    }
    return l;
}
