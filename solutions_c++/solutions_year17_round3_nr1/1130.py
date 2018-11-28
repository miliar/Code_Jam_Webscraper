#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define pp pair<double,double>
#define PI 3.14159265358979323846
double sq(double r){
	return r*r;
}
double bottomArea(double r){
	return PI * sq(r);
}
double heightArea(double r,double h){
	return 2*PI*r*h;
}
int main() {
	int t,test;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		double ans = 0;
		int n,k,i,j;
		vector<pp> G;
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++){
			double r,h;
			scanf("%lf%lf",&r,&h);
			G.push_back(pp(r,h));
			
		}
		sort(G.begin(),G.end());
		for(i=n-1;i>=0;i--){
			double local_ans = bottomArea(G[i].first) + heightArea(G[i].first,G[i].second);
			//printf("#1 i=%d local_ans=%lf\n",i,local_ans);
			vector<double> L;
			for(j=i-1;j>=0;j--){
				L.push_back(heightArea(G[j].first,G[j].second));
			}
			if(L.size()<k-1){
				break;
			}
			sort(L.begin(),L.end());
			int count = k-1;
			for(j=i-1;j>=0 && count;j--){
				count--;
				local_ans+= L[j];
			}
			//printf("#2 i=%d local_ans=%lf\n",i,local_ans);
			ans = max(ans, local_ans);
		}
		printf("Case #%d: %0.9lf\n",test,ans);
	}
	return 0;
}