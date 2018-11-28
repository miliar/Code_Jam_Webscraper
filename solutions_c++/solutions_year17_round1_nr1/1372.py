#include <cfloat>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef unsigned long long ulint;
typedef long long lint;
typedef long double lubb;

void run(vector<vector<char> >& cake, int R, int C) {

	vector<bool> rowHasChar(R, false);
	for (int i = 0; i < R; i++){
		bool hasChar = false;
		char currChar = '6';
		for (int j = 0; j < C; j++) {
			if (cake[i][j] == '?' && !hasChar) continue;
			if (cake[i][j] != '?' && !hasChar) {
				hasChar = true;
				currChar = cake[i][j];
				for(int z = j-1; z>= 0; z--) {
					cake[i][z] = currChar;
				}
				continue;
			}
			if (cake[i][j] == '?' && hasChar) { 
				cake[i][j] = currChar;
				continue;
			}
			//cake[i][j] != '?' && hasChar
			currChar = cake[i][j];
		}
		rowHasChar[i] = hasChar;
	}

	int lastRowWithChar = -1;
	for (int i = 0; i < R; i++) {
		if (!rowHasChar[i] && lastRowWithChar == -1) continue;
		if (rowHasChar[i] && lastRowWithChar == -1) {
			lastRowWithChar = i;
			for (int r = i-1; r >= 0; r--) {
				for (int c = 0; c < C; c++) {
					cake[r][c] = cake[lastRowWithChar][c];
				}
			}
			continue;
		}
		if (rowHasChar[i]) { //lastRowWithChar > -1
			lastRowWithChar = i;
			continue;
		}
		//if (!rowHasChar[i]) { //lastRowWithChar > -1
		for (int c = 0; c < C; c++) {
			cake[i][c] = cake[lastRowWithChar][c];
		}
	}
			


}


void test() {
	int C, F;	
	char next = '?';
	cin >> C >> F;
	vector<vector<char> > cake(C, vector<char>(F, '?'));
	for (int i = 0; i < C; ++i) {
		for (int j = 0; j < F; ++j) {
			cin >> next;
			if (next == '?') continue;
			cake[i][j] = next;
		}
	}
			
	run(cake, C, F);
	cout << endl;	
	for (int i = 0; i < C; ++i) {
		for (int j = 0; j < F; ++j) {
			cout << cake[i][j];
		}
		cout << endl;
	}
}	

int main() {
	unsigned long T;
	cin >> T;
	for(unsigned long i = 1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		test();	
		//cout << endl;
	}
	return 0;
}
