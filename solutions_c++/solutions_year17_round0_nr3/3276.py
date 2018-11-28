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
#include <math.h>
using namespace std;

void printCase(int i) {
	cout << "Case #" << i << ": ";
}

int findIndex(long long K) {
	int index = 0;
	while (K != 0) {
		K /= 2;
		index++;
	}
	return index - 1;
}

pair<long long, long long> findPair(long long N, long long offset, int index) {
	pair<long long, long long> p1 = { N,1 };
	pair<long long, long long> p2 = { N,1 };
	pair<long long, long long> start_val;
	if (N % 2 != 0) {
		start_val.first = N / 2;
		start_val.second = N / 2;
	}
	else {
		start_val.first = N / 2;
		start_val.second = N / 2 - 1;
	}
	if (index == 0) {
		return start_val;
	}

	//Now we can assume index is at least 1:
	p1.first = start_val.first;
	p1.second = 1;
	p2.first = start_val.second;
	p2.second = 1;

	int temp_index = 1;
	while (temp_index < index) {
		//update pairs:
		if (p1.first % 2 != 0 && p2.first % 2 != 0) {
			//they must be equal. One can store half and the other can store half:
			int next = p1.first / 2;
			p1.first = next;
			p2.first = next;
			p1.second = 2 * p1.second;
			p2.second = 2 * p2.second;
		}
		else {
			int temp = p1.first;
			int temp2 = p2.first;
			//p1 should store the larger integer:
			if (p1.first % 2 == 0) {
				p1.first = p1.first / 2;
				p2.first = p1.first - 1;
			}
			else {
				p1.first = p2.first / 2;
				p2.first = p1.first - 1;
			}

			if (temp2 % 2 == 0 && temp % 2 == 0) {
				p1.second = p1.second + p2.second;
				p2.second = p1.second;
			}
			else if (temp % 2 != 0) {
				p1.second = 2 * p1.second + p2.second;
			}
			else {
				p2.second = 2 * p2.second + p1.second;
			}

		}
		temp_index++;
	}

	//now we have the pairs where we want them. 
	if (p1.second >= offset) {
		//p1 can handle it:
		if (p1.first % 2 != 0) {
			start_val.first = p1.first / 2;
			start_val.second = p1.first / 2;
		}
		else {
			start_val.first = p1.first / 2;
			start_val.second = p1.first / 2 - 1;
		}
	}
	else {
		//p2 will have to handle it:
		if (p2.first % 2 != 0) {
			start_val.first = p2.first / 2;
			start_val.second = p2.first / 2;
		}
		else {
			start_val.first = p2.first / 2;
			start_val.second = (p2.first > 0) ? p2.first / 2 - 1 : p2.first;
		}
	}
	return start_val;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		long long N,K;
		cin >> N >> K;

		int index = findIndex(K);
		
		long long offset = K - pow(2, index) + 1;

		pair<long long, long long> p = findPair(N, offset, index);
		printCase(i);
		cout << p.first << " " << p.second << endl;
		
	}
}