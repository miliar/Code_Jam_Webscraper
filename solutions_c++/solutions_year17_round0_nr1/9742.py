#include<stdio.h>
#include <fstream>
#include <string>
#include <iostream>
#pragma warning(disable:4996)
using namespace std;
int f(int lambda, int n, int d)
{
	int i, nc = lambda*n;
	while (nc>0)
	{
		i = nc % 10;
		nc /= 10;
		if ((d >> i) % 2 == 0)
			d += 1 << i;
	}
	if (d == (1 << 10) - 1)
		return lambda*n;
	return f(lambda + 1, n, d);
}

int main()
{



	int t, i, swaps = 0, flag = 0;;
	unsigned int upr, j = 0, n;
	string pc;
	scanf("%d", &t);





	for (i = 0; i < t; i++)
	{

			cin >> pc;
			scanf_s("%d", &n);
	

		printf("Case #%d: ", i + 1);
		if (pc.find('-') == -1){
			printf("0\n");
			continue;
		}
		if (n == 2 && pc.length() == 2){

			
			if (pc[0] != pc[1])
			{
				printf("IMPOSSIBLE\n");
				continue;
			}
			if (pc[0]=='-' && pc[1]=='-')
			{
				printf("1\n");
				
			}
			else 
				printf("0\n");
			continue;
		}
		
		else
		{

			for (j = 0; j < pc.length();){

				if (pc[j] == '+')
				{
					j++;
					continue;
				}

				upr = j + n;
				if (upr >= pc.length())
				{
					upr = pc.length();
					j = pc.length() - n;
				}

				string sub = pc.substr(j, n);
				int kk = sub.find('+');

				for (unsigned int k = j; k < (j + n); k++)
				{
					if (pc[k] == '-')pc[k] = '+';
					else pc[k] = '-';
				}

				swaps++;

				if (kk != -1)
					j = kk;
				else
					j = upr;


				int ll = pc.length() - n;
				if (upr >= pc.length() && (pc.substr(ll, pc.length()).find('-') != -1))
				{
					printf("IMPOSSIBLE\n");
					swaps = 0;
					flag = 1;
					break;
				}
			}
			if (!flag == 1)
			{

				printf("%d\n", swaps);
				swaps = 0;
			}
			flag = 0;

		}


	}
	return 0;
}