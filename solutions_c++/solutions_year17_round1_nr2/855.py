#include <stdio.h>
#include <math.h>
#include <string.h>

#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int INT(){int x;scanf("%d",&x);return x;}
typedef pair<int,int> pii;

int R[200];

typedef long long LL;

bool canMake(int num, LL perUnit, LL haveTotal) {
	return perUnit * num * 90 <= haveTotal*100 && haveTotal * 100 <= perUnit * num * 110;
}

int smallest(int x, int r) {
	int ret = (int) ceil((x * 100.0) / (r * 110.0));
	if (ret == 0) ret = 1;
	return ret;
}

int largest(int x, int r) {
	return (int)((x * 100.0) / (r * 90.0));
}

pii toRange(int x, int r) {
	pii ret = pii(smallest(x,r), largest(x,r));
//printf("\nhave %d, req %d, small %d, large %d", x, r, ret.first, ret.second);
	return ret;
}

bool valid(pii p) {
	return p.first <= p.second;
}

int N;
int P;
pii Q[200][200];
vector<pii> V[200];
int idx[200];

int main() {
	int T=INT();
	for (int t=1;t<=T;++t) {
		N=INT();
		P=INT();
		for (int i=0;i<N;++i)R[i]=INT();
		for (int i=0;i<N;++i)
			for (int j=0;j<P;++j)
				Q[i][j]=toRange(INT(), R[i]);

		for (int i=0;i<N;++i) {
			V[i].clear();
			idx[i]=0;
			for (int j=0;j<P;++j) {
				if (valid(Q[i][j])) {
					V[i].push_back(Q[i][j]);
				}
			}
			sort(V[i].begin(), V[i].end());
		}

		int ans = 0;
#define VAL(x) (V[(x)][idx[(x)]])
		while(true) {
			bool done = false;
			int largestLeft = 0;
			int smallestRight = 0;
			for (int i=0;i<N;++i) {
				if (idx[i] >= V[i].size()) {
					done = true;
					break;
				}
				if (V[i][idx[i]].first < VAL(smallestRight).first) {
					smallestRight = i;
				}
				if (V[i][idx[i]].second > VAL(largestLeft).second) {
					largestLeft = i;
				}
			}
			if (done) {
				break;
			}
			if (VAL(largestLeft).first > VAL(smallestRight).second) {
				idx[smallestRight]++;
			} else {
				++ans;
				for (int i=0;i<N;++i)idx[i]++;
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
