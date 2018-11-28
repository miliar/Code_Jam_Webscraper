#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#define max(a,b) (a>b?a:b)
#define ll long long
#include<iostream>
#include<iomanip>
struct pancake{
	double r,h;
};
bool cmp(pancake a,pancake b){
	if ( (a.r*a.h) > (b.r*b.h) ) return true;
	if ( (a.r*a.h) < (b.r*b.h) ) return false;
	return a.r < b.r;
}
double rd(pancake a){
	return 2*M_PI*a.r*a.h;
}
double area(pancake a){
	return M_PI*a.r*a.r;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("wz","w",stdout);
	int T;
	scanf("%d",&T);
	for(int xx=1;xx<=T;xx++){
		int n,k;
		scanf("%d%d",&n,&k);
		pancake P[1000];
		for(int i=0;i<n;i++){
			scanf("%lf%lf",&P[i].r,&P[i].h);
		}
		double ans=0.0,now=0,fin=0;
		std::sort(P,P+n,cmp);
		for(int j=0;j<k-1;j++){
			ans += rd(P[j]);
			now = max(now , P[j].r);
		}
		for(int i=k-1;i<n;i++){
			double tR= max(P[i].r,now);
			fin = max(fin , ans + rd(P[i]) + tR*tR*M_PI);
		}
		printf("Case #%d: ",xx);
		std::cout << std::fixed << std::setprecision(9) << fin << std::endl;
	}
	return 0;
}
