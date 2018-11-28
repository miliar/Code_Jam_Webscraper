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

char getval(string in , int l) {
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
		string ins;
		cin >> ins;
		ins = ins.substr(ins.find_first_not_of('0'));
		string ops = "";
		for (int i = ins.size()-1 ;i > 0;i--) {
			char r = getval(ins, i);
			ops += r;
			if (r != ins[i]) {
				while (ins[i - 1] == '0') {
					ins[i - 1] = '9';
					ops += '9';
					i--;
				}
				ins[i - 1] -= 1;	
				for (int j = 0; j < ops.size();j++) {
					ops[j] = '9';
				}
			}			
		}
		if (ins[0] != '0') {
			ops += ins[0];
		}
		reverse(ops.begin(), ops.end());
		cout << "Case #" << ++caserunning << ": " << ops << '\n';	

	}


	return 0;
}

