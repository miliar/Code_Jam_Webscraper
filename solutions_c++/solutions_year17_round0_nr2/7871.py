#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
using namespace std;

void solve(int test) {
	char s[20];
	
	cin >> s;
	int j=0;
	int k = strlen(s);
	if(k==1){
		printf("Case #%d: %s\n", test, s);
	}
	
	else
		{
		
	
		for(int i =0; i<k-1; i++)		
			{
			if (s[i]> s[i+1]){
				while(s[i]==s[i-1]){
					i--;
				}
				s[i] = s[i]-1;
				while(i<k-1){
					s[i+1]='9';
					i++;
				}
				
				break;
			}
			
		}
		
		while(s[j]=='0')j++;
		printf("Case #%d: %s\n", test, s+j);
	}
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int testNumber;
	cin >> testNumber;
	for (int test = 1; test <= testNumber; ++test) {
		solve(test);
	}
}
