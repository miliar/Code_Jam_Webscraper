#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
int main() {
	int numTests;
	cin >> numTests;
	for (int test = 0; test < numTests; test++) {
		int C;
		int R;
		cin >> R >> C;
		vector<string> cake(R);
		for (int i = 0; i < R; i++) {
			cin >> cake[i];
		}
		vector<char> first(C,'?');
		for (int j = 0; j < C; j++) {
			for (int i = 0; i < R; i++) {
				if (cake[i][j] != '?') {
					first[j] = cake[i][j];
					break;
				}
			}
		}
		int start;
		for (int j = 0; j < C; j++) {
			if (first[j] != '?') {
				start = j;
				break;
			}
		}
		for (int j = start; j < C; j++) {
			if (first[j] == '?') {
				for (int i = 0; i < R; i++) cake[i][j] = cake[i][j - 1];
			} 
			else {
				char cur = first[j];
				for (int i = 0; i < R; i++) {
					if (cake[i][j] != '?') {
						cur = cake[i][j];
					} else {
						cake[i][j] = cur;
					}
				}
			}
		}
		for (int j = start - 1; j >= 0; j--) {
			for (int i = 0; i < R; i++) {
				cake[i][j] = cake[i][start];
			}
		}
		cout<< "Case #" << (test + 1) <<  ": " << endl;
		for (int i = 0; i < R; i++) 
			cout << cake[i] << endl;
	}
}
