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


void work()
{
	// Code here
	unsigned long long N;
	unsigned long long K;

	scanf("%llu %llu\n", &N, &K);

	// veo la potencia de dos mas grande que contiene y la diferencia a esta, o sea, si k=2^x + y busco el valor de x e y

	unsigned long long uphalfK = (unsigned long long)(K / 2);
	unsigned long long uphalfN = (unsigned long long)(N / 2);
	if (K % 2 != 0) {
		uphalfK++;
	}
	if (N % 2 != 0) {
		uphalfN++;
	}

	/*if (K > uphalfN+100) {
		printf("0 0\n");
		return;
	}*/

	std::priority_queue< unsigned long long > mypq;
	mypq.push(N);

	//printf("N %llu K %llu -- ", N, K);
	unsigned long long a;
	unsigned long long b;
	while ( K > 1 ) {
		a = (mypq.top() - 1) / 2;
		b = a;
		if (mypq.top() % 2 == 0) {
			a++;
		}
		/*
		if (((mypq.top() - 1) / 2) % 2 != 0) {
			a++;
		}
		*/
		mypq.pop();
		mypq.push(a);
		mypq.push(b);
		K--;
	}

	unsigned long long min = (mypq.top() - 1) / 2;
	unsigned long long max = min;
	if (mypq.top() % 2 == 0) {
		max++;
	}

	printf("%llu %llu\n", max, min);
	
	/*
	int power = 1;
	int done = 0;
	while (done == 0) {
		if ( (unsigned long long)(pow(2, power)) >= uphalfK ) {
			done = 1;
		}
		else {
			power++;
		}
	}
	printf( "%llu y %d\n", uphalfN, power);
	*/
}

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w+", stdout);
	freopen("C-small-2-attempt1.in", "r", stdin);
	freopen("C-small-2-attempt1.out.txt", "w+", stdout);

	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; cs++)
	{
		printf("Case #%d: ", cs);
		work();
	}

	return 0;
}
