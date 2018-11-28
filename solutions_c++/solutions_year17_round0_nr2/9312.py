#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#define LL long long

bool isTidy(const char* x)
{
	int prev = -1;
	for (int i = 0; x[i]; i++)
	{
		if ((x[i] - '0') >= prev)
		{
			prev = x[i] - '0';
		}
		else
		{
			return false;
		}
	}
	return true;
}

LL StringToLL(char* str)
{
	char* rev = new char[strlen(str)];
	strcpy(rev, str);
	strrev(rev);
	LL result = 0;
	LL radix = 1;
	for (int i = 0; rev[i]; i++)
	{
		result += (rev[i] - '0')*radix;
		radix *= 10;
	}
	return result;
}

int main(void)
{
	FILE* in = fopen("B-small-attempt0.in", "r");
	FILE* out = fopen("B-small-output.out", "w");
	int TestCase;
	fscanf(in, "%d", &TestCase);
	for (int tc = 0; tc < TestCase; tc++)
	{
		char n[20];
		fscanf(in, "%s", n);
		for (LL i = StringToLL(n); i > 0; i--)
		{
			if (isTidy(std::to_string(i).c_str()))
			{
				fprintf(out,"Case #%d: %d\n", tc + 1, i);
				break;
			}
		}
	}
}