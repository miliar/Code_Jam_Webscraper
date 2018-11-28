#define pi 3.141592653589793238L
#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;

//const long double pi 3.141592653589793238;
//3.141592653589793

struct data
{
	long long int r;
	long long int h;
};

bool compare(data x, data y)
{
	long long int u = x.r*x.h;
	long long int z = y.r*y.h;
	if (u!=z)
		return u > z;
	else
		x.r > y.r;
}

long long int max(data array[], int start, int end)
{
	long long int r = array[0].r;
	for (int j = 1; j < end; j++)
		if (array[j].r > r)
			r = array[j].r;
	return r;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i<=t; i++)
	{
		
		cout << "Case #" << i << ": " ;
		int k, n;
		cin >> n >> k;
		data array[n];
		data d;
		for (int j = 0; j < n; j++)
		{
			cin >> d.r >> d.h;
			array[j] = d;			
		}
		
		sort(array, array+n, compare);
		long long int r = max(array, 0, k);
	 double res =  pi*r*r;
		for (int re = 0; re < k; re++)
			res += 2*pi*array[re].h*array[re].r;
		
		double res1 = (res-2*pi*array[k-1].h*array[k-1].r)-(pi*r*r);
		for (int  j = 0; j < n; j++)
		{
			if (array[j].r > r)
			{
				double yu = pi*array[j].r*array[j].r;
				double yi = 2*pi*array[j].r*array[j].h;
				res = max(res, res1+yu+yi);
			}
		}
		
		
		
		//	cout << res << endl;
		printf("%.10lf\n", res);
	}
}
