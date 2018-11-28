#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	int t,g;
	scanf("%d", &t);
	g = t;
	while(t--){
		string s;
		int k;
		cin>>s>>k;
		int cnt = 0,i = 0;
		while(i<s.length() && k <= (s.length()-i) ){
			if(s[i] == '+')
				i++;
			else{
				for(int j=i;j<i+k;j++){
					s[j] = (s[j] == '+')?'-':'+';
				}
				cnt++;
				i++;
			}
		}
		while(i<s.length()){
			if(s[i] == '-'){
				printf("Case #%d: IMPOSSIBLE\n", g-t);
				break;
			}
			i++;
		}
		if(i == s.length())
			printf("Case #%d: %d\n", g-t, cnt);
	}
}