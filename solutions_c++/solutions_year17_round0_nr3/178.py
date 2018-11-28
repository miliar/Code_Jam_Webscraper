
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

map<pair<long long, long long>, long long> cache;
long long get(long long n, long long k)
{
	if(k == 0) return n;

	n--; k--;

	if(cache.find(mp(n, k)) == cache.end())
	{
		long long n2 = n/2;
		long long k2 = k/2;

		cache[mp(n, k)] = max(get(n2, k2), get(n-n2, k-k2));
	}
	return cache[mp(n, k)];
}




int main()
{
	long T;
	cin >> T;

	for(int t = 1; t<=T; t++)
	{
		long long n,k;
		cin >> n >> k;
		
		long long res  = get(n, k - 1);
		res--;
		long long res2 = res/2;
#if 0
		map<long long, long long> fs;
		fs[n] = 1;
		fi(k-1)
		{
			auto l = fs.end();
			l--;
			while(l->second == 0)
			{
				fs.erase(l);
				l = fs.end();
				l--;
			}
			l->second--;
			long long cn = l->first;
			cn--;
			long long cn2 = cn/2;
			fs[cn2]++;
			fs[cn-cn2]++;
		}
		auto l = fs.end();
		l--;
		while(l->second == 0)
		{
			fs.erase(l);
			l = fs.end();
			l--;
		}
		if(l->first != res+1)
		{
			l++;
			cout << "wrong";
			cache.clear();
		}
#endif

		cout << "Case #" << t << ": " << res-res2 << " " << res2 << endl;
	}

	return 0;
}

