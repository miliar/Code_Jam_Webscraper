#include<bits/stdc++.h>

using namespace std;

long long  f(long long n, long long k)
{
	int q = 1;
	while( (1ll << q) - 1  <  k )
		q++;
	long long x = (n - k + (1ll << (q-1)) ) / (1ll << (q - 1)) ;
	return x;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
	
	                              
		long long n, k;
		cin >> n >> k;	
       	long long x = f(n, k);
		cout << "Case #" << i << ": " <<  x / 2 << " " << (x - 1) / 2  << "\n";
	}
}