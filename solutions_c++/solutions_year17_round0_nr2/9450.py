#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<cstdio>
#include<queue>
#include<vector>
#include<string.h>
#include<math.h>
#include<stack>
#include<queue>
#include<deque>
#include<list>
using namespace std;



int count(long long in) {

	long long tmp = in % 10;
	in /= 10;
	while (in >= 10) {

		if ((in % 10) <= tmp)
		{
			tmp = in % 10;
			in /= 10;
		}
		else
			return 0;
	}
	if (tmp < in)
		return 0;

	return 1;

}


int main() {
	
	FILE *inf;
	inf = fopen("output.txt", "w");
	
	int t;
	long long n;
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		scanf("%lld", &n);
		for (long long i = n; i >= 1; i--)
		{
			if (count(i) == 1)
			{
				fprintf(inf, "Case #%d: %lld\n", test, i);
				break;
			}

		}
	}



	fclose(inf);

}




