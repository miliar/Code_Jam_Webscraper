#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>

#define LLI unsigned long long int

using namespace std;

char digits[20];
int nDigs;
void readDigits(LLI in);
string writeDigits();

int main()
{
	ios_base::sync_with_stdio();
	int T;
	cin >> T;
	for(int aa=0;aa<T;++aa)
	{
		LLI N;
		cin >> N;
		readDigits(N);
		if(nDigs != 1)
		{
			for(int i=1;i<nDigs;++i)
			{
				if(digits[i] > digits[i-1] && digits[i] != 0)
				{
					for(int j=0;j<i;++j)
					{
						digits[j] = 9;
					}
					digits[i]--;
				}
			}
			if(digits[nDigs-1] == 0)
				nDigs--;
		}
		
		cout << "Case #" << aa+1 << ": " << writeDigits() << endl;
	}


	return 0;
}

void readDigits(LLI in)
{
	nDigs = 0;
	while(in > 0)
	{
		digits[nDigs] = (char) (in%10);
		in /= 10;
		++nDigs;
	}
}
string writeDigits()
{
	string out;
	for(int i=nDigs-1;i>=0;--i)
	{
		out += (char) (digits[i] + '0');
	}
	return out;
}
