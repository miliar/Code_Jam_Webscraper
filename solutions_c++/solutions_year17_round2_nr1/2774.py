#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
typedef long long int ll;
using namespace std;

struct Horse
{
	int k, s;
	double t;
};

bool comp (Horse a, Horse b)
{
	return a.k < b.k;
}

int main (void)
{
	int t, d, n, max_id;
	double maxt = -1, result;
	//vector <Horse> horse;
	int k, s;
	double horset;

	//horse.resize(n);

	cin >> t;
	for (int c=1; c<=t; c++)
	{
		maxt = -1;
		cin >> d >> n;

		for (int i=0; i<n; i++)
		{
			/*
			cin >> horse[i].k >> horse[i].s;
			horse[i].t = (double)(d-horse[i].k)/(double)horse[i].s;
			if (horse[i].t > maxt)
			{
				maxt = horse[i].t;
				max_id = i;
			}
			*/

			
			cin >> k >> s;
			horset = (double)(d-k)/(double)(s);
			if (horset > maxt) maxt = horset;
		}
		//sort(horse.begin(), horse.end(), comp);

		result = (double)d/(double)maxt;

		printf("Case #%d: %f\n", c, result);
	}
}