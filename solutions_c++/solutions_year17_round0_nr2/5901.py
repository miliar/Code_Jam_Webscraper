#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++) {
		string str;
		cin >> str;
		str = "0"+str;
		for(int i = 1; i<(int)str.size(); i++) {
			if(str[i] < str[i-1])
				for(int j = i; j >= 1; j--) 
					if(str[j] > str[j-1]) {
						str[j]--;
						for(int k = j+1; k<(int)str.size(); k++) {
							str[k] ='9';
						}
						goto fim;
					}
		}
		fim:
		printf("Case #%d: ", test);
		int flag = true;
		for(int i = 0; i<(int)str.size(); i++) {
			if(str[i] == '0' && flag) continue;
			if(str[i] != '0') flag = false;
			printf("%c", str[i]); 
		}
		printf("\n");
	}
	return 0;
}

