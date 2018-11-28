#include <iostream>
#include <vector>

bool issorted(long long n)
{
	long long d,oldd;
	d = n%10;
	oldd = d;
	for(long long i=10; i<1e20; i*=10)
	{
		if( n%i == n) break;
		d = (n%(10*i) - n%i)/i;
		if(d > oldd) return false;
		oldd = d;
	}
	return true;
}

long long get_power(long long n)
{
	long long i = 10;
	long long d,oldd;
	d = n%10;
	oldd = d;
	for(i=10; i<1e20; i*=10)
	{
		if( n%i == n) break;
		d = (n%(10*i) - n%i)/i;
		if(d > oldd) return i;
		oldd = d;
	}
	return i;	
}

long long get_sorted(long long n)
{
	long long p = get_power(n);
	long long res = n - n%(p/10)-1;
	if(issorted(res)) return res;
	else get_sorted(res);
}

int main()
{
	int t;
	long long d,temp;
	
	std::cin >>	t;
	
	std::vector<long long> N;
	
	while(std::cin >> d) 
	{
		N.push_back(d);
	}
	
	for(int k=1; k<N.size()+1; k++)
	{
		long long res = 0;
		if(issorted(N[k-1])) res = N[k-1];
		else res = get_sorted(N[k-1]);
		std::cout << "Case #" << k << ": " << res << std::endl;		
	}

	return 0;
}