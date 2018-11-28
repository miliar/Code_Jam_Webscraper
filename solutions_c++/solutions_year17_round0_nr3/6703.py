#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

string findMinMaxLR(string rooms, int N, int K);

int main()
{
	ifstream inFile("C-small-1-attempt0.in");
	ofstream outFile("C-small-1-attempt0.out");
	int T;
	int N;
	int K;
	string rooms;

	inFile >> T;

	for (int i = 0; i < T; i++)
	{
		inFile >> N >> K;
		rooms.assign(N, '.');
		rooms = 'o' + rooms + 'o';

		outFile << "Case #" << i + 1 << ": " << findMinMaxLR(rooms, N, K) << endl;
	}

	return 0;
}

string findMinMaxLR(string rooms, int N, int K)
{
	int count = 0;
	int maxLR = -1;
	int minLR = -1;
	int index = -1;
	int L, R;

	while (count < K)
	{
		minLR = maxLR = -1;
		for (int i = 1; i <= N; i++)
		{
			if (rooms.at(i) == 'o')
				continue;
			
			L = R = 0;

			for (int j = i - 1; j >= 0; j--)
			{
				if (rooms.at(j) == 'o')
					break;
				else
					L++;
			}

			for (int k = i + 1; k <= N + 1; k++)
			{
				if (rooms.at(k) == 'o')
					break;
				else
					R++;
			}

			if (min(L, R) > minLR)
			{
				minLR = min(L, R);
				maxLR = max(L, R);
				index = i;
			}
			else if (min(L, R) == minLR)
			{
				if (max(L, R) > maxLR)
				{
					minLR = min(L, R);
					maxLR = max(L, R);
					index = i;
				}
			}
		}

		if(count <= K)
			rooms.at(index) = 'o';

		count++;
	}

	return to_string(maxLR) + " " + to_string(minLR);
}