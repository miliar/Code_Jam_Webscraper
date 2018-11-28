#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int T;
ll N;
ll X[20];
ll solve();
ll Y[20];
bool judge(int ind);
int main()
{
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%lld",&N);
		printf("Case #%d: %lld\n",t,solve());
	}
	return 0;
}
ll solve()
{
	int index=0;
	while(N>0){
		X[index++]=N%10;
		N/=10;
	}
	for(int i=0;i<index;i++){
		int Z=X[i];
		if(i!=0){Z--;}
		for(int k=Z;k>=0;k--){
			for(int j=0;j<i;j++){
				Y[j]=9;
			}
			Y[i]=k;
			for(int j=i+1;j<index;j++){
				Y[j]=X[j];
			}
			/*
			for(int j=index-1;j>=0;j--){
				printf("%d",Y[j]);
			}
			printf("\n");*/
			if(judge(index)){
				ll res=0;
				for(int j=index-1;j>=0;j--){
					res*=10;res+=Y[j];
				}
				return res;
			}
		}
		
	}
}
bool judge(int ind)
{
	for(int i=0;i<ind-1;i++){
		if(Y[i]<Y[i+1])return false;
	}
	return true;
}
