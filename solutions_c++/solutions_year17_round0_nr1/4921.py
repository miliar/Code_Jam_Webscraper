#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int solve(string s, int g){
	int i;
	int count=0;
	for(i=0; i<s.length()-g+1; i++){
		if(s[i]=='-'){
			for(int j=i; j<i+g; j++){
				if (s[j]=='-') s[j]='+';
				else s[j]='-';
			}
			count++;
		}
	}
	bool result = true;
	for(;i<s.length();i++){
		if(s[i]=='-') {
			result=false;
			break;
		}
	}
	if(result){
		return count;
	} else {
		return -1;
	}
}

int main(){
	int n,g;
	string s;
	cin >> n;
	for(int i = 1; i <= n; i++){
		cin >> s >> g;
		printf("Case #%d: ", i);
		int res = solve(s,g);
		if(res==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);

	}
	return 0;
}