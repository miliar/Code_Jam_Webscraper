#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>

#define F0(a,b) for(a = 0; a < b; a++)
#define F1(a,b) for(a = 1; a <= b; a++)
#define FN(a,b) for(a = b - 1; a >= 0; a--)

using namespace std;

struct horseStats
{
	int pos;
	int speed;
};

struct horseComp
{
	bool operator()(const horseStats& h1, const horseStats& h2)
	{
		return h1.pos < h2.pos;
	}
};

void main()
{
	int T, tc;

	cin >> T;

	F1(tc, T)
	{
		int D, N;

		cin >> D >> N;

		priority_queue<horseStats, std::vector<horseStats>, horseComp> horses;

		int i;
		F0(i, N)
		{
			horseStats newHorse;
			cin >> newHorse.pos >> newHorse.speed;

			horses.push(newHorse);
		}

		double lastHorseArrivalTime = 0;

		while(!horses.empty())
		{
			horseStats horse = horses.top();
			horses.pop();

			double currentArrivalTime = (D - horse.pos) / (double)horse.speed;

			if (currentArrivalTime > lastHorseArrivalTime)
			{
				lastHorseArrivalTime = currentArrivalTime;
			}
		}

		double result = D / (double)lastHorseArrivalTime;

		cout << "Case #" << tc << ": " << fixed << setprecision(6) << result << endl;
	}
}