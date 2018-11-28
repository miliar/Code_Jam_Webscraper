#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		long long int d;
		int n;
		cin >> d >> n;
		float x = 0.0;
		for (int j = 0; j < n; j++)
		{
			long long int dest;
			long int speed;
			cin >> dest >> speed;
			float y = (float)(d-dest)/(float)speed;
			if (x < y)
				x = y;
		}
		//cout << d << " " << x << endl;
		cout << "Case #" << i << ": ";
		//double z = ;
		double y = (double)d/(double)x;
		printf("%.06f\n",y);
		//cout << y << endl;
		
	}
}
