#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
	int testCase;
	ofstream output("answer.txt");
	ifstream input("C-large.in");
	long long stall;
	long long people;
	long long nowStall;
	long long future;
	long long nowFuture;
	pair<long long, long long> tmp[2];
	vector<pair<long long, long long>> turn(2, {0,0});
	input >> testCase;
	for (int t = 1; t <= testCase; t++)
	{
		input >> stall;
		input >> people;
		turn[0] = { stall,1 };
		turn[1] = { 0,0 };
		future = 1;
		nowFuture = 1;
		for (;future < people;)
		{
			tmp[0] = turn[0];
			tmp[1] = turn[1];
			if (tmp[0].first % 2 == 0)
			{
				turn[0].first = tmp[0].first / 2;
				turn[1].first = tmp[0].first / 2 - 1;
				turn[1].second = tmp[0].second;
			}
			else
			{
				turn[0].first = tmp[0].first / 2;
				turn[0].second *= 2;
			}
			if ((tmp[1].first != 0) && (tmp[1].first % 2 == 0))
			{
				turn[0].second += tmp[1].second;
				turn[1].first = tmp[1].first / 2-1;
				turn[1].second = tmp[1].second;
			}
			else if (tmp[1].first % 2 != 0)
			{
				turn[1].second += tmp[1].second * 2;
			}
			if (turn[1].first == 0)
				turn[1].second = 0;
			nowFuture = turn[0].second + turn[1].second;
			future += nowFuture;
		}
		nowFuture = nowFuture - (future - people);
		nowStall = turn[0].first;
		if (nowFuture > turn[0].second)
			nowStall = turn[1].first;
		if (nowStall % 2 == 0)
			output << "Case #" << t << ": " << nowStall / 2 << " " << nowStall / 2 - 1 << "\n";
		else
			output << "Case #" << t << ": " << nowStall / 2 << " " << nowStall / 2 << "\n";
	}
	return 0;
}