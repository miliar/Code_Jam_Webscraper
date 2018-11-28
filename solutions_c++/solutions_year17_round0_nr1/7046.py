#include<iostream>
#include<string>
using namespace std;

int main(){
	int t;
	cin>>t;
	int cnt=0;
	while(t>cnt++){
		int ans=0;
		string s;
		cin>>s;
		int k;
		cin>>k;
		for(int i=0;i<s.size();i++){
			for(int j=0;j<s.size();j++){
				if(s[j]=='-' && j+k-1<s.size()){
					for(int l=0;l<k;l++)s[j+l]=(s[j+l]=='+')?'-':'+';
					ans++;
					break;
				}
			}
		}
		bool f=true;;
		for(int i=0;i<s.size();i++)if(s[i]=='-')f=false;
		cout<<"Case #"<<cnt<<": ";
		if(f)cout<<ans<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}
