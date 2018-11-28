#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <map>
#include<vector>
#include <queue>
#include <functional> 

using namespace std;
#define MAX_SIZE	100
#define LL long long
#define U unsigned

LL t;

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

void fillc(char * arr, char ch, LL count, LL i, LL max)
{
	while (arr[i] != '\0')
		i++;

	LL s1, s2;
	if (max > i) {
		s1 = 1;
		s2 = 2;
	}
	else
	{
		s1 = -1;
		s2 = -2;
	}

	for (LL j = i; (i < max ? j <= max : j >= max) && count; ) {
		if (arr[j] == '\0') {
			arr[j] = ch;
			j += s2;
			--count;
		}
		else
			j += s1;
	}
}

bool sortbysec(const pair<char, int> &a,
	const pair<char, int> &b)
{
	return (a.second > b.second);
}

void fillch(LL i, char ch, char * arr)
{
	arr[i] = ch;
}

void answer(long long t)
{
	LL N, R, O, Y, G, B, V;

	vector<pair<char, int>> sortc[1];

	N = ii();
	R = ii();
	sortc[0].push_back(make_pair('R', R));
	O = ii();
	sortc[0].push_back(make_pair('O', O));
	Y = ii();
	sortc[0].push_back(make_pair('Y', Y));
	G = ii();
	sortc[0].push_back(make_pair('G', G));
	B = ii();
	sortc[0].push_back(make_pair('B', B));
	V = ii();
	sortc[0].push_back(make_pair('V', V));

	char arr[1011] = { '\0' };
	
	sort(sortc[0].begin(), sortc[0].end(), sortbysec);

	// small
	if (R > N / 2 || Y > N / 2 || B > N / 2)
	{
		printf("Case #%lld: IMPOSSIBLE\n", t);
		return;
	}

	/*for (LL i = 0; i < N;) {

		for (LL j = 0; j < sortc[0].size(); j++) {
			if (sortc[0][j].second > 0) {
				fillch(i, sortc[0][j].first, arr);
				sortc[0][j].second--;
				i++;
			}
		}
	}*/
	
	bool flip = false;
	while (!sortc[0].empty()) {
		if (sortc[0].begin()->second > 0) {
			fillc(arr, sortc[0].begin()->first, sortc[0].begin()->second, flip ? N-1 : 0, flip ? 0 : N-1);
			flip = flip ? false : true;
		}
		sortc[0].erase(sortc[0].begin());
	}
	
	printf("Case #%lld: %s\n", t, arr);
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);

	t = ii();

	for (long long i = 1; i <= t; i++) {

		answer(i);
		//printf("Case #%lld: %s\n", i, ans);

	}
	return 0;
}