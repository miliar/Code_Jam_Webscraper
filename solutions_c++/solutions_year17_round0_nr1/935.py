#include<iostream>
using namespace std;
int main(){
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		string s;
		int k;
		cin>>s>>k;
		int ans=0;
		for(int i=0;i<s.length()-k+1;i++){
			if(s[i]=='-'){
				ans++;
				for(int j=0;j<k;j++){
					if(s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				}
			}
		}
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				ans=-1;
				break;
			}
		}
		if(ans==-1)
		cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
