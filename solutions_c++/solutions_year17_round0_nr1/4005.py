#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int check(string s){
	int flag = 1;
	for(int x=0;x<s.length();x++){
		if(s[x]!='+'){
			flag = 0;
			break;
		}
	}
	return flag;
}

int main(){
	int t;	cin >> t;
	for(int i=0;i<t;i++){
		string s;	cin >> s;
		int k;		cin >> k;
		int count = 0;
		for(int x=0;x<s.length();x++){
			if(s[x]=='-'){
				if(x+k>s.length()){
					break;
				}
				for(int y=x;y<x+k;y++){
					if(s[y]=='+')	s[y]='-';
					else			s[y]='+';
				}
				count++;
			}
		}
		if(check(s)==1){
			printf("Case #%d: %d\n",i+1,count);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}
	}
	return 0;
}