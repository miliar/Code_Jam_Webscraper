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

string findLastTidyNumber(string N) {
	string result = N.substr(0,1);
	int lastDigit = N[0] - '0';
	int broken = false;
	for (int i = 1; i < N.length(); i++) {
		if ((N[i] - '0') < lastDigit) {
			broken = true;
			break;
		}
		else {
			result += N[i];
		}
		lastDigit = N[i] - '0';
	}
	if (!broken) {
		return N;
	}

	while (result != "" && result[result.length()-1] - '0' == lastDigit) {
		result = result.substr(0, result.length() - 1);
	}

	int remainingChars = N.length() - result.length()-1;
	if (lastDigit > 1) {
		result += lastDigit-1 + '0';
	}
	while (remainingChars > 0) {
		result += '9';
		remainingChars--;
	}

	return result;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		string N;
		cin >> N;

		printCase(i);
		cout << findLastTidyNumber(N) << endl;
	}
}