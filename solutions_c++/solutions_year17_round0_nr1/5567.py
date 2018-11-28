#include <iostream>
#include <bitset>
#include <string>
#include <algorithm>
#include <queue>

#define MAXPANCACKES 10

using namespace std;

struct pancakeState
{
	bitset<MAXPANCACKES> state;
	int flips;
	int lastFlip;

	pancakeState()
	{
		flips = 0;
		lastFlip = -1;
	}

	void flip(const int pos, const int flipperSize)
	{
		for (int i = 0; i < flipperSize; i++)
		{
			state.flip(pos + i);
		}

		flips++;
	}
};

int flipsDemPancackesBoy(pancakeState &initState, const int flipperSize, const int numPancakes)
{
	//cout << initState.state << endl;

	if (initState.state.count() == numPancakes)
	{
		return initState.flips;
	}

	queue<pancakeState> q;
	q.push(initState);	

	while (!q.empty())
	{
		pancakeState state = q.front();
		q.pop();

		if (state.flips >= numPancakes - flipperSize + 1)
		{
			return -1;
		}

		for (int i = state.lastFlip + 1; i <= numPancakes - flipperSize; i++)
		{
			pancakeState newState(state);
			newState.lastFlip = i;
			newState.flip(i, flipperSize);

			//cout << newState.state << " " << newState.state.count() << " " << newState.flips << endl;

			if (newState.state.count() == numPancakes)
			{
				return newState.flips;
			}

			q.push(newState);
		}
	}

	return -1;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		string s;
		int K;

		cin >> s;
		cin >> K;

		replace(s.begin(), s.end(), '-', '0');
		replace(s.begin(), s.end(), '+', '1');

		int N = s.size();

		pancakeState ps;
		ps.state = bitset<MAXPANCACKES>(s);
		ps.flips = 0;
		
		int res = flipsDemPancackesBoy(ps, K, N);

		if (res >= 0)
		{
			cout << "Case #" << i + 1 << ": " << res << endl;
		}
		else
		{
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		}

	}
}