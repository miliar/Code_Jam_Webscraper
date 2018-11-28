#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstring>
using namespace std;
char s[10005];
int T,rec;
bool flag;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		rec=0;
		flag=true;
//		printf("Case #%d: ",t);
		scanf("%s",s);
		for(int i=1;i<strlen(s);i++){
			if(s[i]<s[i-1]){
				flag=false;
				break;
			}
			else if(s[i]!=s[i-1]) rec=i;
		}
		if(flag){
			 printf("Case #%d: %s\n",t,s);
		}
		else{
			printf("Case #%d: ",t);
			s[rec]--;
			for(int i=rec+1;i<strlen(s);i++) s[i]='9';
			for(int i=0;i<strlen(s);i++){
				if(s[i]=='0'){
					if(!flag) continue;
				}
				else flag=true;
				printf("%c",s[i]);
			}
			printf("\n");
		}
	}
	return 0;
}
