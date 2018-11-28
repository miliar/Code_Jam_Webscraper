#pragma warning(disable:4996)
#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	// INPUT AND OUTPUT FILE OPEN
	FILE* fin = fopen("input3.txt", "r");
	FILE* fout = fopen("output3.txt", "w");
	
	// GET THE NUMBER OF TRY
	int Numbtry;
	fscanf(fin, "%d", &Numbtry);

	// KEEP TRYING WITHIN THE NUMBTRY
	// keep in mind that fprintf(fout, "Case %d: ?\n", n, ?);
	// fscanf(fin, "%d", &Numb);
	//for(int n = 1; n <= Numbtry; n++)
	for (int start = 1; start <= Numbtry; ++start)
	{
		long long unsigned int k;
		char* tidybuffer = NULL;

		fscanf(fin, "%lld", &k);

		for (long long unsigned int j = 1; j <= k; ++j)
		{
			string s;
			s = to_string(j);

			char* temp = new char[s.size() + 1];
			copy(s.begin(), s.end(), temp);
			temp[s.size()] = 0;
			char* control = temp;

			char standard = *control;
			
			for (int i = 0; i < s.size(); ++i)
			{
				++control;
				if ((int)(standard) <= (int)(*control))
				{
					standard = *control;
				}
				else
					break;

				if (control == temp + s.size() - 1)
				{
					tidybuffer = temp;
				}

			}

			if (j <= 9)
			{
				char* k = new char[2];
				k[0] = j + 48;
				k[1] = '\0';
				tidybuffer = k;
			}
		}

		printf("Case #%d: %s\n", start, tidybuffer);
		fprintf(fout, "Case #%d: %s\n", start, tidybuffer);
	}
	return 0;
}