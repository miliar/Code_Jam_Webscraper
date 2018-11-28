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
	scanf("%d", &T);

	for (int ts=1; ts<=T; ++ts){
		string s;
		cin>>s;
		int n = s.size();
		string t = s;


		for (int i=0; i<n; ++i){
			if (i)
				t[i] = max(t[i-1], s[i-1]);
			else
				t[i] = 0;
					
		}

		bool minus = false;
		for (int i=n-1; i>=0; --i){
			if (minus)
				-- s[i];
			minus = false;
			if (s[i] < t[i]){
				minus = true;
				for (int j=i; j<n; ++j)
					s[j] = '9';
			}
		}
		unsigned long long ret = stoull(s);


		printf("Case #%d: ", ts);
		cout<<ret<<endl;
	}
	return 0;
}
