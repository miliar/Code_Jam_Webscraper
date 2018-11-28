#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() 
{

	int T;
	cin >> T;

	for(int t=1;t<=T;t++) 
	{
		int flipped = 0;

		//input
		string tmpS;
		int K;
		cin >> tmpS;
		cin >> K;
		vector<char> S(tmpS.begin(), tmpS.end());

		//processing
		int lenS = S.size();
		for(int i=0; i<lenS; i++)
		{
			if(S[i] == '+')
			{
				continue;
			}

			flipped++;

			for(int j=i; j<(i+K); j++)
			{
				if(j >= lenS)
				{
					flipped = -1;
					break;
				}

				if(S[j] == '+')
				{
					S[j] = '-';
				}
				else 
				{
					S[j] = '+';
				}
			}

			if(flipped < 0)
			{
				break;
			}
		}

		cout << "Case #" << t << ": ";
		if(flipped < 0)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << flipped;
		}
		cout << endl;

	}

	return 0;
}
