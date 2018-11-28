#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int T; // number of tests
	scanf("%d", &T);
	string temp;
	getline(cin, temp);

	for (int i = 0; i < T; i++) {
		string line;
		getline(cin, line);

		istringstream ss(line);
		string pan;
		int K;
		ss >> pan >> K;

		int count = 0;
		for (int j = 0; j <= pan.length()-K; j++) {
			if (pan[j] == '-') {
				for (int k = j; k < j+K; k++) {
					if (pan[k] == '-') {
						pan[k] = '+';
					} else {
						pan[k] = '-';
					}
				}
				count++;
			}
		}

		bool possible = true;
		for (int j = pan.length()-K; j < pan.length(); j++) {
			if (pan[j] == '-') {
				cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
				possible = false;
				break;
			}
		}

		if (possible) {
			cout << "Case #" << i+1 << ": " << count << endl;
		}
	}
}