#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	ifstream cin("A-large.in", ifstream::in);
	ofstream cout("A-large.out", ofstream::out);
	
	int x, T;
	double tmax, tcurrent;
	int i, N, D;
	int Ki, Si;
	cin >> T;
	for(x = 1; x <= T; x++)
	{
		cin >> D >> N;
		tmax = 0;
		for(i = 0; i < N; i++)
		{
			cin >> Ki >> Si;
			tcurrent = (D-Ki)/(float)Si;
			if(tcurrent > tmax)
			{
				tmax = tcurrent;
			}
		}
		cout << "Case #" << x << ": ";
		cout << fixed << setprecision(6) << D/tmax << endl;
	}
	return 0;
}