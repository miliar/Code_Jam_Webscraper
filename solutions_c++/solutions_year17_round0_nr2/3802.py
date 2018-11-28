#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
using namespace std;
int main(){
	int t = 0;
	cin>>t;
	for(int c = 1; c <= t; c++){
		string s = "";
		cin>>s;
		for(int i = s.size()-2; i >= 0; i--){
			if(s[i] > s[i+1]){
				for(int j = 0; i+j+1 < s.size(); j++)
					s[i+j+1] = '9';
				s[i]--;
			}
		}
		if(s.rfind('0') != string::npos)
			s = s.substr(s.rfind('0')+1);
		cout<<"Case #"<<c<<": "<<s<<endl;
	}
	return 0;
}