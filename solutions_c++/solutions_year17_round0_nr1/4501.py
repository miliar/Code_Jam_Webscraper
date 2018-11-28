#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int caseNum = 1; caseNum <= t; caseNum++) {
		string pancakes;
		int k;
		cin >> pancakes >> k;
		int numFlips = 0;
		for(int i = 0; i <= pancakes.length() - k; i++) {
			if(pancakes[i] == '-') {
				for(int j = i; j < i + k; j++) {
					if(pancakes[j] == '-')
						pancakes[j] = '+';
					else
						pancakes[j] = '-';
				}
				numFlips++;
			}
		}
		bool isPossible = true;
		for(int i = (int) pancakes.length() - k; i < pancakes.length(); i++) {
			if(pancakes[i] == '-') {
				cout << "Case #" << caseNum << ": IMPOSSIBLE" << endl;
				isPossible = false;
				break;
			}
		}
		if(isPossible)
			cout << "Case #" << caseNum << ": " << numFlips << endl;
	}
	return 0;
}
