#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <unordered_map>
#include <string>
#include <utility>
#include <unordered_set>
using namespace std;


void flip(string & str, int startIndex, int size) {
	
	for (int i=startIndex; i < startIndex+size; i++) {
		if (str[i] == '+')
			str[i] = '-';
		else
			str[i] = '+';
	}
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i < t; i++) {
		string s;
		int flipSize;
		int flips = 0;
		cin >> s >> flipSize;
		int totalPancakes = s.length();
		for (int index=0; index <= totalPancakes-flipSize; index++) {
			if (s[index] == '-') {
				flip(s,index,flipSize);
				flips++;
			}
		}
		for (int j=totalPancakes-flipSize+1; j < totalPancakes; j++ ) {
			if (s[j] == '-')
				flips=-1;
		}
		//cout << "str: " << s << endl;
		if (flips == -1)
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i+1 << ": " << flips << endl;
	}
	return 0;
}