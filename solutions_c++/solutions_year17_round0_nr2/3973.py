#include <bits/stdc++.h>
using namespace std;

int main(){

	freopen("input.txt","r",stdin);
	// freopen("p1A_17_output.txt","w",stdout);
	freopen("p1A_17_outputLarge.txt","w",stdout);

	int t,j;
	long long int n,x;

	scanf("%d",&t);

	for(int i=1;i<=t;i++){

		char s[25]="";
		// printf("%s ",s);

		scanf("%lld",&n);

		x = n;
		j = 0;

		while(n > 0){
			s[j++] = n%10 + '0';
			n /= 10;
		}
		// printf("%s ",s);

		for(j = 0; j < strlen(s) - 1; j++){
			if(s[j]<s[j+1]){
				// printf("horray\n");
				break;
			}
		}

		if(j<strlen(s)-1){
			n=strlen(s);
			for(j=0;j<n-1;j++){
				if(s[j]<='0'){
					s[j+1] = s[j+1]-1;
					for(int k=j;k>=0;k--)
						s[k]=9+'0';
				}
				if(s[j]<s[j+1]){
					s[j+1] = s[j+1]-1;
					for(int k=j;k>=0;k--)
						s[k]=9+'0';
				}
			}
			x=0;
			if(s[n-1]=='0'){
				for(j=0;j<n-1;j++)
					x=x*10+9;
			}else{
				for(j=n-1;j>=0;j--)
					x=x*10+s[j]-'0';
			}
		}
		printf("Case #%d: %lld\n",i,x);
	}
	return 0;
}