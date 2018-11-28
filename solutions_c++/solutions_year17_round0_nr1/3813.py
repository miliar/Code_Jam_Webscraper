#include<bits/stdc++.h>
using namespace std;
string str;
int k;
int main(){
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		cin>>str>>k;   
		int len=str.length(),ans=0;
		for(int i=0;i<=len-k;i++){
			if(str[i]=='-'){
				ans++;
				for(int j=0;j<k;j++){
					if(str[i+j]=='-')
						str[i+j]='+';
					else
						str[i+j]='-';
				}
			}
		}
		bool flag=true;
		for(int i=0;i<len;i++){
			if(str[i]=='-'){
				flag=false;
				break;
			}
		}
		printf("Case #%d: ",++cas);
		if(flag)
			printf("%d\n",ans);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
} 
