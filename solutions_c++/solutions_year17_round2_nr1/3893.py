#include<stdio.h>
#include<iomanip>
#include<iostream>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	std::setprecision(5);
	for(int i=1; i<=t; i++)
	{
		double d;
		int n;
		scanf("%lf%d",&d,&n);
		//cin<<n;
		double max= 0.0;
		for(int j=1; j<=n; j++)
		{
			double k;
			double s;
			scanf("%lf%lf",&k,&s);
			//cin<<s
			double time= ((d-k)*1.0000000)/s;
			//printf("%lf",time);
			if(max<time)
				max= time;
		}
		double speed= d/max;
		printf("Case #%d: %lf\n",i,speed);
	}
	return 0;
}
