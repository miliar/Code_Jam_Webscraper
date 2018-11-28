#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

struct horse
{
	int start;
	double speed;
};
int T;
int dist;
int horseCount = 0;
horse horses[1010];

struct {
	bool operator()(horse a, horse b)
	{
		return a.start < b.start;
	}
} Compare;

double getRightSide(int st, double speed)
{
	return ((st / ((double)(dist - st)/speed))) + speed;
}

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d%d", &dist, &horseCount);
		for (int h = 0; h < horseCount; h++)
		{
			int d, s;
			scanf("%d%d", &d, &s);
			horses[h].start = d;
			horses[h].speed = s;
		}
		sort(horses, &horses[horseCount - 1], Compare);
		double speed = 0;
		horse curHorseR = horses[horseCount - 1];
		speed = getRightSide(curHorseR.start, curHorseR.speed);
		for (int j = horseCount - 2; j >= 0; j--)
		{
			curHorseR = horses[j];
			speed = min(speed, getRightSide(curHorseR.start, curHorseR.speed));
		}
		printf("Case #%d: %f\n", i + 1, speed);
	}

	return 0;
}