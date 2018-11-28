// a-steed.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>
using namespace std;

#define ull unsigned long long

void runCase()
{
	double distance = 0;
	ull numHorses = 0;
	cin >> distance >> numHorses;

	double answerSpeed = 0.0;

	for (ull i = 0; i < numHorses; i++)
	{
		double oKilometer = 0;
		double oSpeed = 0;
		cin >> oKilometer >> oSpeed;
		double oDistance = distance - oKilometer;
		double time = oDistance / oSpeed;
		double speed = distance / time;
		if (i == 0 || speed < answerSpeed)
		{
			answerSpeed = speed;
		}
	}

	printf("%.6lf", answerSpeed);
}

int main()
{
	int numCases = 0;
	cin >> numCases;
	
	for (int i = 0; i < numCases; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		runCase();
		cout << endl;
	}	

    return 0;
}

