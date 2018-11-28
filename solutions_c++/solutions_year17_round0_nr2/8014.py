#include <stdio.h>
#include <sstream>
#include <string>
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

void troca(int j,string& s){
	for(int i = j;i<s.size();++i){
		s[i] = '9';
	}
	s[j-1] = s[j-1] -1;
}
void verifica(int j,string& s){
	for(int i = j;i>0;--i){
		if(s[i] < s[i-1]){
			s[i-1] = s[i-1]-1;
			s[i] = '9';
			verifica(i-1,s);
		}else{
			return;
		}
	}

}

int main(){
	int d = 0;
	int count=1;
	string s;
	scanf("%d",&d);
	string vs[d];
	getline(std::cin,s);
	for(int i = 0;i<d;i++){

		getline(std::cin,vs[i]);
	}
	for(string& s : vs){
		for(int j = 1;j<s.size();++j){
			if(s[j]<s[j-1]){
				troca(j,s);
				verifica(j-1,s);
			}else{
				continue;
			}
		}
		if(s[0]=='0')s = s.substr(1,s.size());
		printf("Case #%d: %s\n",count++,s.c_str());
	}


return 0;
}
