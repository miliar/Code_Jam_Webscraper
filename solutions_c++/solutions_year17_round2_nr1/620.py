#include <bits/stdc++.h>
#define pi acos(-1.0)
using namespace std;
int n,m;
int k[1005],s[1005];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while(T--){ 
		int l,n;
		scanf("%d%d",&l,&n);
		for (int i=1;i<=n;i++)
			scanf("%d%d",&k[i],&s[i]);
		double t = 0;
		for (int i=n;i;i--){
			t = max(t, (double)(l-k[i])/((double)s[i]));
		}
		printf("Case #%d: %.10f\n",++ca,double(l)/t );
		
	}
	return 0;
}