#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

bool shouldFlip(char c, int flips) {
	if (c=='-' && flips%2==0) {
		return true;
	}
	if (c=='+' && flips%2==1) {
		return true;
	}
	
	return false;
}

int main(int argc, char **argv)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T=0;
	string s;
	string res;
	
	cin >> T;
	
	for (int t=1;t<=T;t++) {
		cin >> s;
		res.clear();
		
		res.push_back(s[0]);
		
		for (int i=1;i<s.length();i++) {
			if (s[i]>=res[i-1]) {
				res.push_back(s[i]);
			} else {
				for (int j=i;j<s.length();j++) {
					res.push_back('9');
				}
				for (int j=i-1;j>=0;j--) {
					res[j]--;
					
					if (j>0 && res[j]<res[j-1]) {
						res[j]='9';
					} else {
						break;
					}
				}
				break;
			}
		}
		
		printf("Case #%d: ", t);
		
		int x;
		for (x = 0; x < res.size() && res[x]=='0'; x++);
		
		for (int i=x;i<res.size();i++) {
			printf("%c", res[i]);
		}
		printf("\n");
	}
}