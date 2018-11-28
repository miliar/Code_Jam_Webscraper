#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<fstream>

using namespace std;

int all(string s){
	int len = s.length();
	if((s.find("-")<len) && (s.find("+")<len))return -1;
	if((s.find("-")<len) && (s.find("+")>=len))return 1;
	return 0;
}

string delFirst(string s){
	int i=0;
	while((i<s.length()) && (s[i]=='+')){
		s = s.erase(0,1);
	}
	return s;
}

string flip(string s, int k){
	for(int i=0; i<k;i++){
		if(s[i]=='-')s[i]='+';
		else s[i]='-';
	}
	return s;
}

int main(){
	int T, k;
	string s;
	ifstream ccin("A-large.in");
	ofstream ccout("large_output.txt");
	ccin>>T;
	
	for(int i=1; i<=T; i++){
		ccin>>s;
		ccin>>k;
		int count = 0;
		int len = s.length();
		while(len != k){
			if(all(s)!=0)count++;
			else break;
			
			if(s[0]=='+') s = delFirst(s);
			if(s.length()<k)break;
			s=flip(s,k);
			len = s.length();
			
		}
		int res = all(s);
		if((res==-1) || (s.length()<k))ccout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		else ccout<<"Case #"<<i<<": "<<res+count<<endl;
	}
	ccout.close();
	ccin.close();
}
