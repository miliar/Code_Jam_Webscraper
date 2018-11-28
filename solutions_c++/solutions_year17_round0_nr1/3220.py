// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#define _CRTDBG_MAP_ALLOC  
#include <stdlib.h>  
#include <crtdbg.h>  
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <list>
#include <unordered_map>
#include <stack>
#include <functional>
#include <queue>
using namespace std;

void printCase(int i) {
	cout << "Case #" << i << ": ";
}

int findMin(string s, int k) {
	int i;
	int flips = 0;
	for (i = 0; i <= s.length() - k; i++) {
		if (s[i] == '-') {
			//flip it:
			flips++;
			for (int j = 0; j < k; j++) {
				s[i + j] = (s[i + j] == '-') ? '+' : '-';
			}
		}
	}
	for (int j = i; j < s.length(); j++) {
		if (s[j] == '-') {
			return -1;
		}
	}
	return flips;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		string s;
		int k;
		cin >> s >> k;

		int mini = findMin(s, k);
		if (mini >= 0) {
			printCase(i);
			cout << mini << endl;
		}
		else {
			printCase(i);
			cout << "IMPOSSIBLE" << endl;
		}
	}
}