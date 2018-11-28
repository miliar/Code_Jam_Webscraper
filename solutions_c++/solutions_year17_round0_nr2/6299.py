
#include <iostream>
#include <fstream>
using namespace std;


void main()
{
	ifstream in("B-large.in");
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
		in.getline(Buffer, 1024);
		int Len = strlen(Buffer);

		int Largest = 0;
		for (int j = 0; j < Len; j++)
		{
			if (Buffer[j] > Buffer[Largest])
				Largest = j;
			else if (Buffer[j] < Buffer[Largest])
			{
				Buffer[Largest]--;
				for (int k = Largest+1; k < Len; k++)
					Buffer[k] = '9';
				break;
			}
		}

		out << "Case #" << i + 1 << ": " << (Buffer[0] == '0' ? Buffer+1 : Buffer) << endl;
	}
}
