#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int main(){
	int ca;
	cin >> ca;
	for(int c = 1; c <= ca; c++){
		string str;
		int k;
		cin >> str >> k;
		int len = str.length();
		int cnt = 0;
		bool imp = false;
		for(int i = 0; i < len; i++){
			if(i + k <= len){
				if(str[i] == '-'){
					for(int j = i; j < i + k; j ++)
						str[j] = '+' + '-' - str[j];
					cnt++;
				}
			}
			else if(str[i] == '-')
				imp = true;
		}
		// cout << str << endl;
		printf("Case #%d: ", c);
		if(imp)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << cnt << endl;
	}
	return 0;
}