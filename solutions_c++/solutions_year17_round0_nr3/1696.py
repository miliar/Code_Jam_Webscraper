#include<bits/stdc++.h>
using namespace std;
int T;
long long N,K,num,s1,s2,l1,l2,ans;
int main(){
	freopen("bathroom.in","r",stdin);
	freopen("bathroom.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		scanf("%lld%lld",&N,&K);
		s1=N; s2=1; l1=0; l2=0; num=1;
		while (K>num){
			K-=num;
			num*=2;
			if (s1%2==0){
				l1=s1/2;
				s1=(s1-1)/2;
				l2=l2*2+s2;
			} else {
				s1=(s1-1)/2;
				s2*=2;
				if (l1!=0){
					l1/=2;
					s2+=l2;
				}
			}
			//			printf("%lld %lld    %lld %lld\n",s1,s2,l1,l2);

		}
		if (K<=l2) ans=l1;
		else ans=s1;
		printf("Case #%d: %lld %lld\n",i,ans/2,(ans-1)/2);
	}
	return 0;
}
