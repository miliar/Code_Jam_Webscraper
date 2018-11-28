#include<bits/stdc++.h>
using namespace std;

int main(){
	freopen("cjam2.in","r",stdin);
	freopen("cjam2.out","w",stdout);
	int t;
	cin>>t;
	for(int te=1;te<=t;te++){
		char charind='*';int ind=50; string s;int flag=0;
		cin>>s;
		for(int i=0;i<s.length()-1;i++){
			if((s[i]-'0')>(s[i+1]-'0')){
				ind=i;charind=s[ind];
				if(s[i]=='1'){
					flag=1;
				}
				break;
			}
		}
		for(int i=ind+flag+1;i<s.length();i++){
			s[i-flag]='9';
		}
		for(int i=ind;i>=0;i--){
			if(s[i]==charind && charind!='1' && (i==0 || s[i-1]!=charind))
				s[i]=(char)(s[i]-1);
			else if(s[i]==charind)
				s[i]='9';
			else
				break;
		}
		cout<<"Case #"<<te<<": ";
		for(int i=0;i<s.length()-flag;i++)
			cout<<s[i];
		cout<<'\n';
	}
	return 0;
}
