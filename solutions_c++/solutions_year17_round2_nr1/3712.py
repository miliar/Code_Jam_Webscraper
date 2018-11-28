#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

int main(int argc, char const *argv[])
{
	
	long int T,numOfHorse;
	double D;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		long double max = 0;
		cin >> D >> numOfHorse;
		vector<long double> v;
		long double t1,t2;

		for (int j = 0; j < numOfHorse; ++j)
		{
			cin >> t1 >> t2;

			v.push_back((D-t1)/t2);
		}
		for (int k = 0; k < numOfHorse; ++k)
		{
			if (v[k] > max)
			{
				max = v[k];
			}
		}
		v.clear();
		long double res = D/max;
		printf("Case #%d: %Lf\n",i+1,res );
	}
	return 0;
}