//============================================================================
// Name        : cj2017b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

long long n;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out_large.txt", "w", stdout);
	int t;
	cin >> t;
	int num = 0;
	while(t--) {
		cin >> n;
		long long div = 1;
		while(n/div > 0) {
			long long temp = n/div;
			int cur = temp % 10;
			bool decr = false;
			while(temp > 0) {
				if (temp%10 > cur) decr = true;
				temp/= 10;
			}
			if (decr) {
				n-= (cur+1) * div;
				long long temp_div = div/10;
				while(temp_div > 0) {
					if ((n/temp_div) % 10 != 9) {
						n+= (9 - ((n/temp_div) % 10)) * temp_div;
					}
					temp_div/= 10;
				}
			}
			div*= 10;
		}
		cout << "Case #" << ++num << ": " << n << endl;
	}
	return 0;
}
