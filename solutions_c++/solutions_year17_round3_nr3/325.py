#include<bits/stdc++.h>
using namespace std;
const int maxn=90;
int n,k;
double p[maxn];
double u;
const double eps=1e-9;
int sgn(double x){
	return (x>eps)-(x<-eps);
}
void print(){
	for(int i=1;i<=n;i++)
		printf("%.3f%c",p[i]," \n"[i==n]);
}
void solve(){
	cin>>n>>k;
	cin>>u;
	for(int i=1;i<=n;i++)
		cin>>p[i];
	sort(p+1,p+1+n);
	p[n+1]=1;
	double ans=1;
	int dd=0;
	while(1){
		if(sgn(u)==0)break;
		int cur=1;
		while(cur<=n&&!sgn(p[cur]-p[1]))cur++;
		cur--;
		double d=p[cur+1]-p[cur];
		int len=cur;
		if(cur*d-eps<=u){
			u-=cur*d;
			for(int i=1;i<=cur;i++)p[i]+=d;
		}else{
			d=u/cur;
			for(int i=1;i<=cur;i++)p[i]+=d;
			break;
		}
//		print();
	}
	print();
	for(int i=1;i<=n;i++)ans*=p[i];
	printf("%.10f\n",ans);
}

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
