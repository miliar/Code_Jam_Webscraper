#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
	 freopen("B-large.in", "r", stdin);
	 freopen("answer-large.out", "w", stdout);
	int t,curr=0;
	cin>>t;
	while(curr++ < t){
		string s;
		cin>>s;
		
		while(1){
			//cout<<s<<"\n";
			bool flag=true;
		for(int i=0;i<s.size()-1;i++){
			if(s[i]>s[i+1]){
				flag=false;
				break;
			}
		}
		if(flag){
			cout<<"Case #"<<curr<<": "<<s<<"\n";break;
		}
		else{
			bool flag2=true;
			for(int i=0;i<s.size();i++){
			if(s[i]=='0' || s[i]=='1'){
			}
			else {flag2=false;break;}
		}
		if(flag2){
			string t="";
						for(int j=0;j<s.size()-1;j++) t+='9';
							s=t;
		}
		else{
		for(int i=0;i<s.size()-1;i++){
			if(s[i]>s[i+1]){
				if(s[i]!='1'){//not starting with 1
					s[i]=s[i]-1;
					for(int j=i+1;j<s.size();j++) s[j]='9';
					break;
				}
				else{
					if(i!=0){
						s[i]='0';
					for(int j=i+1;j<s.size();j++) s[j]='9';
					break;
					}
					else{
						string t="";
						for(int j=0;j<s.size()-1;j++) t+='9';
							s=t;
						break;
					}
				}
			}
		}
	}
	}
}
		
	}
	return 0;
}