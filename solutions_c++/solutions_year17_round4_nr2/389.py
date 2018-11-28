#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>

void solveOne(int iTest) {
	int nSeats, nCust, nTick;
	scanf("%d %d %d", &nSeats, &nCust, &nTick);
	std::vector<int> posToCount(1 + nSeats);
	std::vector<int> ticketsPerCust(1 + nCust);
	for (int i = 0; i < nTick; i++) {
		int pos, cust;
		scanf("%d %d", &pos, &cust);
		ticketsPerCust[cust]++;
		posToCount[pos]++;
	}
	int rides = 0;
	for (int i = 1; i <= nCust; i++) {
		rides = std::max(rides, ticketsPerCust[i]);
	}
	{
		int tickSum = 0;
		for (int pos = 1; pos <= nSeats; pos++) {
			tickSum += posToCount[pos];
			while (pos * rides < tickSum) {
				rides++;
			}
		}
	}
	int moves = 0;
	for (int pos = 1; pos <= nSeats; pos++) {
		if (posToCount[pos] > rides) {
			moves += posToCount[pos] - rides;
		}
	}
	printf("Case #%d: %d %d\n", iTest, rides, moves);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		solveOne(i);
	}
	return 0;
}
