#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int T;
	int D,N;
	double time;
	int Dj,sj;
	double tmp;
	double s;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		time = -1;
		cin >> D >> N;
		for(int j=0;j<N;j++)
		{
			cin >> Dj >> sj;
			tmp = (double)(D-Dj)/(double)sj;
			if(tmp > time)
			{
				time = tmp;
			}
		}
		s = D/time;
		cout << "Case #" << i << ": ";
		printf("%.6f\n",s);
	}
	return 0;
}
