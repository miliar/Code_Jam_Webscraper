#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;
typedef long long LL;
typedef long double LD;

struct Horse{
	LL d,v;
	Horse(): d(0),v(0){}
	Horse(int d, int v): d(d),v(v){}
	bool operator<(const Horse &that)const{
		return d<that.d;
	}
};


vector<Horse> horses;
LL d, n;

bool check(double v){
	for(Horse &h:horses){
		if(v<=h.v)continue;
		if(h.v*d<h.d*v)return 0;
		// v=h.v*d/h.d
	}
	return 1;
}

void input(){
	scanf("%lld%lld",&d,&n);
	horses.resize(n);
	for(int i=0; i<n; i++){
		scanf("%lld%lld", &horses[i].d, &horses[i].v);
		horses[i].d = d-horses[i].d;
	}
}
void echo(){
	fprintf(stderr,"\n%lld %lld\n",d,n);
	for(int i=0; i<n; i++){
		fprintf(stderr, "%lld %lld\n", d-horses[i].d, horses[i].v);
	}
}
void solve(){
	// sort(horses.begin(),horses.end());
	LD ans=1011110000LL*10000;
	for(Horse &h:horses){
		ans=min(ans, LD(h.v*d)/h.d);
	}
	printf("%.6Lf\n",ans);
	// fprintf(stderr, "d %d\n", d);
}

int main(){
	int zz;
	scanf("%d",&zz);
	for(int kase=0; kase<zz; kase++){
		input();
		printf("Case #%d: ",kase+1);
		// echo();
		solve();
	}
}