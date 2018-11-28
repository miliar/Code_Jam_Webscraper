#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T,l,n,x,y;
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		double mx = 0;
		scanf("%d%d",&l,&n);
		for (int i=1;i<=n;i++) {
			scanf("%d%d",&x,&y);
			mx=max(mx,(l-x)*1.0/y);
		}
		printf("Case #%d: %lf\n",_,l/mx);
	}
	return 0;
}
