#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <stdio.h>
using namespace std;
int tc;
string s, ans;
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("Boutlarge.txt", "w", stdout);
	scanf("%d", &tc);
	for (int i = 0; i < tc; i++){
		cin >> s;
		bool done = true;
		while (done){
			done = false;
			ans = "";
			for (int j = 0; j < s.length() - 1; j++){
				if (s[j] > s[j + 1]){
					if (s[j] == '1'){
						for (int k = 0; k < s.length() - 1; k++){
							ans = ans + '9';
						}
					} else {
						for (int k = 0; k < j; k++){
							ans = ans + s[k];
						}
						ans = ans + (char)((int)s[j] - 1);
						for (int k = j + 1; k < s.length(); k++){
							ans = ans + '9';
						}
					}
					s = ans;
					done = true;
					break;
				}
			}
		}
		printf("Case #%d: ", i + 1);
		cout << s << endl;
	}
}
