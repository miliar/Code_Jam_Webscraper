// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

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
using namespace std;
#define foreach(i, c) for (__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

unsigned long long ten_pow(int n)
{
	unsigned long long r = 1;
	while (n--)
		r *= 10;

	return r;
}

int numDigits(unsigned long long x)
{

	return (x < 10 ? 1 :
		(x < 100 ? 2 :
			(x < 1000 ? 3 :
				(x < 10000 ? 4 :
					(x < 100000 ? 5 :
						(x < 1000000 ? 6 :
							(x < 10000000 ? 7 :
								(x < 100000000 ? 8 :
									(x < 1000000000 ? 9 :
										(x < 10000000000ULL ? 10 :
											(x < 100000000000ULL ? 11 :
												(x < 1000000000000ULL ? 12 :
													(x < 10000000000000ULL ? 13 :
														(x < 100000000000000ULL ? 14 :
															(x < 1000000000000000ULL ? 15 :
																(x < 10000000000000000ULL ? 16 :
																	(x < 100000000000000000ULL ? 17 :
																		(x < 1000000000000000000ULL ? 18 :
																			(x < 10000000000000000000ULL ? 19 :
																				20)))))))))))))))))));
}

int isTidy(char _N[20]) {

	unsigned long long NN = std::stoull(_N);

	int numDig = numDigits(NN);

	int min = -1;
	for (int i = 0; i < numDig; i++) {
		if ((int)(_N[i] - '0') >= min) {
			min = (int)(_N[i] - '0');
			continue;
		}
		else {
			// resto algo malo
			// NN -= ten_pow(numDig - i - 1);
			// resto el substring
			char part[20];
			//memcpy(part, _N + i, numDig);
			int count = 0;
			for (int j = 0; j < 20; j++) {
				part[j] = '\0';
			}
			
			for (int j = i; j < numDig; j++) {
				part[count] = _N[j];
				count++;
			}

			unsigned long long partN = std::stoull(part);


			//NN -= 1;
			NN -= (partN + 1);

			char buf[20];
			snprintf(buf, sizeof buf, "%llu", NN);

			return isTidy(buf);
		}
	}

	printf("%llu\n", NN);

	return true;
}

void work()
{
	// Code here
	char N[20];
	unsigned long long NN;

	scanf("%s\n", N);

	NN = std::stoull(N);

	isTidy(N);

	// printf("%llu  %d\n", NN, isTidy(N) );
}

int main()
{
	freopen("B-large.in", "r", stdin);
	//freopen("A-large-practice.in", "r", stdin);
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w+", stdout);
	freopen("B-large.out.txt", "w+", stdout);

	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; cs++)
	{
		printf("Case #%d: ", cs);
		work();
	}

	return 0;
}
