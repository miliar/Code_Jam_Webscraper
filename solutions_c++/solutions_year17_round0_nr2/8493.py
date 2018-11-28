#include<cstdio>

void f(int n){
	long long a;
	int t[20];
	for(int i=0;i<20;i++)t[i]=0;
	scanf("%lld",&a);
	int l=0;
	while(a){
		t[l++]=a%10;
		a/=10;
	}
	int j=0;
	for(int i=1;i<l;i++){
		if(t[i]>t[i-1]){
			t[i]--;
			for(;j<i;j++)t[j]=9;
		}
	}
	
	if(!t[l-1])l--;
	printf("Case #%d: ",n);
	for(int i=l-1;i>=0;i--)printf("%d",t[i]);
	printf("\n");
}

main(){
	int a;
	scanf("%d",&a);
	for(int i=1;i<=a;i++)f(i);
}
