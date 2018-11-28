#include "stdafx.h"
#include <iostream>
#include <set>
#include <iomanip>  

using namespace std;

struct Horse
{
	Horse(const long long thePos, const int theSpeed) : myPos(thePos), mySpeed(theSpeed), myTime(0) {}
	Horse() : myPos(0), mySpeed(0), myTime(0) {}
	void Compute(const long long theDistance)
	{
		myTime = (theDistance - myPos) / (long double)mySpeed;
	}
	bool operator < (const Horse &theOther)
	{
		return myTime > theOther.myTime;
	}
	long long myPos;
	int mySpeed;
	long double myTime;

};

bool operator < (const Horse &theOne, const Horse &theOther)
{
	return theOne.myTime > theOther.myTime;
}

void main() {
	int t;

	cin >> t;


	for (int i = 1; i <= t; ++i) {
		long long D;
		int N;

		cin >> D >> N;

		int j;
		set<Horse> aHorses;

		for (j = 0; j < N; ++j) {
			Horse aHorse;

			cin >> aHorse.myPos >> aHorse.mySpeed;

			aHorse.Compute(D);
			aHorses.insert(aHorse);
		}

		const Horse &aHorse = *(aHorses.begin());

		long double aResult = D / aHorse.myTime;
		//cout << n << endl;
		cout << "Case #" << i << ": " << setprecision(15) << aResult << endl;
	}
}
