#include <bits/stdc++.h>
using namespace std;

int t,n;

int main(){
	freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		double d;
		scanf("%lf%d",&d,&n);
		int k,s;
		double ans=0;
		for(int i=0;i<n;i++){
			scanf("%d%d",&k,&s);
			double tmp = (d-k)/s;
			ans=max(ans,tmp);
		}
		if(ans!=0) ans = d/ans;
		printf("Case #%d: %lf\n",tc,ans);
	}
}
