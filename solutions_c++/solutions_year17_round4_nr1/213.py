
#pragma comment(linker, "/STACK:256000000")

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <functional>
#include <vector>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <bitset>
#include <list>
#include <iomanip>      // std::setprecision
#include <random>

typedef std::mt19937 rng_type;
std::uniform_int_distribution<rng_type::result_type> udist(0, 1);

rng_type rng;

using namespace std;

FILE * in, *out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

#define LL long long

int ri() { int a; fscanf(in, "%d", &a); return a; }
double rf() { double a; fscanf(in, "%lf", &a); return a; }
char sbuf[100005];
string rstr()
{
	//fscanf(in, "%lf", sbuf); 
	char c;
	char * b = sbuf;
	while(c = fgetc(in))
	{
		if(c == '\n' || c == 255) break;
		*b++ = c;
	}
	*b = 0;
	return sbuf;
}


long long nod(long long a, long long b)
{
	if(a == 1 || b == 1) return 1;
	if(a == 0) return b;
	if(b == 0) return a;

	return nod(b%a, a);
}

vector<int> primes;
void calculatePrimes()
{
	primes.push_back(2);
	for(int i = 3; i < 100000; i += 2)
	{
		bool bFound = false;
		int m = (int)sqrt((float)i);
		for(int j = 1; j < primes.size() && !bFound && primes[j] <= m; j++)
			bFound = ((i%primes[j]) == 0);
		if(!bFound)
			primes.push_back(i);
	}
}

bool isPrime(int p)
{
	for(int i : primes)
		if(p != i && (p%i) == 0) return false;
	return true;
}


//	std::cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
//	std::cout.precision(7);


void egcd(int a, int b, int &g, int &x, int &y)
{
	if(a == 0)
	{
		g = b;
		x = 0;
		y = 1;
		return;
	}
	egcd(b%a, a, g, y, x);
	x = x - (b / a)*y;
}

int modinv(int a, int m)
{
	int g = 0, x = 0, y = 0;
	egcd(a, m, g, x, y);
	return (x+m)%m;
}

long long modpow(int a, long long n, int p)
{
	long long res = 1;
	long long curp = (a%p);
	while(n)
	{
		if(n&1)
		{
			res = (res*curp)%p;
		}
		curp = (curp*curp)%p;
		n /= 2;
	}
	return res;
}

#define MODP 1000000007

int main()
{
	int T;
	cin >> T;
	for(int cs = 1; cs <= T; cs++)
	{
		int n, p;
		cin >> n >> p;

		int ng = 0;
		int no[4] ={0,0,0,0};
		fi(n)
		{
			int co;
			cin >> co;
			co = co % p;
			no[co]++;
		}

		ng += no[0];

		for(int i = 1; i<p; i++)
		{
			int j = p-i;
			while(no[i] && no[j])
			{
				ng++;
				no[i]--;
				no[j]--;
				if(no[i] < 0 || no[j] < 0)
				{
					ng--;
					no[i]++;
					no[j]++;
					break;
				}
			}
		}

		for(int i = 1; i<p; i++)
		for(int k = 1; k<p; k++)
		{
			int j = (2*p-i-k)%p;
			while(no[i] && no[j] && no[k])
			{
				ng++;
				no[i]--;
				no[j]--;
				no[k]--;
				if(no[i] < 0 || no[j] < 0 || no[k] < 0)
				{
					ng--;
					no[i]++;
					no[j]++;
					no[k]++;
					break;
				}
			}
		}
		for(int i = 1; i<p; i++)
			for(int l = 1; l<p; l++)
				for(int k = 1; k<p; k++)
			{
				int j = (3*p-i-k-l)%p;
				while(no[i] && no[j] && no[k] && no[l])
				{
					ng++;
					no[i]--;
					no[j]--;
					no[k]--;
					no[l]--;
					if(no[i] < 0 || no[j] < 0 || no[k] < 0|| no[l] < 0)
					{
						ng--;
						no[i]++;
						no[j]++;
						no[k]++;
						no[l]++;
						break;
					}
				}
			}

		for(int i = 1; i<p; i++)
			if(no[i])
			{
				ng++;
				break;
			}

		cout << "Case #" << cs << ": " << ng << endl;
	}
	return 0;
}