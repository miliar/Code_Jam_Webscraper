#include <iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>

using namespace std;

ifstream in;
ofstream out;




int main()
{
	in.open("B-large.in");
	out.open("out.txt");
	int casses;
	in >> casses;

	for (int i = 0; i < casses; i++)
	{
		string broj;
		in >> broj;
		string izlaz;
		cout <<"ulaz:"<<i+1<<":"<< broj << endl;
		while (broj.length() > 1)
		{
			if (broj.at(broj.length()-1) < broj.at(broj.length() - 2))
			{
				izlaz += '9';
				broj.erase(broj.length()-1, 1);
				--broj.at(broj.length()-1);
				while (broj.at(broj.length()-1) < '0')
				{
					izlaz += '9';
					broj.erase(broj.length()-1, 1);
					--broj.at(broj.length()-1);
				}
			}
			else
			{
				izlaz += broj.at(broj.length()-1);
				broj.erase(broj.length()-1, 1);
			}

		}

		if (broj.length() != 0)
		{
			if (broj.at(0) > '0')
				izlaz += broj;
		}
		reverse(izlaz.begin(), izlaz.end());
		for (int s = 0; s < izlaz.length()-1; s++)
		{
			if (izlaz.at(s) > izlaz.at(s + 1))
			{
				izlaz.replace(s + 1, izlaz.length()-s-1, izlaz.length() - s - 1, '9');

			}
		}
		out << "Case #" << i + 1 << ": " << izlaz << endl;
		}

	int x;
	cin>> x;
	return 0;
}
