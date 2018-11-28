#include <bits/stdc++.h>
using namespace std;
double t;
int d,n,s,k;

int main(){
	freopen("input.txt","r",stdin);
	int tt,i;
	scanf("%d",&tt);
	for(i=1;i<=tt;i++){
		printf("Case #%d: ",i);
		scanf("%d %d",&d,&n);
		t=0.0;
		while(n--){
			scanf("%d %d",&k,&s);
			t=max(t,(double)(d-k)/s);
		}
		printf("%lf\n",d/t);
	}

	return 0;
}
