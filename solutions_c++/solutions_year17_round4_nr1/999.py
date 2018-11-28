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
	int ts;
	cin >> ts;
	for (int te=1; te<=ts; ++te){
		int n, m;
		scanf("%d%d", &n, &m);

		vector<int> a;

		for (int i=0; i<n; ++i){
			int k;
			scanf("%d", &k);
			a.push_back(k);
		}

		int ret = 0;
		if (m == 2){

			int countOne = 0;

			for (int i=0; i<n; ++i){
				a[i] %= 2;
				if (a[i] == 0)
					++ ret;
				else
					++ countOne;
			}

			ret += (countOne + 1) / 2;

		} else if (m == 3){
			int countOne = 0;
			int countTwo = 0;

			for (int i=0; i<n; ++i){
				a[i] %= 3;
				if (a[i] == 0)
					++ ret;
				else if (a[i] == 1){
					++ countOne;
				} else {
					++ countTwo;
				}
			}

			int oneAndTwo = min(countTwo, countOne);
			ret += oneAndTwo;

			countTwo -= oneAndTwo;
			countOne -= oneAndTwo;

			ret += (countOne + 2) / 3;
			ret += (countTwo + 2) / 3;
		} else {
			vector<int> left(4, 0);
			for (int i=0; i<n; ++i)
				++ left[a[i] % 4];

			ret += left[0];
			ret += left[2] / 2;
			left[2] %= 2;

			int oneAndThree = min(left[1], left[3]);
			ret += oneAndThree;
			left[1] -= oneAndThree;
			left[3] -= oneAndThree;

			if (left[2] == 0){
				ret += (left[1] + 3) / 4;
				ret += (left[3] + 3) / 4;
			} else {
				ret += (left[1] + left[3] + 2 + 3) / 4;
			}
		}
		printf("Case #%d: %d\n", te, ret);
	}

	return 0;
}
