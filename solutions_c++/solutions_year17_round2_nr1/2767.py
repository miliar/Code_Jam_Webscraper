#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	int Case = 1;
	while( t--)
	{
		int d, n;
		cin >> d >> n;
		double at = 0;
		for( int i = 0; i < n; i++)
		{
			int k, s;
			cin >> k >> s;
			double t = double(d-k)/double(s);
			if( t > at)
				at = t;
		}
		printf( "Case #%d: %.6f\n", Case++, double(d)/at);
		// cout << "Case #" << Case << ": " << 
	}
	return 0;
}