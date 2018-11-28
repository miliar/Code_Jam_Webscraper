#ifndef _HEAD_H_
#define _HEAD_H_
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>

#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define sz(a) ((int)(a).size())
#define SQR(x) ((x)*(x))

using namespace std;

template <class T> void checkmin(T &a, T b){ if (b<a) a=b; }
#endif
#define N 1000

int k[N+10];
int s[N+10];

int main(){
	int ts;
	cin>>ts;
	for (int te=1; te<=ts; ++te){
		int d;
		int n;
		scanf("%d%d", &d, &n);
		double myTime = 0.0;
		for (int i=0; i<n; ++i){
			scanf("%d%d", &k[i], &s[i]);
			myTime = max(myTime, double(d - k[i]) / s[i]);
		}
		printf("Case #%d: ", te);
		printf("%.10lf\n", d / myTime);
	}
	return 0;
}
