#include<deque>
#include<queue>
#include<map>
#include<string>
#include<iostream>
#include<set>
#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
#define scanf scanf_s
#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pub push_back
using namespace std;
typedef long long int llint;
const llint one = 1;
const llint big = (one<<30);
llint solve(void){
	llint N,K,i,j,a,b;
	scanf("%lld %lld",&N,&K);
	map<llint,llint> space;//‹ó‚«‚Ì’·‚³Al‚Ì”
	space[N]+=1;
	auto it=space.begin();
	while(K>0){
		
		b=it->first;a=it->second;
		b--;
		space[b/2]+=a;
		space[b-(b/2)]+=a;
		K-=a;
		it--;
	}
	return b;
}

int main(void){
	llint a,b,T,ok,bef=0,i,j;
	auto fi=fopen("GCJC.txt","w");
	scanf("%lld",&T);
	for(a=1;a<=T;a++){
		fprintf(fi,"Case #%lld: ",a);
		b=solve();
		fprintf(fi,"%lld %lld\n",b-(b/2),b/2);
	}
	return 0;
}