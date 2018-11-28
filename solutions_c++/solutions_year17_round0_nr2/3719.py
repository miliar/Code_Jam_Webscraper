#include <bits/stdc++.h>
using namespace std;

char str[30];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		scanf("%s", str+1);
		str[0]='0';
		int len=strlen(str+1);
		for(int i=2;i<=len;i++){
			if(str[i]<str[i-1]){
				for(int j=i-1;j>=1;j--){
					if(str[j]>str[j-1]){
						str[j]--;
						for(int k=j+1;k<=len;k++)str[k]='9';
						break;
					}
				}
				break;
			}
		}
		printf("Case #%d: ", t);
		bool ok=false;
		for(int i=0;i<=len;i++){
			if(str[i]!='0')ok=true;
			if(ok)printf("%c", str[i]);
		}
		printf("\n");
	}
}

