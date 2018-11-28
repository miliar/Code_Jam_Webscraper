
#include <iostream>
#include <fstream>
using namespace std;

struct State
{
	bool It[1024];
	int Num;
};

void main()
{
	ifstream in("A-large.in");
	if (!in)
	{
		cout << "Fehler!" << endl;
		return;
	}
	ofstream out("out.txt");

	int Num;
	in >> Num;
	in.ignore();

	for (int i = 0; i < Num; i++)
	{
		char Buffer[1024];
		in.getline(Buffer, 1024, ' ');
		int Size;
		in >> Size;
		in.ignore();

		State S;
		S.Num = strlen(Buffer);
		for (int j = 0; j < S.Num; j++)
			S.It[j] = Buffer[j] == '+';

		int Flips = 0;
		for (int j = 0; j <= S.Num - Size; j++)
			if (!S.It[j])
			{
				Flips++;
				for (int k = 0; k < Size; k++)
					S.It[j + k] = !S.It[j + k];
			}

		out << "Case #" << i + 1 << ": ";
		for (int j = 0; j < S.Num; j++)
			if (!S.It[j])
			{
				out << "IMPOSSIBLE" << endl;
				goto Next;
			}
		out << Flips << endl;
		Next:;
	}
}