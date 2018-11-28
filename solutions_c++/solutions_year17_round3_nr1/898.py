#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>

using namespace std;

const int INF=1e9+10;
const double pi=3.14159265358979323846264338;

bool ord(pair <double,double> a,pair <double,double> b){
	if( a.first*a.second != b.first*b.second ) return a.first*a.second > b.first*b.second;
	else return a.first>b.first;
}

int t,n,k;

pair <double,double> pan[1024];

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		scanf("%d %d",&n,&k);
		for(int i=0;i<n;i++) scanf("%lf %lf",&pan[i].first,&pan[i].second);
		sort(pan,pan+n,ord);
		
//		for(int i=0;i<n;i++) printf("%lf %lf\n",pan[i].first,pan[i].second);
		
		double maxr=0,sumh=0,resp=0;
		for(int i=0;i<k-1;i++){
			sumh+=2*pan[i].first*pan[i].second;
			maxr=max(maxr,pan[i].first);
		}
		for(int i=k-1;i<n;i++){
			resp=max( resp , pi * (max(maxr,pan[i].first)*max(maxr,pan[i].first) + 2*pan[i].second*pan[i].first + sumh ) );
		}
		printf("Case #%d: %lf\n",tt,resp);
	}
	return 0;
}
