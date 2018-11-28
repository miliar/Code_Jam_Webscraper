#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	// your code goes here
	int t,test;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		char s[20];
		scanf("%s",s);
		int n = strlen(s),i;
		for(i=1;i<n;i++){
			if(s[i]<s[i-1]){
				s[i-1]--;
				int idx = i-1;
				while(idx-1>=0){
					//printf("idx = %d s[idx-1]=%c s[idx]=%c\n",idx,s[idx-1],s[idx]);
					if(s[idx-1] > s[idx]){
						s[idx-1]--;
						s[idx]='9';
						idx--;
					}
					else{
						break;
					}
				}
				for(;i<n;i++){
					s[i]='9';
				}
			}
		}
		if(s[0] != '0')
			printf("Case #%d: %s\n",test,s);
		else
			printf("Case #%d: %s\n",test,s+1);
	}
	return 0;
}