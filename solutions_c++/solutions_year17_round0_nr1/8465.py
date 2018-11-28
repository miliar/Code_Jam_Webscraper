#include <bits/stdc++.h>
using namespace std;

int main() {
    int t,T,i,j,k,ans;
    string str;
	cin>>T;
	for(t=1;t<=T;t++)
	{
	    cin>>str>>k;
	    i=0;
	    ans=0;
	    for(;i<(str.length()-k+1);){
	        while(i<(str.length()-k)){
	            if(str[i]=='-')break;
	            i++;
	        }
	        if(str[i]=='-'){
	            ans++;
    	        for(j=0;j<k;j++){
    	            if(str[i+j]=='-')str[i+j]='+';
    	            else if(str[i+j]=='+')str[i+j]='-';
    	        }
    	        }
    	        i++;
	    }
	    int flag=0;
	    for(j=0;j<k;j++){
	        if(str[str.length()-j-1]=='-'){flag++;break;}
	    }
	    if(flag==0)
	        printf("Case #%d: %d\n",t,ans);
	    else
	        printf("Case #%d: IMPOSSIBLE\n",t);
	}
	return 0;
}

