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
typedef long long ll;

int main(){
	int ts;
	scanf("%d", &ts);
	for (int te=1; te<=ts; ++te){
		int n, m;
		scanf("%d%d", &n, &m);
		vector<int> e(n);
		vector<int> s(n);
		for (int i=0; i<n; ++i)
			scanf("%d%d", &e[i], &s[i]);

		vector<vector<ll>> d(n, vector<ll>(n));
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
				cin>>d[i][j];

		vector<pair<int,int>> q(m);
		for (int i=0; i<m; ++i)
			scanf("%d%d", &q[i].first, &q[i].second);

		for (int k=0; k<n; ++k)
			for (int i=0; i<n; ++i) if (i != k && d[i][k] != -1)
				for (int j=0; j<n; ++j) 
					if (i != j && j != k && d[k][j] != -1)
						if (d[i][j] == -1 || d[i][k] + d[k][j] < d[i][j])
							d[i][j] = d[i][k] + d[k][j];

		vector<vector<double>> t(n, vector<double>(n, 1e100));
		for (int i=0; i<n; ++i){
			for (int j=0; j<n; ++j){
				if (i == j)
					t[i][j] = 0.0;
				if (d[i][j] != -1 && d[i][j] <= e[i])
					t[i][j] = double(d[i][j]) / s[i];
//				cout<<t[i][j]<<' ';
			}
			//cout<<endl;
		}


		for (int k=0; k<n; ++k)
			for (int i=0; i<n; ++i) if (i != k)
				for (int j=0; j<n; ++j) if (i != j && j != k)
					if (t[i][k] + t[k][j] < t[i][j])
						t[i][j] = t[i][k] + t[k][j];


		printf("Case #%d:", te);

		for (int i=0; i<m; ++i)
			printf(" %.10lf", t[q[i].first - 1][q[i].second - 1]);

		puts("");

	}
	return 0;
}
