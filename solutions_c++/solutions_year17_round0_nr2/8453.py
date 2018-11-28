#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

using namespace std;

long long int make_num(long long int num);
int len_ll(long long int num);
int num_in_add(int add, long long int num);

int main()
{
	int t,len;
	long long int num=0;
	FILE *pf_r,*pf_w;

	pf_r = fopen("B-large.in", "r");
	pf_w = fopen("B-large.out", "w+");
	fscanf(pf_r,"%d", &t);
	for (int i = 0; i < t; i++)
	{
		fscanf(pf_r,"%lld", &num);
		len = len_ll(num);
		for(int j=0;j<len;j++)
			num = make_num(num);
		fprintf(pf_w,"Case #%d: %lld\n", i + 1, num);
	}

}
long long int make_num(long long int num)
{
	int len = len_ll(num);
	int key = 0,a,b;
	long long int ans = 0;
	for (int i = len; i > 0; i--)
	{
		a = num_in_add(i, num);
		b = num_in_add(i - 1, num);
		//printf("%d %d %d\n", i, a, b);
		if (key == 1)
		{
			ans *= 10;
			ans += 9;
		}
		else if (a > b)
		{
			key = 1;
			ans *= 10;
			ans += a - 1;
		}
		else
		{
			ans *= 10;
			ans += a;
		}
	}
	return ans;
}
int len_ll(long long int num)
{
	int n = 0;
	while (num > 0)
	{
		n++;
		num /= 10;
	}
	return n;
}
int num_in_add(int add, long long int num)
{
	for (int i = 1; i < add; i++)
		num /= 10;
	return num % 10;
}