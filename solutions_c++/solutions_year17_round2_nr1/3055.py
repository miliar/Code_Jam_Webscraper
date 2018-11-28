#include "stdafx.h"
#include "iostream"
#include "string"
using namespace std;


int main()
{
	int T;

	cin >> T;
	cout.precision(9);
	cout.fixed;
	cout.floatfield;

	for (int Tl = 1; Tl <= T; ++Tl) {
		double D;
		int N;
		double Ih, Sh; // Start postion and speed for a hosre (these are integers but answre requires floating point calc.

		double Th ; // worst time
		double TWorst = 0;

		cin >> D >> N;
		
		for (int Ni = 0; Ni < N; ++Ni) {
			cin >> Ih >> Sh;
			Th = (D - Ih) / Sh;
			if (Th > TWorst) TWorst = Th;
		}
// Having calulated worst horse can no work out shortest time for Annes horse

		cout << "Case #" << Tl << ": ";
		cout <<  D/TWorst;
		cout << endl;
	}
	return 0;
}
