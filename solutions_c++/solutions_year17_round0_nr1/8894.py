#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, k;
	char s[1005];
	cin>>t;
	for(int i=1;i<=t;i++){
		scanf("%s %d",s,&k);
		int l=strlen(s); int count=0, f=0;
		for(int j=0;j<l;j++){
			if(s[j]=='-'){
				if(j+k-1<l){
					for(int x=j;x<j+k;x++){
						if(s[x]=='+') s[x]='-';
						else s[x]='+';
					}
					++count;
				}
				else {
					f=1;
					break;
				}
			}
		}
		printf("Case #%d: ",i);
		if(f) printf("IMPOSSIBLE");
		else printf("%d",count);
		printf("\n");
	}
	return 0;
}