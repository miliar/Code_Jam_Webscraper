#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <map>
#include<vector>
#include <queue>
#include <functional> 
#include <climits>

using namespace std;
#define MAX_SIZE	100
#define LL long long
#define U unsigned

LL t;
char arr[MAX_SIZE];
char arr2[MAX_SIZE];

long long ii()
{
	long long a;
	scanf("%lld", &a);
	return a;
}

long long uii()
{
	U LL a;
	scanf("%llu", &a);
	return a;
}


char * si(char * arr)
{
	scanf("%s", arr);
	return arr;
}

long long min(long long a, long long b)
{
	if (a < b)
		return a;
	else
		return b;
}

U LL umin(U LL a, U LL b)
{
	if (a < b)
		return a;
	else
		return b;
}

long long diff(long long a, long long b)
{
	if (a < b)
		return b - a;
	else
		return a - b;
}

U LL udiff(U LL a, U LL b)
{
	if (a < b)
		return b - a;
	else
		return a - b;
}

LL horse[1000][2] = {0};

void answer(long long t)
{
	LL d, n, i, h, s;
	d = ii();
	n = ii();
	double maxtime = -1;
	double speed;

	//memset(horse, 0, sizeof(LL) * 1000 * 2);

	for (i = 0; i < n; i++)
	{
		h = ii();
		s = ii();

		if (d!=h && (maxtime == -1 || maxtime < (double)(d-h) / (double)s)){
			maxtime = (double)(d-h) / (double)s;
		}
	}

	speed = (double)d / maxtime;

	printf("Case #%lld: %lf\n", t, speed);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

	t = ii();

	for (long long i = 1; i <= t; i++) {

		answer(i);
		//printf("Case #%lld: %s\n", i, ans);

	}
	return 0;
}