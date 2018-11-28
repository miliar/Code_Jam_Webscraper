#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{   freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    int T,K;
    char S[1010];
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
    	scanf("%s %d",&S,&K);
    	int ans=0,len=strlen(S);
    	bool flag=true;
    	for(int i=0;S[i]!='\0';i++){
    		
    		if(S[i]=='-'){
    			int p=i+K-1;
    			if(p<len){
    				ans++;
    				for(int j=i;j<=p;j++){
    					if(S[j]=='-') S[j]='+';
    					else S[j]='-';
					}
    				
				}else{
					flag=false;
					break;
				}
			}
		}
    	if(flag)
    	printf("Case #%d: %d\n",t,ans);
    	else
    	printf("Case #%d: IMPOSSIBLE\n",t);
	}
   return 0;   
}
