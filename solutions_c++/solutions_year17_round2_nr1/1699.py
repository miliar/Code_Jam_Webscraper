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


int main()
{
	int T;
	cin >> T;


	for (int t = 1; t <= T; t++) {
		printCase(t);

		cout.precision(17);

		int D, N;
		cin >> D >> N;

		double max_time = (double) 0;

		for (int i = 0; i < N; i++) {
			int K, S;
			cin >> K >> S;

			double finish_time = (double) (D - K) / S;
			if (finish_time > max_time) {
				max_time = finish_time;
			}
		}

		double ratio = D / max_time;

		cout << ratio << endl;

	}





	return 0;
}
