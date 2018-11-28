#include <iostream>
#include <map>
#include <math.h>

using namespace std;

struct baze
{
	long long unsigned int a;
	long long unsigned int b;  
};

int main()
{
	int t;
	cin >> t;
	int Case = 1;
	while( t--)
	{
		long long unsigned int n ,k, l, r;
		cin >> n >> k;
		multimap<long long unsigned int, baze> mp;
		baze b;
		b.a = 1;
		b.b = n;
		mp.insert(pair<long long unsigned int, baze>(n, b));
		for( long long unsigned int i = 0; i < k; i++)
		{
			multimap<long long unsigned int, baze>::iterator it = mp.end();
			it--;
			baze selected = it->second;
			long long unsigned int v = it->first-1;
			mp.erase( it);
			b.a = selected.a;
			b.b = floor( (v)/2)+selected.a;
			mp.insert(pair<long long unsigned int, baze>(floor( double(v)/2.0), b));
			b.a = floor( (v)/2)+selected.a;
			b.b = selected.b;
			mp.insert(pair<long long unsigned int, baze>(ceil( double(v)/2.0), b));
			l = max( floor( double(v)/2.0), ceil( double(v)/2.0));
			r = min( floor( double(v)/2.0), ceil( double(v)/2.0));
		}

		cout << "Case #" << Case++ << ": " << l << " " << r << endl ;
	}
	return 0;
}