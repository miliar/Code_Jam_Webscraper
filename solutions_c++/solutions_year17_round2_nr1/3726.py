#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef enum { Cruise, Unicorns, Pony }Problems;

static const Problems PROBLEM = Cruise;

void horseCruise(int dest, vector<pair<double,double>> &horses)
{
	sort(horses.begin(), horses.end());
	reverse(horses.begin(), horses.end());
	double totalTime, curTime;
	for (size_t i = 0; i < horses.size(); i++)
	{
		if (i == 0)
			totalTime = (dest - horses[i].first) / horses[i].second;
		else
		{
			double destCur, destPrev;
			destCur = dest - horses[i].first;
			destPrev = dest - horses[i - 1].first;
			curTime = (destCur - destPrev) / horses[i].second;
			double prevSpeed = (destPrev / totalTime);
			if (prevSpeed < horses[i].second && ((destCur - destPrev) / (horses[i].second - prevSpeed)) < totalTime)
				;
			else
				totalTime = curTime + destPrev / horses[i].second;
		}
	}

	printf("%.6f\n", dest / totalTime);
}

void unicornStalls(string &cakes, int &size)
{

}

void ponyExpress(long long stallCount, long long personCount)
{

}

int main()
{
	unsigned int loopcount;
	cin >> loopcount;
	switch (PROBLEM)
	{
	case Cruise:
		for (size_t i = 0; i < loopcount; i++)
		{
			int destination, numOfHorses;
			cin >> destination >> numOfHorses;
			vector<pair<double, double>> horses;
			for (int j = 0; j < numOfHorses; j++)
			{
				double loc, speed;
				cin >> loc >> speed;
				horses.push_back(pair<double, double>(loc, speed));
			}
			cout << "Case #" << i + 1 << ": ";
			horseCruise(destination, horses);
		}
		break;
	case Unicorns:
		for (size_t i = 0; i < loopcount; i++)
		{

		}
		break;
	case Pony:
		for (size_t i = 0; i < loopcount; i++)
		{

		}
		break;
	default:
		break;
	}

	return 0;
}