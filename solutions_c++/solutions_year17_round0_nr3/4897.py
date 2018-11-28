#include <iostream>
#include <map>
using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	int numStalls, numPeople;
	int cnt = 0;
	while (cin >> numStalls >> numPeople) {
		map<int, int> mapping;
		mapping[numStalls]++;
		int y, z;
		for (int i=0; i<numPeople; ++i) {
			int empty = mapping.rbegin()->first;
			if (--mapping.rbegin()->second == 0) mapping.erase(prev(mapping.end()));
			z = (empty-1)/2;
			y = empty-1-z;
			if (y > 0) mapping[y]++;
			if (z > 0) mapping[z]++;
		}
		cout << "Case #" << ++cnt << ": " << y << " " << z << endl;
	}
	return 0;
}