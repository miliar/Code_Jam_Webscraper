#include <iostream>
#include <limits.h>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;

int main() {
	long t;
	cin >> t;
	cin.ignore();
	int x = t;
	string s;
	while(t--) {
		getline(cin, s);
		for(long i = 0; i < s.length()-1; i++) {
			if(s[i] > s[i+1]) {
				while(i > 0 && s[i-1] == s[i]) i--;
				s[i]--;
				for(long j = i+1; j < s.length(); j++) {
					s[j] = '9';
					}
				}
			}
			cout << "Case #" << x-t << ": ";
			for(int i = 0; i < s.length(); i++)
			{
				if(s[i] != '0') cout << s[i];
			}
			cout << '\n';
		}
	
  return 0;
}
