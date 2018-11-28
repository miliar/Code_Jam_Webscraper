#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	cin >>t;
	for(int x =1;x<=t;x++)
	{
		double last(0.0);
		int distance,horseCount;
		cin >> distance >>horseCount;
		while(horseCount--)
		{
			int position,speed;
			cin>>position>>speed;
			double hourToDest = ((double)(distance-position))/speed;
			if(hourToDest>last)
				last = hourToDest;
		}
		double hasil = double(distance)/last;
		
		printf("Case #%d: %.6lf",x,hasil);
	}
    return 0;
}
