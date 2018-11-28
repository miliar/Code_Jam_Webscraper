#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
char S[25];
int N[25];
int main(){
	int T,n;
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out.txt","w",stdout);
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){
		scanf("%s",S);
		int n=strlen(S);
		long long A=0;
		for (int i=0;i<n;i++)
			N[i]=S[i]-'0';
		for (int i=1;i<n;i++)
			if (N[i]<N[i-1]){
				for (int j=i;j<n;j++) N[j]=9;
				N[i-1]--;
				int x=i-1;
				while (x && (N[x]<0 || N[x]<N[x-1])){
					N[x]=9;
					N[x-1]--;
					x--;
				}
				break;
			}
		for (int i=0;i<n;i++)
			A=A*10+N[i];
		printf("Case #%d: %lld\n",cases,A); 
	}
	return 0;
}