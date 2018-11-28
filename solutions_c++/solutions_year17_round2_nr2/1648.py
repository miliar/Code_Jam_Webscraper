/*
ID: paradoxes
PROG: Stable Neigh-bors
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>

using namespace std;

int T;

int N;

int R, O, Y, G, B, V;

char getmax()
{
	int maxia = max(max(R, B), Y);

	if (maxia == R)
		return 'R';
	if (maxia == B)
		return 'B';
	if (maxia == Y)
		return 'Y';

	else
	{
		cerr << "Error 1" << endl;
		getchar();
		getchar();
	}


}

void deinc(char prev)
{
	switch (prev)
	{
	case 'R':
		R--;
		break;
	case 'B':
		B--;
		break;
	case 'Y':
		Y--;
		break;
	}
}

char nextR(char prev)
{
	switch (prev)
	{
	case 'R':
	{
		if (B >= Y)
			return 'B';
		else
			return 'Y';
		break;
	}
	case 'B':
	{
		if (R >= Y)
			return 'R';
		else
			return 'Y';
		break;
	}
	case 'Y':
	{
		if (R >= B)
			return 'R';
		else
			return 'B';
		break;
	}
	}
}

char nextB(char prev)
{
	switch (prev)
	{
	case 'R':
	{
		if (B >= Y)
			return 'B';
		else
			return 'Y';
		break;
	}
	case 'B':
	{
		if (R >= Y)
			return 'R';
		else
			return 'Y';
		break;
	}
	case 'Y':
	{
		if (R > B)
			return 'R';
		else
			return 'B';
		break;
	}
	}
}

char nextY(char prev)
{
	switch (prev)
	{
	case 'R':
	{
		if (B > Y)
			return 'B';
		else
			return 'Y';
		break;
	}
	case 'B':
	{
		if (R > Y)
			return 'R';
		else
			return 'Y';
		break;
	}
	case 'Y':
	{
		if (R >= B)
			return 'R';
		else
			return 'B';
		break;
	}
	}
}

int main()
{
	ifstream Input("Q.in");
	ofstream Output("Q.out");

	Input >> T;

	string answer;

	for (int j = 1; j <= T; j++)
	{
		Input >> N >> R >> O >> Y >> G >> B >> V;

		if (2 * R > N)
		{
			Output << "Case #" << j << ": IMPOSSIBLE" << endl;
			continue;
		}
		if (2 * Y > N)
		{
			Output << "Case #" << j << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		if (2 * B > N)
		{
			Output << "Case #" << j << ": " << "IMPOSSIBLE" << endl;
			continue;
		}

		answer = "";

		char prev = getmax();
		answer += prev;
		deinc(prev);

		if (prev == 'R')
		{
			for (int i = 1; i < N; i++)
			{
				prev = nextR(prev);
				answer += prev;
				deinc(prev);

			}
		}

		else if (prev == 'B')
		{
			{
				for (int i = 1; i < N; i++)
				{
					prev = nextB(prev);
					answer += prev;
					deinc(prev);

				}
			}
		}

		else if (prev == 'Y')
		{
			{
				for (int i = 1; i < N; i++)
				{
					prev = nextY(prev);
					answer += prev;
					deinc(prev);

				}
			}
		}

		Output << "Case #" << j << ": " << answer << endl;
	}

	return 0;
}