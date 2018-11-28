#include <bits/stdc++.h>

using namespace std;

void query(long long n, long long k)
{
	long long min;
	long long max;
	map<long long,long long> range;
	range[n]=1;
	while (k>0)
	{
		auto current=prev(range.end());
		long long len=(*current).first;
		long long count=(*current).second;
		range.erase(current);
		
		if (len & 1)
		{
			range[len/2]+= count*2;			
			k-=count;
			max=len/2;
			min=len/2;
		} else
		{
			range[len/2]+= count;			
			range[(len/2)-1]+= count;			
			k-=count;
			max=len/2;
			min=(len/2)-1;
		}
		
	}
	cout << max << " " << min;
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i=0;i<t;i++) 
	{
		long long n;
		long long k;
		cin >> n >> k;		
		cout << "Case #" << i+1 << ": ";
		query(n,k);
		cout << endl;
	}
}