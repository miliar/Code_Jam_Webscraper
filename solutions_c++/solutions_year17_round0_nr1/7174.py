#include <iostream>
#include<string.h>
using namespace std;

int main() {
	// your code goes here
	int t,n,k;
	string str;
	cin>>t;
	
	for(int test=1;test<=t;test++){
		int moves=0;
		cin>>str>>k;
		//cout<<str<<" "<<k;
		int len = str.length();
		for(int i=0;i<=len-k;i++){
			if(str[i]=='-'){
				moves++;
				for(int ii=i;ii<i+k;ii++){
					str[ii]=(str[ii]=='+'?'-':'+');
				}
			}
		}
		bool result=true;
		for(int i=len-k+1;i<len;i++)
			if(str[i]=='-'){
				result = false;
				break;
			}				
		if(result)
		cout<<"Case #"<<test<<": "<<moves<<endl;
		else
		cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
	}
	
	
	return 0;
}