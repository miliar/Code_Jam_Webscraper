// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;

void number2(int a, int b,int i);
void number3(int a, int b, int c,int i);
int main()
{
	int t, n, i;
	int a[3];
	int count;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		count = 0;
		scanf("%d", &n);
		if (n == 1000) {
			printf("Case #%d: %d\n", i, 999);
		}
		else {
			while (n > 0) {
				a[count++] = n % 10;
				n = n / 10;
			}
			switch (count) {
			case 1: printf("Case #%d: %d\n", i, a[0]); break;
			case 2: number2(a[0], a[1],i); break;
			case 3: number3(a[0], a[1], a[2],i); break;
			}
		}
	}
    return 0;
}
void number2(int a, int b,int i) {
	if (a >= b) {
		printf("Case #%d: %d%d\n", i, b, a);
	}
	else {
		b = b - 1;
		a = 9;
		if (b == 0)
			printf("Case #%d: %d\n", i, a);
		else
			printf("Case #%d: %d%d\n", i, b, a);
	}
}

void number3(int a, int b, int c, int i) {
	if (c > b) {
		c = c - 1;
		b = 9;
		a = 9;
		if (c == 0)
			printf("Case #%d: %d%d\n", i, b, a);
		else
			printf("Case #%d: %d%d%d\n", i, c, b, a);
	}
	else {
	if(a>=b)
		printf("Case #%d: %d%d%d\n", i, c, b, a);
	else {
		if (b - 1 >= c) {
			a = 9;
			b = b - 1;
			printf("Case #%d: %d%d%d\n", i, c, b, a);
		}
		else {
			c = c - 1;
			b = 9;
			a = 9;
			if (c == 0)
				printf("Case #%d: %d%d\n", i, b, a);
			else
				printf("Case #%d: %d%d%d\n", i, c, b, a);
		}
	}
	}
}

