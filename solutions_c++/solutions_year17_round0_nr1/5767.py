#include "stdafx.h"
#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cstdint>
#include <queue>
using namespace std;
#define foreach(i, c) for (__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

int K;
int stringLen;
char strarray[10];
int result = 99999999;

bool isHappy() {
	for (int i = 0; i < stringLen; i++) {
		if (strarray[i] == '-') {
			return false;
		}
	}
	return true;
}

void flip(int _i) {
	for (int i = _i; i < _i + K; i++) {
		if (strarray[i] == '-') {
			strarray[i] = '+';
		}
		else {
			strarray[i] = '-';
		}
	}
}

int calc( int _flips )
{
	if (isHappy()) {
		result > _flips ? result = _flips : false;
		return 0;
	}

	if (_flips > 8) {
		return 0;
	}

	for (int i = 0; i < stringLen - K +1; i++) {
		flip(i);
		calc(_flips + 1);
		flip(i);
	}
	return 0;
}

void work()
{
	// Code here
	scanf("%s %d\n", strarray, &K);

	stringLen = strlen(strarray);
	//flip(0);
	//printf("%s %d\n", strarray, stringLen);
	//return;
	calc(0);

	if (result == 99999999) {
		printf("IMPOSSIBLE\n");
	}
	else {
		printf("%d\n", result);
	}


	result = 99999999;
}

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w+", stdout);
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out.txt", "w+", stdout);

	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; cs++)
	{
		printf("Case #%d: ", cs);
		work();
	}

	return 0;
}
