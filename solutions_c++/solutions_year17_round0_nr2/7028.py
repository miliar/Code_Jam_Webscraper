#include<iostream>
#include<string>
using namespace std;

int main(){
	int t;
	cin>>t;
	int cnt=0;
	while(t>cnt++){
		string s;
		cin>>s;
		for(int i=s.size()-1;i>0;i--){
			if(s[i]<s[i-1]){
				int tmp=i-1;
				while(1){
					if(s[tmp]>0){s[tmp]=s[tmp]-1;break;}
					else s[tmp--]='9';
				}
				for(int j=i;j<s.size();j++)s[j]='9';
			}
		}
		cout<<"Case #"<<cnt<<": ";
		for(int i=0;i<s.size();i++)if(s[i]!='0')cout<<s[i];
		cout<<endl;
	}
}
