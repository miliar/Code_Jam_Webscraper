#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<math.h>
using namespace std;
int T;
typedef pair<double,double> pii;

void Gao(){
	scanf("%d",&T);
	for(int t = 1;t<=T;t++){
		double k;
		int n;
		scanf("%lf%d",&k,&n);
		vector<pii> a;
		for(int i=0;i<n;i++){
			double st, speed;
			scanf("%lf%lf",&st,&speed);
			a.push_back(make_pair(st,speed));
		}
		double maxx=0;
		for(int i=0;i<n;i++){
			double dis = k-a[i].first;
			double tt = dis/a[i].second;
			double temMax = k/tt;
			if(i==0){
				maxx = temMax;
			}
			maxx= min(temMax,maxx);
		}
		printf("Case #%d: %.6lf\n",t,maxx);
	}
} 
int main(){
	freopen("A-large.in","r",stdin);
	freopen("alarge.out","w",stdout);
	Gao();
	return 0;
} 
