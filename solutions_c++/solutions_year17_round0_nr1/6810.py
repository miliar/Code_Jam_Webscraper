#include<bits/stdc++.h>
using namespace std;
char s[2000];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
    int t,i,j,k,z,coun,len;
    scanf("%d",&t);
    for(z=1;z<=t;z++){
		coun=0;
        scanf(" %s %d",s,&k);
        len= strlen(s);
        for(i=0;i<=len-k;i++){
            if(s[i]=='-'){
				coun++;
                for(j=i;j<=i+k-1;j++){
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
                }
            }
        }
		int ch=1;
		for(i=len-k+1;i<len;i++)
			if(s[i]!='+'){
				ch=0;
				break;
			}
        if(ch) printf("Case #%d: %d\n",z,coun);
		else printf("Case #%d: IMPOSSIBLE\n",z);
    }
    return 0;
}
