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

int solve(string str, int k) {
	int len = str.size(), res = 0;
	for (int i = 0; i <= len - k; i++) {
		if (str[i] == '-') {
			res++;
			for (int j = i; j < i + k; j++)
				if (str[j] == '-')	str[j] = '+';
				else	str[j] = '-';
		}
	}
	for (int i = 0; i < len; i++)
		if(str[i] == '-')
			return -1;
	return res;
}

int main(void) {
    int t, k;
	string str;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> str >> k;
		int res = solve(str, k);
		if (res != -1)
			cout << "Case #" << i << ": " << res << "\n";
		else
			cout << "Case #" << i << ": IMPOSSIBLE\n";
	}

    return 0;
}