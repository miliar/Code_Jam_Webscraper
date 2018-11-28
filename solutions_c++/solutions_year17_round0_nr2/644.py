#include <cstdio>

int S[33],P[33];
int n,p,i,j,f,t;
long long a;

int main()
{
//	freopen("output.txt","w",stdout);

	scanf("%d",&n);

	for(t=1;t<=n;t++){
		scanf("%lld",&a);
		for(p=0;a;a/=10) S[++p] = a%10;
		for(i=p;i>=1;i--){
			for(f=0,j=i-1;j>=1;j--){
				if(S[j]>S[i]) break;
				else if(S[j]<S[i]) f=1;
			}
			if(f){
				P[i] = S[i]-1;
				break;
			}
			else P[i] = S[i];
		}
		for(i--;i>=1;i--) P[i] = 9;
		for(i=p;P[i]==0;i--);
		printf("Case #%d: ",t);
		for(;i>=1;i--) printf("%d",P[i]);
		printf("\n");
	}

	return 0;
}