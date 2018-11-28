#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");

	in.seekg(0, ios::beg);

	int T;
	in >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		char cake[26][26];
		int R, C;
		in >> R >> C;

		for (int j = 0; j < R; j++)
		{
			for (int i = 0; i < C; i++)
			{
				in >> cake[j][i];
			}
		}

		char tmp = '?';
		for (int j = 0; j < R; j++)
		{
			tmp = '?';
			for (int i = 0; i < C; i++)
			{
				if (cake[j][i] != '?')
					tmp = cake[j][i];
				else
					cake[j][i] = tmp;
			}
			tmp = '?';
			for (int i = C - 1; i >= 0; i--)
			{
				if (cake[j][i] != '?')
					tmp = cake[j][i];
				else
					cake[j][i] = tmp;
			}
		}

		for (int i = 0; i < C; i++)
		{
			tmp = '?';
			for (int j = 0; j < R; j++)
			{
				if (cake[j][i] != '?')
					tmp = cake[j][i];
				else
					cake[j][i] = tmp;
			}
			tmp = '?';
			for (int j = R - 1; j >= 0; j--)
			{
				if (cake[j][i] != '?')
					tmp = cake[j][i];
				else
					cake[j][i] = tmp;
			}
		}

		out << "Case #" << Case << ":" << endl;
		for (int j = 0; j < R; j++)
		{
			for (int i = 0; i < C; i++)
			{
				out << cake[j][i];
			}
			out << endl;
		}
	}


	return 0;
}