#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in("C-small-1-attempt2.in");
	ofstream out("output.txt");
	out << fixed;
	out.precision(10);

	int T;
	in >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		int N, K;
		in >> N >> K;
		double U;
		in >> U;
		double *P = new double[N + 1];
		for (int i = 0; i < N; i++)
			in >> P[i];
		P[N] = 1;

		sort(&P[0], &P[N]);

		for (int i = 0; i < N; i++)
		{
			if (U >= (P[i + 1] - P[i]) * (i + 1))
			{
				U -= (P[i + 1] - P[i]) * (i + 1);
				for (int j = 0; j <= i; j++)
					P[j] = P[i + 1];
			}
			else
			{
				for (int j = 0; j <= i; j++)
					P[j] = P[j] + U/(i + 1);
				break;
			}
		}

		double ret = 1;
		for (int i = 0; i < N; i++)
			ret *= P[i];

		out << "Case #" << Case << ": " << ret << endl;
	}

	return 0;
}
