
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

vector<string> l;
int H, W;
pair<pair<int,int>,pair<int,int>> trl(int x, int y, int dir)
{
	if(x < 0 || x >= H || y < 0 || y >= W) return mp(mp(-1, -1),mp(dir,'#'));
	if(l[x][y] == '#' || l[x][y] == '?' || l[x][y] == '-' || l[x][y] == '|')
		return mp(mp(x, y), mp(dir, l[x][y]));
	if(l[x][y] == '\\')
	{
		switch(dir)
		{
		case 0:
			return trl(x+1, y, 1);
		case 1:
			return trl(x, y+1, 0);
		case 2:
			return trl(x-1, y, 3);
		case 3:
			return trl(x, y-1, 2);
		}
	}
	if(l[x][y] == '/')
	{
		switch(dir)
		{
		case 0:
			return trl(x-1, y, 3);
		case 1:
			return trl(x, y-1, 2);
		case 2:
			return trl(x+1, y, 1);
		case 3:
			return trl(x, y+1, 0);
		}
	}
	if(l[x][y] == '.')
	{
		switch(dir)
		{
		case 0:
			return trl(x, y+1, 0);
		case 1:
			return trl(x+1, y, 1);
		case 2:
			return trl(x, y-1, 2);
		case 3:
			return trl(x-1, y, 3);
		}
	}
	return mp(mp(-1, -1), mp(dir, '#'));
}


int main()
{
	int T;
	cin >> T;
	for(int cs = 1; cs <= T; cs++)
	{
		cin >> H >> W;
		l.resize(H);
		fi(H) cin >> l[i];

		fi(H)
		{
			fj(W)
			{
				if(l[i][j] == '-') l[i][j] = '?';
				if(l[i][j] == '|') l[i][j] = '?';
			}
		}
		
		bool ispos = true;

		fi(H)
		{
			fj(W)
			{
				if(l[i][j] == '?')
				{
					auto r0 = trl(i, j+1, 0);
					auto r2 = trl(i, j-1, 2);
					auto r1 = trl(i+1, j, 1);
					auto r3 = trl(i-1, j, 3);

					if(r0.second.second != '#' || r2.second.second != '#')
						l[i][j] = '|';
					if(r1.second.second != '#' || r3.second.second != '#')
					{
						if(l[i][j] == '?')
							l[i][j] = '-';
						else
							ispos = false;
					}
				}
			}
		}


		bool ischanges = true;
		int state = 1;
		while(ispos && ischanges)
		{
			ischanges = false;
			fi(H)
			{
				fj(W)
				{
					if(l[i][j] == '.')
					{
						auto r0 = trl(i, j+1, 0);
						auto r2 = trl(i, j-1, 2);
						auto r1 = trl(i+1, j, 1);
						auto r3 = trl(i-1, j, 3);


						if(r0.second.second == '-' && ((r0.second.first & 1) == 0))
							continue;
						if(r0.second.second == '|' && ((r0.second.first & 1) == 1))
							continue;
						if(r1.second.second == '-' && ((r1.second.first & 1) == 0))
							continue;
						if(r1.second.second == '|' && ((r1.second.first & 1) == 1))
							continue;
						if(r2.second.second == '-' && ((r2.second.first & 1) == 0))
							continue;
						if(r2.second.second == '|' && ((r2.second.first & 1) == 1))
							continue;
						if(r3.second.second == '-' && ((r3.second.first & 1) == 0))
							continue;
						if(r3.second.second == '|' && ((r3.second.first & 1) == 1))
							continue;

						vector<pair<pair<int, int>, pair<int, int>>> var;
						if(r0.second.second == '?')
						{
							var.push_back(r0);
							var.back().second.second = ((r0.second.first & 1) == 0)?'-':'|';
						}

						if(r1.second.second == '?')
						{
							var.push_back(r1);
							var.back().second.second = ((r1.second.first & 1) == 0)?'-':'|';
						}
						if(r2.second.second == '?')
						{
							var.push_back(r2);
							var.back().second.second = ((r2.second.first & 1) == 0)?'-':'|';
						}
						if(r3.second.second == '?')
						{
							var.push_back(r3);
							var.back().second.second = ((r3.second.first & 1) == 0)?'-':'|';
						}

						if(!var.size())
						{
							ispos = false;
							continue;
						}
						if(var.size() == 1)
						{
							ischanges = true;
							state = 1;
							l[var[0].first.first][var[0].first.second] = var[0].second.second;
							continue;
						}
						if(state == 1)
							continue;
						l[var[0].first.first][var[0].first.second] = var[0].second.second;
						state = 1;
					}
				}
			}
			if(state == 1 && !ischanges)
			{
				ischanges = true;
				state = 2;
			}
		}

		fi(H)
			fj(W)
			if(l[i][j] == '?')
				l[i][j] = '|';
					
		cout << "Case #" << cs << ": ";
		if(ispos)
		{
			cout << "POSSIBLE" << endl;
			fi(H) cout << l[i] << endl;
		}
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}