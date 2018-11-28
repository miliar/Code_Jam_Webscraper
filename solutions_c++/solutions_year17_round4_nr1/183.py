#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
int main() {
	int numTests;
	cin >> numTests;
	for (int test = 0; test < numTests; test++) {
		
		int N, P;
		cin  >> N >> P;
		int c[4];
		c[0] = 0;c[1]=0;c[2]=0;c[3]=0;
		int result = 0;
		for (int i = 0; i < N; i++) {
			int tmp;
			cin >> tmp;
			c[tmp%P]++;
		}
		result += c[0];
		if (P == 2) {
			result += (1+c[1]) / 2;
		} else if (P == 3) {
			result += min(c[1], c[2]);
			result += (abs(c[1] - c[2]) + 2) /3;
		} else {
			result += c[2]/2;
			result += min(c[1], c[3]);
			if (c[2] % 2) {
				int rm = (abs(c[1] - c[3]) % 4);
				if (rm == 0 || rm == 3) 
					result += 1;
			} 
				result += (abs(c[1] - c[3]) + 3) /4;
			

		}
		cout<< "Case #" << (test + 1) <<  ": " << result <<  endl;
		//for (int i = 0; i < R; i++) 
		//	cout << cake[i] << endl;
	}
}
