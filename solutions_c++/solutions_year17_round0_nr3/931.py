#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("a.out");

long long Q[10000000];
long long c[10000000];
int l = 1, r = 0;

void Add(long long ct, long long n)
{
//	cout  << ct<<" "<<n<<endl;
	for(int i = l; i <= r; i++)
	if(Q[i] == n)
	{
		c[i] += ct;
		return;
	}
	r++;
	Q[r] = n;
	c[r] = ct;
}

long long slv(long long n, long long k)
{
	l = 1;
	r = 0;
	Q[++r] = n;
	c[r] = 1;
	long long rem = k;
	while(rem > 0)
	{
		rem -= c[l];
		
		Add(c[l], Q[l] - 1 - (Q[l] - 1) / 2);
		Add(c[l], (Q[l] - 1) / 2);
		l++;
	}
	return Q[l - 1];
}

int main()
{
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		long long n, k;
		cin >> n >> k;
		long long ans = slv(n, k);
		cout << "Case #" << i << ": " << ans - 1 - (ans - 1) / 2 << " " << (ans - 1) / 2 << endl;
	}
	
	
	
	return 0;
}

