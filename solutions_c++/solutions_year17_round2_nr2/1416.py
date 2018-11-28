#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <string>
#include <iomanip>
#include <algorithm>
typedef long long int LL;
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{

	long long int num_t, N,cnt,R,C;
	fin >> num_t;
	cnt = 1;
	while (num_t--)
	{
		int N, R, O, Y, G, B, V;
		fin >> N >> R >> O >> Y >> G >> B >> V;

		int mm = max(max(R, B), Y);
		int sum = R + B + Y;
		sum = sum - mm;

		string s[3];
		s[0] = "R";
		s[1] = "Y";
		s[2] = "B";
		int mm2, mm3;
		mm2 = Y;
		mm3 = B;
		if (mm == R)
			s[0] = "R";
		else if (mm == B)
		{
			s[0] = "B";
			s[2] = "R";
			mm3 = R;
		}
		else
		{
			s[0] = "Y";
			s[1] = "R";
			mm2 = R;
		}
		
		fout << "Case #" << cnt++ << ": ";
		
		if (sum<=mm-1)
		{
			fout << "IMPOSSIBLE" << endl;
			continue;
		}
		while (1)
		{
			if (mm2 + mm3 <= mm)
			{
				fout << s[0];
				mm--;
				if (mm2 > 0)
				{
					mm2--;
					fout << s[1];
				}
				else if (mm3 > 0)
				{
					mm3--;
					fout << s[2];
				}
			}
			else
			{
				fout << s[0] << s[1] << s[2];
				mm--; mm2--; mm3--;
			}

			if (mm == 0)
			{
				while (mm2--)
				{
					fout << s[1];
					if (mm3 > 0)
					{
						mm3--;
						fout << s[2];
					}
				}
				if (mm3 != 0)
					fout << s[2];
				break;
			}
		}

		fout << endl;
	}
}