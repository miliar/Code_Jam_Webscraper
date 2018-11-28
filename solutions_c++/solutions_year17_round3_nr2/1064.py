#include <iostream>
#include <algorithm>

using namespace std;

struct Data
{
	int value;
	int start;

	bool operator<(Data other) const
	{
		return value < other.value;
	}

	bool operator>(Data other) const
	{
		return value > other.value;
	}

};

void doWork()
{
	int Ac, Aj;
	cin >> Ac;
	cin >> Aj;

	int activ[10000] = { 0 };
	bool activJ[10000] = { false };
	bool activC[10000] = { false };

	for (int n = 0; n < Ac; ++n)
	{
		int s, e;
		cin >> s;
		cin >> e;

		for (int c = s; c < e; ++c)
		{
			activ[c] = 1;
			activC[c] = true;
		}
	}

	for (int n = 0; n < Aj; ++n)
	{
		int s, e;
		cin >> s;
		cin >> e;

		for (int c = s; c < e; ++c)
		{
			activ[c] = 2;
			activJ[c] = true;
		}
	}

	Data dp[2000][3][1000];

	for (int n = 0; n < 1000; ++n)
	{
		dp[0][1][n].value = -1;
		dp[0][2][n].value = -1;
	}

	dp[0][1][0].value = activ[0] != 1 ? 0 : -1;
	dp[0][2][0].value = activ[0] != 2 ? 0 : -1;

	dp[0][1][0].start = 1;
	dp[0][2][0].start = 2;

	for (int time = 1; time <= 1440; ++time)
	{
		for (int role = 1; role <= 2; ++role)
		{
			for (int perc = 0; perc <= 720; ++perc)
			{
				if (activ[time] == role)
				{
					dp[time][role][perc].value = -1;
				}
				else
				{
					//czy mozemy zmienic role
					if (dp[time - 1][role == 1 ? 2 : 1][role == 1 ? perc - 1 : perc].value >= 0)
					{
						Data change = dp[time - 1][role == 1 ? 2 : 1][role == 1 ? perc - 1 : perc];
						change.value += 1;

						//czy mozemy nie zmieniac rol
						if (dp[time - 1][role][role == 1 ? perc - 1 : perc].value >= 0)
						{
							Data noChange = dp[time - 1][role][role == 1 ? perc - 1 : perc];
							if (noChange.value == change.value)
							{
								dp[time][role][perc] = noChange.start == role ? noChange : change;
							}
							else
							{
								dp[time][role][perc] = min(change, noChange);
							}
						}
						else
						{
							dp[time][role][perc] = change;
						}
					}
					else
					{
						//czy mozemy nie zmieniac rol
						if (dp[time - 1][role][role == 1 ? perc - 1 : perc].value >= 0)
						{
							Data noChange = dp[time - 1][role][role == 1 ? perc - 1 : perc];
							dp[time][role][perc] = noChange;
						}
						else
						{
							dp[time][role][perc].value = -1;
						}
					}
				}
			}
		}
	}

	Data a = dp[1440][1][720];
	if (a.value >= 0)
	{
		if (a.start != 1)
		{
			a.value += 1;
		}
	}

	Data b = dp[1440][2][720];
	if (b.value >= 0)
	{
		if (b.start != 2)
		{
			b.value += 1;
		}
	}

	if (a.value < 0)
	{
		cout << b.value << endl;
	}
	else if (b.value < 0)
	{
		cout << a.value << endl;
	}
	else
	{
		//cout << "a: " << a.value << ", b: " << b.value << endl;
		cout << min(a.value, b.value) << endl;
	}
}

void main()
{
	int cases;
	cin >> cases;

	for (int k = 1; k <= cases; ++k)
	{
		cout << "Case #" << k << ": ";
		doWork();
	}

	//system("pause");
}