#include <iostream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main() {

	int t;
	cin>>t;
	for (int i1 = 1; i1<= t; ++i1) 
	{
		long int d,n;
		cin >> d;
		cin >>n;

		long int *k = new long int[n];
		long int *s = new long int[n];
		for (int i = 0; i < n; ++i)
		{
			cin>>k[i];
			cin>>s[i];
			/* code */
		}


		if (n == 1)
		{
			double value = 1.0*(d*s[0])/(d-k[0]);
			cout <<"Case #"<<i1<<": ";
			printf("%0.6lf\n",value);//<<endl;

		}
		else if (n == 2)
		{ 
			long int k0;
			long int k1;
			long int s0;
			long int s1;
			if (k[0] > k[1]) 
			{	
				k0 = k[1];
				k1 = k[0];

				s0 = s[1];
				s1 = s[0];

			} else {
				k0 = k[0];
				k1 = k[1];

				s0 = s[0];
				s1 = s[1];

			}

				long int d1 = k1 - k0;
				if (s0 > s1) 
				 {
				 	double time = 1.0*d1/(s0 - s1);
				 	if ((time*s1) >= (d - k1))
				 	{
						double value = 1.0*(d*s0)/(d-k0);
						cout <<"Case #"<<i1<<": ";
						printf("%0.6lf\n",value);
				 	}
				 	else {
				 		double r = 1.0*d - k1 - (time*s1);
				 		time += 1.0*r/s1;
				 		double value = 1.0*d/time;
						cout <<"Case #"<<i1<<": ";
						printf("%0.6lf\n",value);

				 	}
				 } 

				 else {
				 	double value = 1.0*(d*s0)/(d-k0);
					cout <<"Case #"<<i1<<": ";
					printf("%0.6lf\n",value);//<<endl;

				 }
			}

		}

	return 0;
}
