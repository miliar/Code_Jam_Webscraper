#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <string.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		long long n, cn, answer = 0;
		int counter = 0, step = 0, len = 0;
		int p[19] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
		cin >> n;
		cn = n;
		while (cn > 0) {
			p[counter] = cn % 10;
			cn /= 10;
			counter++;
		}
		counter--;
		while (step < counter) {
			if (p[step] < p[step + 1] && p[step + 1] >= 0) {
				p[step + 1]--;
				while (step >= 0) {
					p[step] = 9;
					step--;
				}
				step = 0;
			}
			else {
				step++;
			}
		}
		for (int j = 17; j >= 0; j--) {
			answer *= 10;
			answer += p[j];
		}
		cout << "Case #" << i << ": " << answer << endl;
	}
}