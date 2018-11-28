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

struct triple {
	char model;
	int i;
	int j;

	friend bool operator==(const triple& triple1, const triple& triple2) {
		if (triple1.model == triple2.model) {
			return true;
		}
		else {
			return false;
		}
	}
};

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N,M;
		cin >> N >> M;


		vector<triple> arr(N, { '.',0,0 });
		int indexOfXorO = 0;
		for (int i = 0; i < M; i++) {
			char c;
			int a, b;
			cin >> c >> a >> b;
			arr[b-1] = { c,a,b };
			if (c == 'x' || c == 'o') {
				indexOfXorO = b - 1;
			}
		}

		vector<triple> modifications;
		vector<triple> first_row(N);
		for (int i = 0; i < N; i++) {
			if (i == 0) {
				first_row[(i+indexOfXorO)%N] = { 'o', 1, (i + indexOfXorO) % N + 1 };
			}
			else {
				first_row[(i + indexOfXorO) % N] = { '+', 1, (i + indexOfXorO) % N + 1 };
			}
		}

		for (int i = 0; i < N; i++) {
			if (arr[i].model != '.') {
				if (first_row[i].model != arr[i].model) {
					modifications.push_back(first_row[i]);
				}
			}
			else {
				modifications.push_back(first_row[i]);
			}
			
		}

		int offset_below = 1;
		for (int i = 0; i < N; i++) {
			if (first_row[N - 1].model == 'o') {
				if (first_row[i].model == '+') {
					modifications.push_back({ 'x', N-offset_below+1, i + 1 });
					offset_below++;
				}
			}
			else {
				if (first_row[i].model == '+') {
					modifications.push_back({ 'x', offset_below + 1, i + 1 });
					offset_below++;
				}
			}
		}

		for (int i = 1; i < N-1; i++) {
			modifications.push_back({ '+', N, i + 1});
		}

		int value = N == 1 ? 2 : 3 * N - 2;
		printCase(t);
		cout << value << " " << modifications.size() << endl;
		for (int i = 0; i < modifications.size(); i++) {
			cout << modifications[i].model << " " << modifications[i].i << " " << modifications[i].j << endl;
		}
	}
}