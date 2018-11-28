#include <string>
#include <math.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <queue>

using namespace std;
typedef long long int lli;

#define pb push_back

vector < vector<int> >grid;


int main(int argc, char* argv[])
{
	string directory = "d:\\Google Drive\\versenyek";


	if (argc > 1)
	{
		freopen((directory + "\\be.txt").c_str(), "rt", stdin);
		freopen((directory + "\\ki.txt").c_str(), "wt", stdout);
	}

	int N,TT,t,D;

	cin >> TT;
	t = TT;

	char good = '+', bad = '-';
	
	while (TT--)
	{
		string pancakes;

		cin >> pancakes >> N;
		bool impossible = false;

		int flips = 0;

		for (size_t i = 0; i < pancakes.size(); i++)
		{
			if (pancakes[i] == bad)
			{
				if (pancakes.size() - i < N)
				{
					impossible = true;
					break;
				}

				for (size_t j = 0; j < N; j++)
				{
					if (pancakes[i + j] == good)
						pancakes[i + j] = bad;
					else
						pancakes[i + j] = good;
				}

				flips++;
			}

		}
		
		
		if (impossible)
			cout << "Case #" << t - TT << ": " <<"IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t - TT << ": " << flips <<endl;
	}


	return 0;

}
