// Google Code Jam 2017, Round 2 - problem A
// "Fresh Chocolate"
// Andras Eles, Veszprem, Hungary, 2017.05.13.

#include <cstring>
#include <iostream>
using namespace std;

typedef unsigned int uint;

void solveProblem (void)
{
	uint N, P;
	cin >> N >> P;
	uint* mgr = new uint [101*101*101];
	memset(mgr,0,sizeof(uint)*101*101*101);
	for (uint m1=0;m1<=100;m1++)
	{
		for (uint m2=0;m2<=((P > 2) ? 100 : 0);m2++)
		{
			for (uint m3=0;m3<=((P > 3) ? 100 : 0);m3++)
			{
				if (P == 2)
				{
					mgr[m1] = m1 >> 1;
				}
				else if (P == 3)
				{
					uint opt = 0;
					if (m1 >= 3 && m2 >= 0 && opt < 1 + mgr[(m1 - 3) + (m2 - 0) * 101])
					{
						opt = 1 + mgr[(m1 - 3) + (m2 - 0) * 101];
					}
					if (m1 >= 0 && m2 >= 3 && opt < 1 + mgr[(m1 - 0) + (m2 - 3) * 101])
					{
						opt = 1 + mgr[(m1 - 0) + (m2 - 3) * 101];
					}
					if (m1 >= 1 && m2 >= 1 && opt < 1 + mgr[(m1 - 1) + (m2 - 1) * 101])
					{
						opt = 1 + mgr[(m1 - 1) + (m2 - 1) * 101];
					}
					mgr[m1 + m2 * 101] = opt;
				}
				else
				{
					uint opt = 0;
					uint m1c[] = {4,0,0,1,2,0};
					uint m2c[] = {0,2,0,0,1,1};
					uint m3c[] = {0,0,4,1,0,2};
					for (uint k=0;k<6;k++)
					{
						if (m1 >= m1c[k] && m2 >= m2c[k] && m3 >= m3c[k] &&
								opt < 1 + mgr[(m1 - m1c[k]) + (m2 - m2c[k]) * 101 + (m3 - m3c[k]) * 101 * 101])
						{
							opt = 1 + mgr[(m1 - m1c[k]) + (m2 - m2c[k]) * 101 + (m3 - m3c[k]) * 101 * 101];
						}
					}
					mgr[m1 + m2 * 101 + m3 * 101 * 101] = opt;
				}
			}
		}
	}
	uint gm[4];
	gm[0] = gm[1] = gm[2] = gm[3] = 0;
	for (uint i=0;i<N;i++)
	{
		uint G;
		cin >> G;
		gm[G % P]++;
	}
	uint opt = mgr[gm[1] + gm[2] * 101 + gm[3] * 101 * 101];
	for (uint m1=0;m1<P && m1<=gm[1];m1++)
	{
		for (uint m2=0;m2<=((P > 2) ? 100 : 0)&&m2 < P&&m2<=gm[2];m2++)
		{
			for (uint m3=0;m3<=((P > 3) ? 100 : 0)&&m3 < P&&m3<=gm[3];m3++)
			{
				if (m1 + m2 + m3 > 0 && opt < 1 + mgr[(gm[1] - m1) + (gm[2] - m2) * 101 + (gm[3] - m3) * 101 * 101])
				{
					opt = 1 + mgr[(gm[1] - m1) + (gm[2] - m2) * 101 + (gm[3] - m3) * 101 * 101];
				}
			}
		}
	}
	opt += gm[0];
	cout << opt << endl;
	delete [] mgr;
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
