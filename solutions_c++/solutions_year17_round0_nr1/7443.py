#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
int main(){
	int t,k,l,ans,flag;
	scanf("%d",&t);
	for(int t1=1; t1<=t; t1++){
	char s[1005];
		ans = 0;
		flag = 0;
		scanf("%s",s);
		scanf("%d",&k);
		l = strlen(s);
		for(int i=0; i<l; ){
			if(s[i] == '+'){
				i++;
				continue;
			}
			if(i<l && s[i]=='-' && i+k-1>=l){
				flag = 1;
				break;
			}
			for(int j=i; j<=i+k-1; j++){
				if(s[j] == '-'){
					s[j] = '+';
				}else{
					s[j] = '-';
				}
			}
			ans++;
			i++;
		}
		printf("Case #%d: ",t1);
		if(flag == 1){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n",ans);
		}
	}
	return 0;
}