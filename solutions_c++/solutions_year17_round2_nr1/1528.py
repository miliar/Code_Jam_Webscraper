
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>

#define FO(X,Y) for(int X = 0; X < (Y); X++)

using namespace std;

string solve(istream& in)
{
	int distance;
	int horseCount = 0;

	in >> distance;
	in >> horseCount;

	long double largestTimeTaken = 0;

	for (int i = 0; i < horseCount; i++)
	{
		int position;
		long double speed;
		in >> position;
		{
			int tempSpeed;
			in >> tempSpeed;
			speed = tempSpeed;
		}
		long double testTimeTaken = (distance - position) / speed;
		largestTimeTaken = largestTimeTaken > testTimeTaken ? largestTimeTaken : testTimeTaken;
	}

	char result[512];

	sprintf_s(result, 500, "%.6f", distance / largestTimeTaken);

	return string(result);
}

void main()
{
	ifstream in = ifstream("A-large.in");
	ofstream out = ofstream("A-large.out");

	int numberOfCases;

	in >> numberOfCases;

	for (int i = 0; i < numberOfCases; i++)
	{
		string result = solve(in);



		cout << "Case #" << i + 1 << ": " << result << endl;
		out << "Case #" << i + 1 << ": " << result << endl;
	}

	in.close();
	out.close();
}


