#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int Ntests;
	cin >> Ntests;

	for ( int Ntest = 0; Ntest < Ntests; ++Ntest )
	{
		int D, N;
		cin >> D >> N;
		double tmax = 0;
		for ( int i = 0; i < N; ++i )
		{
			int K, S;
			cin >> K >> S;
			const double ti = (double(D-K))/S;
			if ( ti > tmax )
				tmax = ti;
		}

		double speed = double(D) / tmax;
		cout << setprecision( 16 ) << "Case #" << Ntest+1 << ": " << speed << endl;
	}

	return 0;
}

