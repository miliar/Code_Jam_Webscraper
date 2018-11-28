#include <stdio.h>
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
int N, D, K[1005], S[1005];

int main() {
	int T=INT();
	for (int t=1;t<=T;++t) {
		D=INT();N=INT();
		for(int i=0;i<N;++i){K[i]=INT();S[i]=INT();}

		vector<pii> v;
		for(int i=0;i<N;++i)v.push_back(pii(K[i],S[i]));
		sort(v.begin(),v.end());

#define f(x) (1.0*(D-v[(x)].first)/v[(x)].second)
		double maxTime = f(N-1);
		for (int i=N-2; i >= 0; --i) {
			maxTime = max(maxTime, f(i));
		}

		printf("Case #%d: %.8lf\n", t, D/maxTime);
	}
	return 0;
}
