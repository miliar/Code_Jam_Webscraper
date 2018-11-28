#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <map>
using namespace std;


void solve () {
	long long size;
	long long persons;
	map <long long, long long> spaces;
	cin >> size;
	cin >> persons;
	spaces[size] = 1;
	long long currentSize;
	long long currentPersons;
	while(persons > 0) {
        auto it = spaces.end();
		it--;
		currentSize = it->first;
		currentPersons = it->second;
		spaces.erase(it);
		persons -= currentPersons;
		if (currentSize%2) {
			spaces[currentSize/2] += 2*currentPersons;
		} else {
			spaces[(currentSize/2)-1] += currentPersons;
			spaces[currentSize/2] += currentPersons;
		}
	}
	
	cout << currentSize/2 << " " << (currentSize-1)/2 << endl;
	
	
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 1; i <= tests; i++) {
    	cout << "case #" << i << ": ";
    	solve();
	}
	return 0; 
}

