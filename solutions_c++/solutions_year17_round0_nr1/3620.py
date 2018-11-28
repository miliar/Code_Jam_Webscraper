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

char s[N+10];

int main(){
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; ++t){
		int k;
		scanf("%s %d", s, &k);
		int n = strlen(s);
		int ret = 0;
		for (int i=0; i<n-k+1; ++i)
			if (s[i] == '-'){
				++ ret;
				for (int j=0; j<k; ++j)
					if (s[j+i] == '+')	
						s[j+i] = '-';
					else
						s[j+i] = '+';
			}

		bool ok = true;
		for (int i=0; i<n; ++i)
			if (s[i] == '-')
				ok = false;

		printf("Case #%d: ", t);
		if (!ok)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ret);
				

	}
}
