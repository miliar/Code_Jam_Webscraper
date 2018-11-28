#include<iostream>
#include<string>

using namespace std;

int S[1000], K[1000];

double Solve(int d,int n)
{
	double maxt = 0;
	for (int i = 0; i < n; i++)
	{
		double t = (d - K[i]) / (double)S[i];
		if (t > maxt) maxt = t;
	}
	return d / maxt;
}

int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++)
	{
		int D, N;
		cin >> D >> N;
		for (int i = 0; i < N; i++) cin >> K[i] >> S[i];
		printf("Case #%d: %.6f\n", c, Solve(D, N));
	}
	return 0;
}

