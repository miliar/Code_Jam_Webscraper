#include <bits/stdc++.h>
using namespace std;

char S[1010];
int A[1010];
int n,k;

void flip(int p){
	for(int i=0;i<k;i++){
		A[i+p]=(A[i+p]+1)%2;
	}
}

int check(){
	for(int i=0;i<n;i++){
		if(A[i]==0) return(0);
	}
	return(1);
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%s",S);
		scanf("%d",&k);
		n=strlen(S);
		for(int i=0;i<n;i++){
			if(S[i]=='+') A[i]=1;
			else A[i]=0;
		}
		int res=0;
		for(int i=0;i+k-1 < n; i++){
			if(A[i]==0){
				flip(i);
				res++;
			}
		}
		if(check()) printf("Case #%d: %d\n",t,res);
		else printf("Case #%d: IMPOSSIBLE\n",t);
	}
}