#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;


void main()
{
	ifstream in("A-large.in");
	if (!in)
	{
		cout << "Fehler!" << endl;
		return;
	}
	//ofstream out("out.txt");
	FILE* out = fopen("out.txt", "w");

	int Num;
	in >> Num;
	in.ignore();

	for (int i = 0; i < Num; i++)
	{
		double Destination;
		int Horses;
		in >> Destination >> Horses;
		double MaxTime = 0;
		for (int j = 0; j < Horses; j++)
		{
			double Start, Speed;
			in >> Start >> Speed;
			MaxTime = std::max(MaxTime, (Destination - Start) / Speed);
		}

		//out << "Case #" << i + 1 << ": " << (Destination / MaxTime) << endl;
		fprintf(out, "Case #%i: %f\n", i + 1, Destination / MaxTime);
	}
	fclose(out);
}
