#include<stdio.h>
#include <fstream>
#include <string>
#include <array>
#include <iostream>
#pragma warning(disable:4996)
using namespace std;

bool check(unsigned int n){

	unsigned int	temp = n;
	unsigned int r = temp % 10, s;

	bool flag = 1;
	temp = temp / 10;
	while (temp != 0){



		s = temp % 10;

		if (r < s){
			flag = 0; break;
		}
		else
		{
			r = s;
		}
		temp = temp / 10;
	}

	return flag;

}


int main()
{

	int t, i;
	unsigned int n;
	scanf("%d", &t);


	unsigned answer;

	for (i = 0; i < t; i++)
	{



		//	cin >> pc;
			scanf_s("%d", &n);

	


		printf("Case #%d: ", i + 1);


		if (n<10){

			answer = n;

		}
		else if (n % 10 == 0)
		{
			answer = n - 1;
		}

		else {

			if (check(n))answer = n;

			else{
				for (unsigned int i = n; i > 0; i--)
				{
					if (check(i)){ answer = i; break; }
				}

			}

		}

		printf("%d\n", answer);
	}
	return 0;
}