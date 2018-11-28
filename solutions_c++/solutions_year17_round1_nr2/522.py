// Google Code Jam 2017, Round 1A - problem B
// "Ratatouille"
// Andras Eles, Veszprem, Hungary, 2017.04.15.

#include <iostream>
using namespace std;

typedef unsigned long long int uint;

void solveProblem (void)
{
	uint N, P;
	uint R[50];
	uint Q[50][50];
	bool in[50][50];
	cin >> N >> P;
	for (uint i=0;i<N;i++)
	{
		cin >> R[i];
	}
	for (uint i=0;i<N;i++)
	{
		for (uint j=0;j<P;j++)
		{
			cin >> Q[i][j];
			in[i][j] = true;
		}
	}
	uint solution = 0;
	{
		uint left = P * N;
		while (left >= N)
		{
			// min find
			uint ifound = N, jfound = P;
			for (uint i=0;i<N;i++)
			{
				for (uint j=0;j<P;j++)
				{
					if (in[i][j])
					{
						if (ifound == N)
						{
							ifound = i;
							jfound = j;
						}
						else
						{
							if (Q[i][j] * R[ifound] < Q[ifound][jfound] * R[i])
							{
								ifound = i;
								jfound = j;
							}
						}
					}
				}
			}
			//cout << "<" << ifound << "," << jfound << ">" << Q[ifound][jfound] << " / " << R[ifound] << endl;
			// min of all ingrs
			uint jf2 [50];
			uint minpack [50];
			uint maxpack [50];
			for (uint i=0;i<N;i++)
			{
				jf2[i] = P;
				for (uint j=0;j<P;j++)
				{
					if (in[i][j])
					{
						if (jf2[i] == P)
						{
							jf2[i] = j;
						}
						else
						{
							if (Q[i][j] < Q[i][jf2[i]])
							{
								jf2[i] = j;
							}
						}
					}
				}
				if (jf2[i] == P)
				{
					break;
				}
				minpack[i] = (10 * Q[i][jf2[i]]) / (11 * R[i]);
				if ((10 * Q[i][jf2[i]]) % (11 * R[i]))
				{
					minpack[i]++;
				}
				maxpack[i] = (10 * Q[i][jf2[i]]) / (9 * R[i]);
				//cout << "ingr " << i << " " << Q[i][jf2[i]] << "," << R[i] << " -- " << minpack[i] << " " << maxpack[i] << endl;
			}
			// checking packability
			uint maxofmin = minpack[0];
			uint minofmax = maxpack[0];
			for (uint i=1;i<N;i++)
			{
				if (maxofmin < minpack[i])
				{
					maxofmin = minpack[i];
				}
				if (minofmax > maxpack[i])
				{
					minofmax = maxpack[i];
				}
			}
			//cout << "maxofmin=" << maxofmin << " *** minofmax=" << minofmax << endl;
			if (minofmax < maxofmin)
			{
				//cout << "FAIL" << endl;
				in[ifound][jfound] = false;
				left--;
			}
			else
			{
				//cout << "PASS" << endl;
				solution++;
				for (uint i=0;i<N;i++)
				{
					in[i][jf2[i]] = false;
				}
				left -= N;
			}
			//cout << "LEFT=" << left << " " << P << endl;
		}
	}
	cout << solution << endl;
}

int main (int argc, char** argv)
{
	int T;
	cin >> T;
	for (int t=1;t<=T;t++)
	{
		cout << "Case #" << t << ": " << flush;
		solveProblem();
	}
	return 0;
}
