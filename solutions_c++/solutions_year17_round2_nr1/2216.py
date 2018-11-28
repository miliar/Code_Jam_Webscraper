#include <math.h>
#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;

	int d,n;
	int k,s;
	double time=0;

	for(int j=0; j<t; ++j)
	{
		cin >> d >> n;

		time=0;
		for(int i=0; i<n; ++i)
		{
			cin >> k >> s;
			time=max(time,(double)(d-k)/s);
		}
		cout << "Case #" << j+1 << ": " << fixed << setprecision(6) << (double)d/time << endl;
	}

	
	return 0;
}
