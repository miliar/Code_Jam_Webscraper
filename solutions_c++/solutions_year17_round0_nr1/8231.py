#include <bits/stdc++.h>
using namespace std;
int main(){
	int test;cin>>test;
	string s,t;int k,n;
	for(int te=1;te<=test;te++){
		cin>>s>>k;
		n=s.size();
		bool sw=1;
		int c=0;
		int i=0;
		while(i<=n-k){		
			for(i=0;i<n;i++){
				if(s[i]=='-')break;
			}
			if(i<=n-k){
				c++;
				for(int j=0;j<k;j++){
					if(s[i+j]=='-')s[i+j]='+';
					else s[i+j]='-';
				}				
			}
		}
		for(int i=0;i<n;i++)
				if(s[i]=='-')sw=0;
		if(sw){
			printf("Case #%d: %d\n",te,c );
		}else{
			printf("Case #%d: IMPOSSIBLE\n",te );
		}
	}
	return 0;
}