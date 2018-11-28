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
int main(){
	int T;
	cin>>T;
	for (int ts=1; ts<=T; ++ts){
		int n;
		int k;
		scanf("%d%d", &n, &k);
		priority_queue<int> q;
		q.push(n);

		for (int i=0; i<k-1; ++i){
			int j = q.top();
			q.pop();
			--j;
			q.push(j / 2);
			q.push(j - j / 2);
		}
		int j = q.top();
		--j;
		printf("Case #%d: %d %d\n", ts, (j + 1) / 2, j - (j + 1) / 2);
	}
	return 0;
}
