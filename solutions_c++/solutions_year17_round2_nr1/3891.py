#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int test=1;test<=t;test++)
	{
		double d ;
		int n;
		cin >> d >> n;
		double k[n] , s[n];
		double res[n];
		for(int i=0;i<n;i++)
		{
			cin >> k[i] >> s[i];
			res[i] = (d-k[i])/s[i];
		}
/*		cout << "------" << endl;
		for(int i=0;i<n;i++)
		{
			cout << res[i] << endl;
		}
		cout << "-----" << endl;*/
		long double max=0;
		for(int i=0;i<n;i++)
		{
			if(res[i] >= max)
				max = res[i];
		}
		
		cout << "Case #" << test << ": ";
		printf("%lf\n",(double)(d/max));
		
	}	
		
	return 0;
}
