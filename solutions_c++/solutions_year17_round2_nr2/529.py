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
	scanf("%d", &ts);

	for (int te=1; te<=ts; ++te){
		int n;
		scanf("%d", &n);
		vector<int> d;
		for (int i=0; i<6; ++i){
			int k;
			scanf("%d", &k);
			d.push_back(k);
		}

		vector<int> b = d;
		vector<char> c;
		sort(d.rbegin(), d.rend());
		string x = "ROYGBV";

		for (int i=0; i<6; ++i)
			for (int j=0; j<6; ++j)
				if (d[i] == b[j]){
					c.push_back(x[j]);
					b[j] = -1;
					break;
				}

		printf("Case #%d: ", te);

		if (d[1] + d[2] < d[0] || d[1] > d[0] + d[2]){
			puts("IMPOSSIBLE");
		} else {
			string s;	
			for (int i=0; i<d[0]; ++i)
				s.push_back(c[0]);
			for (int i=d[0]; i>=0; --i){
				if (d[1]) {
					s.insert(i, 1, c[1]);
					-- d[1];
				}
				else if (d[2]) {
					s.insert(i, 1, c[2]);
					-- d[2];
				}
			}

			int l = s.size() - 1;
			for (int i=0; i<d[2]; ++i){
				s.insert(l, 1, c[2]);
				--l;
			}


			cout<<s<<endl;

		}
	}

	return 0;
}
