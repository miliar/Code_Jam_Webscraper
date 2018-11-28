#include<bits/stdc++.h>
using namespace std;
pair<double,double> a[1000];
bool catch_(int h1,int h2,double des){
	double d=1e11;
	if(a[h1].second>a[h2].second)
		d=((a[h2].first-a[h1].first)*a[h2].second)/(a[h1].second-a[h2].second);
	return (d+a[h2].first<des);
	//return 0;

}
int main(){
	freopen("A-large.in","r",stdin);
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		int n;
		double d;
		scanf("%lf%d",&d,&n);
		for(int i=0;i<n;i++)
			scanf("%lf%lf",&a[i].first,&a[i].second);
		sort(a,a+n);
		//cur=a[0];
		//idx=0;
		//while(catch_(idx,idx+1,d))idx++;
		double time=-1;
		for(int i=n-1;i>=0;i--){
			time=max(time,(d-a[i].first)/a[i].second);
		}
		double s=d/time;
		printf("Case #%d: %.6lf\n",T,s);
	}

}
