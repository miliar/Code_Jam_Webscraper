#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <cstring>
#include <set>
#include <map>
using namespace std;

int N,D;

void solve(){
	scanf("%d%d", &D, &N);
	double time_ = 0.0;
	for (int i=0;i<N;i++){
		int k,s;
		scanf("%d%d",&k,&s);
		double time_need = (double)(D - k)/(double)s;
		time_ = max(time_, time_need);
	}

	double vel = (double) D / time_;
	printf("%.9lf\n", vel);
}

int main(){
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}