#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define FI first
#define SE second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

double eps=1e-8;
double ans,u,tmp,p[60];
int cas,n,k;

pair<double,int> f[1100];
int main(){
#ifdef AKAISORA
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&k);
		scanf("%lf",&u);
		rep(i,0,n)scanf("%lf",&p[i]);
		priority_queue<double,vector<double> ,greater<double> > Q;
		rep(i,0,n)Q.push(p[i]);
		while(u>eps){
			tmp=Q.top();Q.pop();
			tmp+=0.0001;
			u-=0.0001;
			Q.push(tmp);
		}
		ans=1;
		while(!Q.empty()){
			ans*=Q.top();
			Q.pop();
		}
		printf("%.8f\n",ans);
	}
	return 0;
}