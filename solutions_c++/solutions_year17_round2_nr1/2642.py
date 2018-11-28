#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >>  t;
	for(int l=1;l<=t;l++)
	{
		long  long n,d;
		cin >> d  >> n;
		double max=0;
		for(int i=0;i<n;i++)
		{
			long long k,s;
			cin >> k >> s;
			double dis;
			k=d-k;
			dis=double(k)/double(s);
			if(max<dis)
				max=dis;
		}
		double res;
		res = double(d)/double(max);
		printf("Case #%d: %.6lf\n",l,res);
	}
	return 0;
}
