#include <iostream>
#include <stdio.h>
using namespace std;
int main() {
	int numTests;
	cin >> numTests;
	for (int test = 0; test < numTests; test++) {
		string cakes;
		int k;
		int r = 0;
		cin >> cakes >> k;
		for (int cake = 0; cake < cakes.length(); cake++) {
			if (cakes[cake] == '-') {
				if (cake + k > cakes.length()) {
					r = -1;
					break;
				}
				r++;
				for (int i = cake; i < cake + k; i++) {
					cakes[i] = cakes[i] == '+'? '-' : '+';  
				}
			}
		}
		if (r == -1) 
			cout << "Case #" << (test + 1) <<  ": IMPOSSIBLE\n";
		else cout<< "Case #" << (test + 1) <<  ": " <<  r << "\n";
	}
}
