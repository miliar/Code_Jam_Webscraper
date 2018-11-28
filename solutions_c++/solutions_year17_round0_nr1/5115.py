#include <bits/stdc++.h>

using namespace std;

int strlen(char A[]){
    int c = 0;
    while(A[c]!='\0' && A[c]!='\n') c++;
    return c;
}


int main(){

	int t,k,n;
	scanf("%d",&t);
	for(int cases=1;cases<=t;cases++){
		char A[1001];
		scanf("%s",A);
		scanf("%d",&k);	
		n = strlen(A);
		int answer = 0;
		for(int i=0;i+k<=n;i++){
			if(A[i]=='-'){
				answer++;
				A[i] = '+';
				for(int j=i+1;j<i+k;j++){
					if(A[j]=='+') A[j] = '-';
					else A[j] = '+';
				}
			}
		}
		for(int i=n-k;i<n;i++)
			if(A[i]=='-')
				answer = -1;

		printf("Case #%d: ",cases);

		if(answer==-1){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n",answer);
		}
	}
	


	return 0;
}