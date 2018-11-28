#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		string s,ans;
		cin>>s;
		//sort(tmp.begin(),tmp.end());
		if(s.length()==1) ans=s;
		else {
			int ff=0;
			while(ff==0){
			if(ff==1) break;
			int fi=-1,li=-1,flag=0;
			for(int i=0;i<s.length()-1;i++){
				if(flag==1) break;
				if(s[i]>s[i+1]) {
					fi=i;li=i+1;
					flag=1;
					}
				}
			if(flag==0) ff=1;
			if(fi==-1&&li==-1) ans=s,ff=1;
			else if(s[fi]=='1'&&s[li]=='0'){
				for(int j=0;j<s.length()-1;j++) ans+='9';
				ff=1;
				}
			else{
				int val=s[fi]-'0';
				--val;
				char c=val+'0';
				s[fi]=c;
				for(int j=li;j<s.length();j++) s[j]='9';
				ans=s;
				}
			if(ff==1) break;
			}
			}
		cout<<"Case #"<<t<<": ";
		cout<<ans<<endl;
		}
	return 0;
	}
