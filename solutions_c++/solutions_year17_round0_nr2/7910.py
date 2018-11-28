#include <iostream>
#include <string>
#include <string.h>
#include <cstdlib>
#include <cstdio>
#include <cfloat>
#include <vector>
#include <fstream>
#include <time.h>
#include <math.h>


using namespace std;

long long int tidy(long long int a)
{
	long long int d = 1;
	long long int num = 0;
	long long int current = a%10;
	long long int next = (a%100)/10;
	//int repeat = 0;
	while(a/10 != 0)
	{
		current = a%10;
		next = (a%100)/10;
		if(current == 0 || current < next)
		{
			if(current == 0)
			{
				a--;
				num = d-1;	
			}
			else
			{
				a = (a/10)-1;
				d = d*10;
				num = d-1;
				//repeat = 1;
				return tidy((a*d)+num);
			}
		}
		else
		{
			num  = num + (d*current);
			a = a/10;
			d = d*10;
		}
	}

		return ((a*d)+num);

}

int main()
{
 	int t;
	long long int n;
	fstream f1,f2;
	f2.open("output.txt", ios::in|ios::out|ofstream::trunc);
	f1.open("input.txt",ios::in|ios::out);
	f1>>t;
	for(int k = 0; k < t; k++)
	{
		f1>>n;
		f2<<"Case #"<<k+1<<": "<<tidy(n)<<endl;
	}

	f2.close();
	f1.close();

}
