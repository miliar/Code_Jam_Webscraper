#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("output.txt","w",stdout);
	int n,len;
	char s[20];
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%s",s);
		len=strlen(s);
		/*if(strcmp(s,"10")==0) printf("Case #%d: 9\n",i);
		else if(strcmp(s,"100")==0) printf("Case #%d: 99\n",i);
		else if(s[0]=='9' && len==3) printf("Case #%d: 899\n",i);
		else if(strcmp(s,"1000")==0) printf("Case #%d: 999\n",i);
		else{*/
			
			for(int j=len-1;j>=1;j--){
				if(s[j]<s[j-1]){
					s[j-1]--;
					for(int k=j;k<len;k++) s[k]='9';
				}
			}
			printf("Case #%d: ",i);
			for(int j=0;j<len;j++){
				if(s[j]!='0') printf("%c",s[j]);
			}
			printf("\n");				
		//}
	}
	return 0;
}
