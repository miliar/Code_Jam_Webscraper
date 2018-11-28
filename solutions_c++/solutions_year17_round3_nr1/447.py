#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define FI first
#define SE second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

double pi=acos(-1);
int cas,n,k,maxr,r,h;
double ans,maxans;
pair<double,int> f[1100];
int main(){
#ifdef AKAISORA
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&k);
		rep(i,0,n){
			scanf("%d%d",&r,&h);
			f[i]=make_pair((double)r*2*pi*h,r);
		}
		sort(f,f+n);
		maxans=0;
		for(int i=0;i<n;i++){
			ans=0;
			maxr=f[i].second;
			int cnt=1;
			for(int j=n-1;j>=0;j--){
				if(cnt>=k)break;
				if(j!=i && f[j].second<=maxr){
					ans+=f[j].first;
					cnt++;
				}
			}
			if(cnt==k){
				ans+=f[i].first+(double)f[i].second*f[i].second*pi;
				if(ans>maxans)maxans=ans;
			}
		}
		printf("%.9f\n",maxans);
	}
	return 0;
}