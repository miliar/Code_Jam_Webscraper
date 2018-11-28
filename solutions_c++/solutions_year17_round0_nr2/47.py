#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
long long n;
int A[50],len,B[50];
void solve(){
	scanf("%lld",&n); len=0;
	while (n){
		A[++len]=n%10; n/=10;
	}
	for (int i=0;i<=len;i++){
		for (int j=len;j>i;j--) B[j]=A[j];
		B[i]=A[i]-1;
		for (int j=1;j<i;j++) B[j]=9;
		int flag=0;
		for (int i=1;i<len;i++) if (B[i]<B[i+1]) flag=1;
		if (flag==0){
			long long ans=0;
			for (int i=len;i;i--) ans=ans*10+B[i];
			printf("%lld\n",ans); return;
		}
	}
}
int main(){
	freopen("Bl.in","r",stdin);
	freopen("Bl.out","w",stdout);
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i); solve();
	}
	return 0;
}
