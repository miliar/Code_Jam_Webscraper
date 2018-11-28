#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main() {
	freopen("intput.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++) {
		string str;
		int n;
		cin >> str >> n;
		int ans = 0;
		for(int i = 0; i<(int)str.size()-n+1; i++) {
			if(str[i] == '-') {
				for(int j = 0; j<n; j++) {
					str[i+j] = str[i+j]=='+'?'-':'+';
				}
				ans++;
			}
		}
		//cout << str << endl;
		int hasAns = true;
		for(int i = 0; i<(int)str.size(); i++) {
			if(str[i] == '-') hasAns = false;
		}
		printf("Case #%d: ", test);
		if(hasAns)
			printf("%d", ans);
		else 
			printf("IMPOSSIBLE");
		printf("\n");
	}
	
	return 0;
}
