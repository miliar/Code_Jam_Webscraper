#include <bits/stdc++.h>
using namespace std;
string elimz(string &s){


	int l=s.length();
	for(int i=0;i<l-1;i++){
		if(s[i+1]=='0'){
			s[i]--;
			for(int j=i+1;j<l;j++) s[j]='9';
			break;
		}
	}
	while(s.length()>0 && s[0]=='0') s.erase(s.begin());
	return s;
}


string lowtidy(string& s){
	elimz(s);

	int l=s.length();

	for(int i=0;i<l-1;i++){
		if(s[i+1]<s[i]){
			for(int j=i+1;j<s.length();j++) s[j]='9';
			while(i>0 && s[i-1]==s[i]){s[i]='9'; i--;}
			s[i]--;
			break;
		}
	}

	while(s.length()>0 && s[0]=='0') s.erase(s.begin());

	return s;
}




int main(){
	int T;string st;
	cin>>T;
	for(int t=0;t<T;t++){
		cin>>st;
		cout<<"Case #"<<(t+1)<<":"<<" "<<lowtidy(st)<<endl;
	}
}
