
#if 1
#define _CRT_SECURE_NO_WARNINGS
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int T, N;





void PanCake()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		string sample, sampleTmp;
		cin >> sampleTmp;
		sample = "0" + sampleTmp;
		N = sample.size();
		for (int i = N - 1; i >= 1; i--)
		{
			if (sample[i - 1] > sample[i])
			{
				sample[i - 1]--;
				for (int k = i; k < N; k++)
					sample[k] = '9';
			}
		}
		cout << "Case #" << t << ": ";
		for (int i = 0; i < sample.size(); i++)
		{
			if (sample[i] != '0')
				cout << sample[i];
		}
		cout << endl;
		
	}
}

int main()
{
	PanCake();
	return 0;
}

#endif
