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


bool augment(int i, vector<vector<int>> &a, 
		vector<bool> &v, vector<int> &f){
	for (auto k : a[i]){
		if (!v[k]){
			v[k] = true;
			if (f[k] == -1 || augment(f[k], a, v, f)) {
				f[k] = i;
				return true;
			}
		}
	}
	return false;
}

int main(){
	int ts;
	cin >> ts;
	for (int te=1; te<=ts; ++te){
		int n, c, m;
		scanf("%d%d%d", &n, &c, &m);
		vector<vector<int>> p(c);

		for (int i=0; i<m; ++i){
			int pi, bi;
			scanf("%d%d", &pi, &bi);
			p[bi - 1].push_back(pi);
		}



		sort(p[0].begin(), p[0].end());
		sort(p[1].begin(), p[1].end());

		if (p[0].size() > p[1].size())
			swap(p[0], p[1]);

		vector<vector<int>> a(p[0].size());

		for (int i=0; i<p[0].size(); ++i){

			for (int j=0; j<p[1].size(); ++j)
				if (p[0][i] != p[1][j])
					a[i].push_back(j);
		}
		
		vector<int> f(p[1].size(), -1);

		int ret = 0;
		for (int i=0; i<p[0].size(); ++i){
			vector<bool> v(p[1].size(), false); 
			if (augment(i, a, v, f))
				++ ret;
		}

		int promote = 0;

		if (ret == p[0].size()){
			ret = p[0].size() + p[1].size() - ret;
		} else {
			for (int j=0; j<p[1].size(); ++j)
				if (f[j] == -1) {
					if (p[1][j] == 1)
						ret = p[0].size() + p[1].size() - ret;
					else {
						promote = p[0].size() - ret;
						ret = p[1].size();
					}
					break;
				}
		}

		printf("Case #%d: %d %d\n", te, ret, promote);

	}
}
