#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

struct data
{
	int S;
	int i;
	char w;
};

bool cmp(struct data x, struct data y)
{
	return x.S < y.S;
}

int main()
{
	ifstream in("B-small-attempt5.in");
	ofstream out("output.txt");

	int T;
	in >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		int Ac, Aj;
		in >> Ac >> Aj;

		int Tc = 720;
		int Tj = 720;

		char Time[1442];
		for (int i = 0; i <= 1440; i++)
			Time[i] = ' ';

		int *C = new int[Ac];
		int *D = new int[Ac];
		int *J = new int[Aj];
		int *K = new int[Aj];

		for (int i = 0; i < Ac; i++)
		{
			in >> C[i] >> D[i];
			Tc -= D[i] - C[i];
			for (int t = C[i]; t < D[i]; t++)
				Time[t] = 'c';
		}

		for (int i = 0; i < Aj; i++)
		{
			in >> J[i] >> K[i];
			Tj -= K[i] - J[i];
			for (int t = J[i]; t < K[i]; t++)
				Time[t] = 'j';
		}

		struct data s[210];
		int cnt = 0;

		for (int t = 0; t < 1440; t++)
		{
			if (Time[t] == 'c' && Time[t + 1] == ' ')
			{
				int j;
				for (j = t + 1; j < 2880; j++)
				{
					if (Time[j%1440] == 'c')
					{
						s[cnt].i = t + 1;
						s[cnt].w = 'c';
						s[cnt++].S = j - t - 1;
						break;
					}
					else if (Time[j%1440] == 'j')
						break;
				}
				t = j;
			}
		}

		for (int t = 0; t < 1440; t++)
		{
			if (Time[t] == 'j' && Time[t + 1] == ' ')
			{
				int j;
				for (j = t + 1; j < 2880; j++)
				{
					if (Time[j%1440] == 'j')
					{
						s[cnt].i = t + 1;
						s[cnt].w = 'j';
						s[cnt++].S = j - t - 1;
						break;
					}
					else if (Time[j%1440] == 'c')
						break;
				}
				t = j;
			}
		}

		sort(&s[0], &s[cnt], cmp);

		for (int i = 0; i < cnt; i++)
		{
			if (s[i].w == 'c')
			{
				if (s[i].S <= Tc)
				{
					Tc -= s[i].S;

					for (int t = s[i].i; t < s[i].i + s[i].S; t++)
						Time[t % 1440] = 'c';
				}
			}
			else if(s[i].w == 'j')
			{
				if (s[i].S <= Tj)
				{
					Tj -= s[i].S;

					for (int t = s[i].i; t < s[i].i + s[i].S; t++)
						Time[t % 1440] = 'j';
				}
			}
		}

		for (int i = 0; i < 2880; i++)
		{
			if (Tc > 0 && Time[i%1440] == 'c' && Time[(i + 1)%1440] == ' ')
			{
				Time[(i + 1)%1440] = 'c';
				Tc--;
			}
			else if (Tj > 0 && Time[i%1440] == 'j' && Time[(i + 1)%1440] == ' ')
			{
				Time[(i + 1)%1440] = 'j';
				Tj--;
			}
		}

		if (Tc == 0)
		{
			for (int t = 0; t < 1440; t++)
				if (Time[t] == ' ')Time[t] = 'j';
		}
		else if (Tj == 0)
		{
			for (int t = 0; t < 1440; t++)
				if (Time[t] == ' ')Time[t] = 'c';
		}
		
		cnt = 0;
		Time[1440] = Time[0];
		for (int t = 0; t < 1440; t++)
			if (Time[t] != Time[t + 1])cnt++;

		out << "Case #" << Case << ": " << cnt << endl;
	}

	return 0;
}