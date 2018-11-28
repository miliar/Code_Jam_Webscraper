#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

void sub(string &s,int r){
	int n=s.length();
	int temp=1;
	while(temp&&r>=0){
		//cout<<r<<" "<<temp<<endl;
		if(s[r]=='0'){
			s[r]='9';
			temp=1;
			r--;
		}
		else{
			s[r]--;
			if(r==0&&s[r]=='0') s.erase(0,1);
			temp=0;
		}
	}
	//if(temp==1) cout<<"error!"<<endl;
}

string tidy(string &s,int tail){
	if(tail==0) return s;
	for(int i=0;i<tail;i++){
		if(s[i]>s[i+1]){
			s[tail]='9';
			sub(s,tail-1);
			return tidy(s,tail-1);
		}
	}
	return s;
}

int main(){
	int n;
	cin>>n;
	vector<string> str;
	vector<int> k;
	for(int i=0;i<n;i++){
		string s;
		cin>>s;
		str.push_back(s);
	}
	for(int i=0;i<n;i++){
		string res=tidy(str[i],str[i].length()-1);
		cout<<"Case #"<<i+1<<": ";
		cout<<res<<endl;
	}
}