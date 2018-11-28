#include <bits/stdc++.h>

using namespace std;

void help(string& s,int index){
	int i;
	if(index>=s.length())return;
	for(i=index;i<s.length();i++){
		if(s[i]-'0' == s[index]-'0')continue;
		if(s[i]-'0' > s[index]-'0'){
			i=s.length();
			break;
		}
		else break;
	}
	if(i!=s.length()){
		s[index]=(s[index]-'0'-1)+'0';
		for(i=index+1;i<s.length();i++)s[i]='9';
		return;
	}
	help(s,index+1);
}

int main(){
	long long int n;
	int T;
	int i;
	string s;
	char tmp;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>s;
		for(i=1;i<s.length();i++){
			if(s[i]-'0' >= s[0]-'0')continue;
			else break;
		}
		cout<<"Case #"<<t<<": ";
		help(s,0);
		if(s[0]!='0')cout<<s[0];
		for(i=1;i<s.length();i++)cout<<s[i];
		cout<<endl;
	}
}