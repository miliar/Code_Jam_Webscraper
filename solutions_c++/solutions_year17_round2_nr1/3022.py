// Template.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

#define F0(i,n) for(i=0; i< n; ++i)
#define F1(i,n) for(i=1; i<=n; ++i)
#define FX(i,x,n) for(i=x; i< n; ++i)

using namespace std;

void horses()
{
	double dest;
	int n; // no of horses
	int i;
	double start;
	double speed;
	double time = 0;
	double maxtime = 0;
	double maxspeed = 0;

	cin >> dest >> n;
	F0(i, n)
	{
		cin >> start >> speed;
		time = (dest - start) / speed;
		if (maxtime < time)
			maxtime = time;
	}
	maxspeed = dest / maxtime;
	printf("%f\n", maxspeed);
}

int main()
{
	freopen("sample.in", "r", stdin);
	freopen("sample.out", "w", stdout);

	int i,t;
	cin >> t;
	F1(i, t)
	{
		printf("Case #%d: ", i);
		horses();
	}

    return 0;
}

