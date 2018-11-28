#pragma warning(disable:4996)
#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	// INPUT AND OUTPUT FILE OPEN
	FILE* fin = fopen("input.txt", "r");
	FILE* fout = fopen("output.txt", "w");
	
	// GET THE NUMBER OF TRY
	int Numbtry;
	fscanf(fin, "%d", &Numbtry);

	// KEEP TRYING WITHIN THE NUMBTRY
	// keep in mind that fprintf(fout, "Case %d: ?\n", n, ?);
	// fscanf(fin, "%d", &Numb);
	//for(int n = 1; n <= Numbtry; n++)
	for (int start = 1; start <= Numbtry; ++start)
	{
		char buffer[1000];
		int k;
		bool notHappy = true;

		fscanf(fin, "%s", buffer);
		fscanf(fin, "%d", &k);
		

		int check = 0;
		int index = 0;
		string s = buffer;

		char* temp = new char[s.size() + 1];
		copy(s.begin(), s.end(), temp);
		temp[s.size()] = '\0';
		char* control = temp;

		//
		for (int i = 0; i < s.size(); ++i)
			if (temp[i] == '+')
				++check;

		if (check == s.size())
		{
			notHappy = false;
			fprintf(fout, "Case #%d: 0\n", start);
			printf("Case #%d: 0\n", start);
		}
		//

		check = 0;

		while (notHappy)
		{
			
			for (int i = 0; i < s.size(); ++i)
				if (temp[i] == '-')
				{
					if ((int)temp + i + (k - 1) <= (int)temp + (int)s.size() - 1)
					{
						control += i;

						for (int j = 0; j < k; ++j)
						{
							if (*control == '-') *control = '+';
							else *control = '-';
							++control;
						}

						++index;
						break;
					}
					else if ((int)temp + i + (k - 1) > (int)temp + (int)s.size() - 1)
					{
						fprintf(fout, "Case #%d: IMPOSSIBLE\n", start);
						printf("Case #%d: IMPOSSIBLE\n", start);
						notHappy = false;
						goto end;
					}
				}

			for (int i = 0; i < s.size(); ++i)
				if (temp[i] == '+')
					++check;
			
			if (check == s.size())
			{
				fprintf(fout, "Case #%d: %d\n", start, index);
				printf("Case #%d: %d\n", start, index);
				notHappy = false;
			}

			control = temp;
			check = 0;
		}
		end:{}
	}
	return 0;
}