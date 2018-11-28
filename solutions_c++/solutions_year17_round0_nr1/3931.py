#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
char S[1005];
int main(){
	int T,k,n;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){
		scanf("%s%d",S,&k);
		int n=strlen(S),A=0;
		for (int i=k-1;i<n;i++)
			if (S[i-k+1]=='-'){
				A++;
				for (int x=i-k+1;x<=i;x++)
					if (S[x]=='-') S[x]='+';
				              else S[x]='-';
			}
		for (int i=n-k;i<n;i++)
			if (S[i]!='+') A=-1;
		if (A!=-1)
			printf("Case #%d: %d\n",cases,A);
		else
			printf("Case #%d: IMPOSSIBLE\n",cases);
	}
	return 0;
}