#include<bits/stdc++.h>


using namespace std;

long long n;

int A[20],cnt,Ans[20];
int cas;

void Work(){
	for(int i=1;i<=cnt;i++){
		bool ok=1;
		for(int j=i+1;j<=cnt;j++){
			if(A[j]>A[i])break;
			if(A[j]<A[i])ok=0;
		}
		if(ok)Ans[i]=A[i];
		else{
			Ans[i]=A[i]-1;
			for(int j=i+1;j<=cnt;j++)Ans[j]=9;
			break;
		}
	}
	printf("Case #%d: ",++cas);
	if(Ans[1])printf("%d",Ans[1]);
	for(int i=2;i<=cnt;i++)printf("%d",Ans[i]);
	printf("\n");
}

void Init(){
	cin>>n;
	cnt=0;
	while(n){
		A[++cnt]=n%10;
		n/=10;
	}
	reverse(A+1,A+cnt+1);
}

int main(){
	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	int T;
	scanf("%d",&T);
	while(T--){
		Init();
		Work();
	}
	return 0;
}
