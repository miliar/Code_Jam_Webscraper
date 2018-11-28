
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>

#define FO(X,Y) for(int X = 0; X < (Y); X++)

using namespace std;

typedef unsigned long long BIGNO;

BIGNO calculateBaseTwo(BIGNO input)
{
	int testValue = 1;
	while (true)
	{
		if (testValue > input)
		{
			return testValue / 2;
		}
		testValue *= 2;
	}
	return -1;
}

void solve(ofstream& out, BIGNO stalls, BIGNO users)
{
	BIGNO baseTwoOfUsers = calculateBaseTwo(users);

	BIGNO offset = users - 1;
	BIGNO position = (stalls - offset + baseTwoOfUsers - 1) / baseTwoOfUsers;

	BIGNO min = (position - 1) / 2;
	BIGNO max = (position + 0) / 2;


	cout << max << " " << min;
	out << max << " " << min;
}

void main()
{
	ifstream in = ifstream("C-small-2-attempt0.in");
	ofstream out = ofstream("C-small-2-attempt0.out");

	int numberOfCases;

	in >> numberOfCases;

	for (int i = 0; i < numberOfCases; i++)
	{
		BIGNO stalls;
		BIGNO users;
		in >> stalls;
		in >> users;


		cout << "Case #" << i + 1 << ": ";
		out << "Case #" << i + 1 << ": ";
		solve(out, stalls, users);
		cout << endl;
		out << endl;
	}

	in.close();
	out.close();
}


