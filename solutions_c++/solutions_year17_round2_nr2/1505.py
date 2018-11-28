// Round1ProblemA2015.cpp : Defines the entry point for the console application.
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
#include <set>
#include <map>
#include <tuple>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

void printCase(int i) {
	cout << "Case #" << i << ": ";
}

const long long inf = (long long) 2e18;

ll gcd(ll a, ll b) {
	if (b > a) {
		return gcd(b, a);
	}
	if (b == 0) {
		return a;
	}
	return gcd(b, a%b);
}

const ll moduluss = 1000000007;

ll factorial(ll N) {
	if (N == 1 || N == 0) {
		return N;
	}
	else {
		return (ll)(N*factorial(N - 1)) % moduluss;
	}
}


struct color {
	int count;
	char c;
	friend bool operator<(const color& c1, const color& c2) {
		return c1.count < c2.count;
	}
};

int main()
{
	int T;
	cin >> T;


	for (int t = 1; t <= T; t++) {
		printCase(t);

		cout.precision(17);

		int N;
		cin >> N;
		vector<int> colors(6); //R O Y G B V
		for (int i = 0; i < 6; i++) {
			cin >> colors[i];
		}


		//for small index 0,2,4 is R Y B 
		int reds = colors[0];
		int yellows = colors[2];
		int blues = colors[4];

		priority_queue<color> q;
		q.push({ reds, 'R' });
		q.push({ yellows, 'Y' });
		q.push({ blues, 'B' });

		char first = 'X';
		char lastColor = 'X';

		int ratio1 = ceil((double)(N + 1) / 2);

		if (reds >= ratio1 || blues >= ratio1 || yellows >= ratio1) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		while (reds != yellows || blues != yellows) {
			char mx;
			int mxx;

			if (reds >= yellows && reds >= blues && 'R' != lastColor) {
				mx = 'R';
				mxx = reds;
				reds--;
			}
			else if (reds >= yellows && reds >= blues && 'R' == lastColor) {
				if (yellows >= blues) {
					mx = 'Y';
					mxx = yellows;
					yellows--;
				}
				else {
					mx = 'B';
					mxx = blues;
					blues--;
				}
			}
			else if (blues >= reds && blues >= yellows && 'B' != lastColor) {
				mx = 'B';
				mxx = blues;
				blues--;
			}
			else if (blues >= reds && blues >= yellows && 'B' == lastColor) {
				if (reds >= yellows) {
					mx = 'R';
					mxx = reds;
					reds--;
				}
				else {
					mx = 'Y';
					mxx = yellows;
					yellows--;
				}
			}
			else if (yellows >= reds && yellows >= blues && 'Y' != lastColor) {
				mx = 'Y';
				mxx = yellows;
				yellows--;
			}
			else if (yellows >= reds && yellows >= blues && 'Y' == lastColor) {
				if (reds >= blues) {
					mx = 'R';
					mxx = reds;
					reds--;
				}
				else {
					mx = 'B';
					mxx = blues;
					blues--;
				}
			}


			lastColor = mx;
			cout << mx;
			if (first == 'X') {
				first = mx;
			}
		}

		if (first == 'X') {
			lastColor = 'R';
			first = 'R';
		}

		int total = blues;

		if (first == 'R' && lastColor != 'R') {
			//output beginning with R until nothing left
			for (int i = 0; i < total; i++) {
				cout << "RYB";
			}
		}
		else if (first == 'R' && lastColor == 'R') {
			for (int i = 0; i < total; i++) {
				cout << "BRY";
			}
		}
		else if (first == 'Y' && lastColor != 'Y') {
			//start with Y
			for (int i = 0; i < total; i++) {
				cout << "YBR";
			}
		}
		else if (first == 'Y' && lastColor == 'Y') {
			for (int i = 0; i < total; i++) {
				cout << "BYR";
			}
		}
		else if (first == 'B' && lastColor != 'B') {
			//start with Y
			for (int i = 0; i < total; i++) {
				cout << "BYR";
			}
		}
		else if (first == 'B' && lastColor == 'B') {
			for (int i = 0; i < total; i++) {
				cout << "YBR";
			}
		}

		cout << endl;

		/*
		while (!q.empty()) {
			auto top = q.top();
			q.pop();
			if (lastColor == top.c) {
				auto next = q.top();
				q.pop();
				next.count--;
				cout << next.c;
				if (next.count > 0) {
					q.push(next);
				}
				q.push(top);
				lastColor = next.c;
			}
			else {
				top.count--;
				cout << top.c;
				if (top.count > 0) {
					q.push(top);
				}
				lastColor = top.c;
			}
		}*/



	}





	return 0;
}
