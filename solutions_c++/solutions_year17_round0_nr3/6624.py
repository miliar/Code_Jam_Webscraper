#include <iostream>
#include <fstream>
#include <set>
#include <vector>
using namespace std;

pair <int, int> bathroomStalls(int N, int K)
{
	set<int> occupiedStalls;
	occupiedStalls.insert(0);
	occupiedStalls.insert(N+1);

	int lastAddedStall, bestMax, bestMin;
	for (int person = 0; person < K; ++person) {
//		cout << "Person #" << person << endl;
		//create list of occupied stalls
		vector<pair<int,int> > stallPairs;
		for (auto stall = occupiedStalls.begin(); stall != prev(occupiedStalls.end()); ++stall) {
			stallPairs.push_back(pair<int,int>(*stall, *(next(stall, 1))));
		}	
		
		int bestMinSoFar = 0;
		int bestMaxSoFar = 0;
		bestMax = 0;
		bestMin = 0;
		int bestStallSoFar, lastMax, lastMin;
		for (const auto &pair : stallPairs) {
//			cout << "Left stall in pair: " << pair.first << endl;
			//find center
			int centerForPair = (pair.first + pair.second) / 2;
			int rDist = abs(centerForPair - pair.second) - 1;
			int lDist = abs(centerForPair - pair.first) - 1;
//			cout << centerForPair << " " << rDist << " " << lDist << endl;

			lastMax = max(rDist, lDist);
			lastMin = min(rDist, lDist);
			if (lastMin > bestMinSoFar || (lastMin == bestMinSoFar && lastMax > bestMaxSoFar)) {
				bestMinSoFar = lastMin;
				bestMaxSoFar = lastMax;
				bestStallSoFar = centerForPair;
				bestMax = lastMax;
				bestMin = lastMin;
			}
		}
		occupiedStalls.insert(bestStallSoFar);
		lastAddedStall = bestStallSoFar;
	}
	return pair<int, int>(bestMax, bestMin);
}

int main()
{
	ifstream infile("thisInput.txt");
	ofstream outfile("thisOutput.txt");

	int numCases;
	infile >> numCases;

	for (int i = 1; i <= numCases; ++i) {
		int N, K;
		infile >> N >> K;
		pair<int, int> maxMin = bathroomStalls(N, K);
		outfile << "Case #" << i << ": " << maxMin.first << " " << maxMin.second << endl;
	}
}

