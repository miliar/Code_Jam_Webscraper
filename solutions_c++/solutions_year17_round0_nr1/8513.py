#include <iostream>
#include <string.h>
using namespace std;

int main() {
    int i,t,j,k,flag,ans,flag0,flag1;
    string s;
	cin>>t;
	for(j=1;j<=t;j++){
	    cin>>s>>k;
	    if(k>s.length())
	    cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
	    else{
	    ans=flag=flag1=flag0=0;
	    for(i=0;i<s.length()-k+1;i++){
	        if(s[i]=='+')
	        continue;
	        if(s[i]=='-'){
	        ans++;
	        for(int l=i;l<k+i;l++)
	        if(s[l]=='+')
	        s[l]='-';
	        else
	        s[l]='+';
	        }
	    }
	    flag1=1;
	    for(int m=i;m<s.length();m++)
	    if(s[m]=='-')
	        flag1=0;
	    if(flag1)
	    cout<<"Case #"<<j<<": "<<ans<<endl;
	    else
	    cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
	}
	}
	return 0;
}
