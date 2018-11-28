#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{ 
	ifstream fp(".\\A-large.in");
	ofstream fpo(".\\A-large.out");

	int T;
	double D, N;
	double K, S;
	double est, maxEst = 0.0f;
	fp >> T;

	for (int i = 0; i < T; ++i)
	{
		fp >> D >> N;		
		maxEst = 0.0;
		for (int j = 0; j < N; ++j)
		{ 
			fp >> K >> S;
			est = (D - K) / S;
			maxEst = maxEst < est ? est : maxEst;

		}


		fpo << "Case #" << i + 1 << ": ";
		fpo << fixed;
		fpo.precision(6);
		fpo << D / maxEst << endl;
	}
	fp.close();
	fpo.close();
}