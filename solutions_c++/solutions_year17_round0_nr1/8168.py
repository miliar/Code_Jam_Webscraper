#include <iostream>
#include <string>
using namespace std;

char flip(char c){
	if(c=='+') {return '-';}
	else {return '+';}
}

int main(){

	int t;
	cin>>t;
	for(int x=1;x<=t;x++){
		string str; int k;
		cin>>str >> k;

		int tries=0;
		for (int i=0;i<str.length();i++){
			if(str[i]=='-' && (i + (k-1)) <str.length() ){
				for(int f=0;f<k;f++){
					str[i+f]=flip(str[i+f]);
				}
				tries++;
			}

		}
		if(str.find('-') == string::npos){ cout<<"Case #"<<x<<": "<<tries<<endl;}
		else{ cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl; }
		
	}

	return 0;
}