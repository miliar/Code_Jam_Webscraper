#include <bits/stdc++.h>
using namespace std;
string s;
int k;
int cnt;
		
void flipper(int ind){
	for(int i=ind;i>ind-k;i--){
		s[i]=='+'?s[i]='-':s[i]='+';
		}
	++cnt;
	}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>s;
		cin>>k;
		int flag=0;
		cnt=0;
		for(int i=s.length()-1;i-(k-1)>=0;i--){
			if(s[i]=='-') flipper(i);
			}
		for(int i=0;i<s.length();i++) if(s[i]=='-') flag=1;
		cout<<"Case #"<<t<<": ";
		flag==0?cout<<cnt<<endl:cout<<"IMPOSSIBLE"<<endl;
		}
	return 0;
	}
