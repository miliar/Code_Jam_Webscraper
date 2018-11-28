//#include "stdafx.h"

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int ll;

string ConvToString(ll n) {
	string res = "";
	while (n) {
		int d = n % 10;
		res.push_back(d + '0');
		n /= 10;
	}
	if(res == "")	res = "0";
	else	std::reverse(res.begin(), res.end());
	return res;
}

string ClearLeadingZeros(string str) {
	int sz = str.size(), ind;
	for(ind = 0; ind < sz; ind++)
		if (str[ind] != '0')
			break;
	string res = "";
	for(; ind < sz; ind++)
		res.push_back(str[ind]);
	if(res == "")	res = "0";
	return res;
}

bool Verify(string str) {
	int sz = str.size();
	for (int i = 0; i < sz - 1; i++)
		if (str[i] > str[i + 1])
			return false;
	return true;
}

string solve(string str) {
	int sz = str.size();
	for (int i = 0; i < sz - 1; i++) {
		if (str[i] > str[i + 1]) {
			str[i] = str[i] - 1;
			for (int j = i + 1; j < sz; j++)
				str[j] = '9';
			break;
		}
	}
	str = ClearLeadingZeros(str);
	if (Verify(str) == false)
		str = solve(str);
	return str;
}

int main(void) {
    ll t, n;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n;
		cout << "Case #" << i << ": " << solve(ConvToString(n)) << "\n";
	}

    return 0;
}