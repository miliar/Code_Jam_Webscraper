#include<bits/stdc++.h>
using namespace std;
char s[30];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("BLarge.out","w",stdout);
	int t,z,i,j,len,ch;
	scanf("%d",&t);
	for(z=1;z<=t;z++){
        scanf(" %s",s);
		len=strlen(s);
		ch=1;
        while(ch){
            for(i=0;i<len-1;i++){
                if(s[i]-'0' > s[i+1]-'0'){
                    s[i]=s[i]-1;
                    for(j=i+1;j<len;j++)
						s[j]='9';
                }
            }
            ch=0;
            for(i=0;i<len-1;i++)
				if(s[i]-'0' > s[i+1]-'0')
					ch=1;
        }
        printf("Case #%d: ",z);
		for(i=0;i<len;i++)
			if(s[i]!='0')
				printf("%c",s[i]);
		printf("\n");
	}
    return 0;
}
