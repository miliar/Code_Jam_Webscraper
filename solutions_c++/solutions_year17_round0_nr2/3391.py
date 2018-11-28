#include <iostream>
#include <cstdio>
#include <string>
typedef unsigned long long int ull;
using namespace std;
int check(string s){	// Até onde ele vai sem dar problema
	int i;
	for(i = 1; i < s.size(); i++)
		if(s[i] < s[i-1]) return i-1;
	return s.size()-1;
}
int main(){
	int t,p;
	ull n;
	string num;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> n;
		num = to_string(n);
		while((p = check(num)) < num.size()-1){
			num[p] = num[p]-1;
			for(int j = p+1; j < num.size(); j++)
				num[j] = '9';
		}
		int j = 0;
		while(num[j] == '0')j++;
		printf("Case #%d: ",i);
		while(j < num.size())
			printf("%c",num[j++]);
		printf("\n");
	}
	return 0;
}

