#include<bits/stdc++.h>
using namespace std;
main(){
	int T,i,k;
	char s[100];
	freopen("B-large.in","r",stdin);
	freopen("outputBlarge.out","w",stdout);
	scanf("%d",&T);
	for(k=1;k<=T;k++){
		scanf("%s",s);
		int l=strlen(s);
		int index=-1;
		for(i=1;i<l;i++){
			if(s[i]<s[i-1]){
				index=i;
				break;
			}
		}
		while(index!=-1){
			for(i=index;i<l;i++){
				s[i]='9';
			}
			//printf("%s\n",s);
			if(s[index-1]=='0'){
				for(i=index-1;i>0;i--){
					if(s[i]=='0'){
						s[i]='9';
					}
					else{
						s[i]--;
						break;
					}
				}
			}
			else s[index-1]--;
			index=-1;
			for(i=1;i<l;i++){
				if(s[i]<s[i-1]){
					index=i;
					break;
				}
			}
		}
		long long num=0;
		for(i=0;i<l;i++){
			num*=10;
			num+=(s[i]-'0');
		}
		printf("Case #%d: %lld\n",k,num);
	}
}
