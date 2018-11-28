#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

int main() {
	 int t;
	 unsigned long long n;
	 int tab[20] = {0};
	 
	 cin >> t;
	 for (int test = 1; test <= t; ++test) {
		cin >> n;
		 
		int len = 0;
		while (n != 0) {
			tab[len] = n%10;
			n /= 10;
			++len;
		}
		 
		int ninesFrom = -1;
		 
		for (int i = 1; i < len; ++i) {
			int prev = i-1;
			if (ninesFrom >= 0 && tab[i] >= tab[prev]) {
				ninesFrom = prev;
			}
			else if (tab[i] > tab[prev]) {
				ninesFrom = prev;
			}
		}
		
		if (ninesFrom >= 0) {
			--tab[ninesFrom + 1];
		}
		 
		cout << "Case #" << test << ": ";
		int first = tab[len-1];
		if (first > 0) {
			cout << first;
		}
		
		for (int i = len-2; i > ninesFrom; --i) {
			cout << tab[i];
		}
		
		for (int i = ninesFrom; i >= 0; --i) {
			cout << 9;
		}
		cout << endl;
			
	 }
}
