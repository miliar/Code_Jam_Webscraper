#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
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
		int r, c;
		string cake[25];
		string newCake[25];
		cin >> r >> c;
		for(int i = 0; i < r; i++) {
			cin >> cake[i];
			newCake[i] = cake[i];
		}
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				char cell = cake[i][j];
				if(cell == '?')
					continue;
				int leftBound = j, rightBound = j;
				for(int k = j-1; k >= 0 && newCake[i][k] == '?'; k--) {
					leftBound = k;
					newCake[i][k] = cell;
				}
				for(int k = j+1; k < c && newCake[i][k] == '?'; k++) {
					rightBound = k;
					newCake[i][k] = cell;
				}
				for(int k = i-1; k >= 0; k--) {
					bool canExpandUpwards = true;
					for(int x = leftBound; x <= rightBound; x++) {
						if(newCake[k][x] != '?')
							canExpandUpwards = false;
					}
					if(!canExpandUpwards)
						break;
					for(int x = leftBound; x <= rightBound; x++) {
						newCake[k][x] = cell;
					}
				}
				for(int k = i+1; k < r; k++) {
					bool canExpandDownwards = true;
					for(int x = leftBound; x <= rightBound; x++) {
						if(newCake[k][x] != '?')
							canExpandDownwards = false;
					}
					if(!canExpandDownwards)
						break;
					for(int x = leftBound; x <= rightBound; x++) {
						newCake[k][x] = cell;
					}
				}
			}
		}
		cout << "Case #" << caseNum << ": " << endl;
		for(int i = 0; i < r; i++)
			cout << newCake[i] << endl;
	}
	return 0;
}
