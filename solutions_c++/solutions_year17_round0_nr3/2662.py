#include<bits/stdc++.h>
using namespace std;
int T;
long long a,k,A,B; 
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%lld%lld",&a,&k);
		A=1;B=0;
		while(k){
			if(k<=A+B)break;
			k-=A+B;
			if(a&1)a=a>>1,A+=A+B;
			else a=a+1>>1,B+=A+B;
		}
		printf("Case #%d: ",_);
		if(k<=A)printf("%lld %lld\n",a>>1,a-1>>1);
		else printf("%lld %lld\n",a-1>>1,a-2>>1);
	}
}
