#include <stdio.h>
#include <iostream>
#include <string>
#define FOR(i,n) for(int (i)=0; (i)<(n); (i)++)
#define SD(x) scanf("%d", &x); 
using namespace std;
string str;
bool solve(int idx, int last){
	if(idx == str.size()-1){
		return (str[idx]-'0' >= last);
	}
	if(str[idx]-'0' < last) {
		return false;
	}
	if(solve(idx+1, str[idx]-'0')){
		return true;
	}
	else{
		if(str[idx] == '0'){
			str[idx] == '9';
			str[idx-1]--;
		}
		else str[idx]--;
		for(int i=idx+1; i<str.size(); i++)
			str[i] = '9';
		return str[idx]-'0' >= last;
	}
}
int main(){
	int t; SD(t);
	FOR(j,t){
		cin >> str;
		solve(0, 0);
		printf("Case #%d: ", j+1);
		int i = 0;
		while(str[i] == '0') i++;
		while(i<str.size()) printf("%c", str[i++]);
		printf("\n");
	}
}