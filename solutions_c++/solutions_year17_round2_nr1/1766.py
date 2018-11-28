#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");

	out.setf(ios::fixed);
	out.precision(6);

	int T;
	in >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		int N;
		double D;
		double K[1001];
		double S[1001];
		in >> D >> N;
		for (int i = 0; i < N; i++)
			in >> K[i] >> S[i];

		double max = (D - K[0]) / S[0];
		for (int i = 1; i < N; i++)
		{
			if (max < (D - K[i]) / S[i])
				max = (D - K[i]) / S[i];
		}
		out << "Case #" << Case << ": " << D / max << endl;
	}

	return 0;
}