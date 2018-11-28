#include <iostream>
#include <fstream>

using namespace std;

int main()
{

	ifstream fin("input.in");
	ofstream fout("output.out");

	int t;

	fin >> t;

	for (int test = 0; test < t; test++)
	{
		long long inp, inp1;
		int id;
		id = 0;
		int number[20] = { 0 };

		fin >> inp;

		inp1 = inp;

		while (inp1 != 0)
		{
			number[id] = inp1 % 10;
			inp1 = inp1 / 10;
			id++;
		}

		bool prov = true;

		for (int i = 19; i >= 1; i--)
		{
			if (number[i] > number[i - 1]) prov = false;
		}

		if (prov == false)
		{

			int pos = 0;
			int max_num = -1;
			
			int beg = 19;
			while (number[beg] == 0) beg--;
			for (int i = beg; i >= 1; i--)
			{
				pos = i;
				if (number[i] > number[i - 1]) break;
			}

			while (number[pos] == number[pos + 1]) pos++;

			number[pos]--;
			for (int i = pos - 1; i >= 0; i--)
			{
				number[i] = 9;
			}

			long long ans = 0;
			for (int i = 19; i >= 0; i--)
			{
				ans = ans * 10 + number[i];
			}

			fout << "Case #" << test + 1 << ": " << ans << endl;
		}
		else fout << "Case #" << test + 1 << ": " << inp << endl;
	}


	fin.close();
	fout.close();
	


	return 0;
}