#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

bool IsTidyNum(unsigned long long i)
{
	unsigned long long tmp =i;
	unsigned long long pre;
	unsigned long long d ;

	pre = tmp %10;
	tmp = i/10;
	bool r = true;
	while(tmp > 0)
	{
		d = tmp % 10;
		tmp = tmp / 10;
		if (pre >= d)
		{
			pre = d;
			continue;
		}
		else
		{
			r = false;
			break;
		}
	}
	return r;
}

int GetDigitCount(long long n)
{
	int count = 0;
	while(n != 0)
    {
        n /= 10;
        ++count;
    }
	return count;
}

unsigned long long NextNum(unsigned long long nn, int len)
{
	int prevdigit = nn / pow((double)10, len -1);
	for( int i = len-2; i >= 0 ; i--)
	{
		unsigned long long digit = (unsigned long long)(nn / (unsigned long long)pow((double)10, i));
		digit = digit % 10;
		if(prevdigit > digit)
		{
			nn = nn - (nn % (unsigned long long)pow((double)10, i+1)) - 1;
			break;
		}
		prevdigit = digit;
	}
	return nn;
}


int main() {
	FILE* fpin = fopen("c:\\Blarge.in", "r");
	FILE* fpout = fopen("c:\\Blarge.out","w");

	int T;
	fscanf(fpin, "%d", &T);
	unsigned long long N;

	for(int i = 0; i < T; i++)
	{
		fscanf(fpin, "%lld", &N);
		fprintf(fpout, "Case #%d: ", i+1);
		if (N < 10)	
			fprintf(fpout, "%d\n", N);
		else
		{
			int len = GetDigitCount(N);

			while(true)
			{
				if(!IsTidyNum(N))
				{
					N = NextNum(N, len);
				}
				else
				{
					fprintf(fpout, "%lld\n", N);
					break;
				}
			}
		}
	}

	fclose(fpin);
	fclose(fpout);

	return 0;
}
