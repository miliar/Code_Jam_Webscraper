#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	int N;
	double D;
	cin>>T;

	for(int tc=1;tc<=T;tc++)
	{
		cout<<"Case #"<<tc<<": ";
		cin>>D>>N;

		double maxS = 100000000000.0;
		double maxTime = 0;
		double times[1001];
		double d1, v1;

		for(int i=0;i<N;i++)
		{
			int s;
			int x;
			cin>>x>>s;
			if(i==0)
			{
				d1 = x;
				v1 = s;
			}
			times[i] = (double(D-x))/s;

			if(times[i] > maxTime)
			{
				maxTime = times[i];
			}
		}

		maxS = D/maxTime;

		printf("%.6f\n", maxS);
	}

	return 0;
}