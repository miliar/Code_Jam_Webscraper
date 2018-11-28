#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{					
	ll k,count,tc,flag;
	string str;
	cin>>tc;
	for(int t=1;t<=tc;t++){
		cin>>str;
		cin>>k;
		count=0;
		flag=0;
		for(int i=0;i+k<=str.length();i++){//
			if(str[i]=='-'){
				count++;
				for(int j=0;j<k;j++){
					if(str[i+j]=='-'){
						str[i+j]='+';
					}
					else{
						str[i+j]='-';
					}
				}
			}
		}
		for(int i=0;i<str.length()&&flag==0;i++){
			if(str[i]=='-'){
				flag=1;
			}
		}
		cout<<"Case #"<<t<<": ";
		if(flag==1){
			cout<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<count<<endl;
		}
	}
	return 0;
}