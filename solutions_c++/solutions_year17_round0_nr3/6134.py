/*
* File:   main.cpp
* Author: Sreekanth
*
* Created on Apr 7, 2017
*/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

char getval(string in, int l) {
	for (int i = 0;i < l;i++) {
		if (in[i] > in[l]) {
			return '9';
		}
	}
	return in[l];
}

int main()
{
	freopen("I.in", "r", stdin);
	freopen("O.op", "w", stdout);

	int cases;
	cin >> cases;
	int caserunning = 0;
	while (cases--)
	{
		unsigned long long n, k;
		cin >> n >> k;
		map<unsigned long long, unsigned long long> gaps;
		gaps[n] = 1;
		unsigned long long r = 0, l = 0;
		if (k != n) {
			for (int i = 0; i < k;i++) {
				int sp;
				if (gaps.size() == 1) {
					sp = gaps.begin()->first;					
				}
				else {
					sp = gaps.rbegin()->first;
				}
				if (sp % 2) {
					l = r = (sp / 2);
				}
				else {
					l = (sp / 2);
					r = l - 1;
				}
				gaps[sp] -= 1;
				if (gaps[sp] == 0) {
					gaps.erase(sp);
				}
				if (gaps.find(l) == gaps.end()) {
					gaps[l] = 1;
				}
				else {
					gaps[l] += 1;
				}
				if (gaps.find(r) == gaps.end()) {
					gaps[r] = 1;
				}
				else {
					gaps[r] += 1;
				}
			}
		}
		
		cout << "Case #" << ++caserunning << ": " << max(r,l) << " " << min(r,l) << '\n';

	}


	return 0;
}

