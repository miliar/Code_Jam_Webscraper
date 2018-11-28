#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main() {
	int t,test;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		char s[1005];
		int k,i,j,n,ans=0;
		scanf("%s%d",s,&k);
		n = strlen(s);
		for(i=0;i<n;i++){
			//printf("i=%d s=%s\n",i,s);
			if(s[i]!='+'){
				//printf("i=%d n=%d i+k=%d\n",i,n,i+k);
				if(i+k-1<n){
					ans++;
					for(j=0;j<k;j++){
						//printf("j=%d\n",j);
						s[i+j]=(s[i+j]=='+' ? '-' : '+');
					}
				}
				else {
					ans=-2000;
				}
			}
		}
		if(ans>=0)
			printf("Case #%d: %d\n",test,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",test);
	}
	return 0;
}