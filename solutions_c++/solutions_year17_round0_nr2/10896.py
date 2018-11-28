/*
	code well or go home

  mohammad harrawi
	-----  -----
	 ::::  ::::
		 ==
  {_^_^_^_^_^_^_^_^}
*/



#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <list>
#include <stack>
#include <utility>
#include <set>
#include <ctime>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <cctype>

using namespace std;

#define ll long long int 
#define ull unsigned long long int 

#define F first
#define S second
#define MOD 1000000007


const double PI = acos(-1);
const double eps = 1e-9;
const int inf = 2000000000;

#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a) * (a))
#define optimize() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

#define pint(a) printf("%d\n",a)
#define plong(a) printf("%lld\n",a)
#define pdouble(a) printf("%f\n",a)

#define SL(a,n) a<<n
#define SR(a,n) a>>n

inline bool isLeapYear(ll year) { return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0); }

bool comp(const pair < int, int > &p1, const pair < int, int > &p2){ return p1.S < p2.S; }
ll toLL(string a){ return atoll(a.c_str()); }
int toINT(string a){ return atoi(a.c_str()); }
int __gcd(int a, int b) { return b == 0 ? a : __gcd(b, a % b); }

template<typename T>
void __memset(T a[], T val, int size){ T *p = &a[0]; for (size_t i = 0; i < size; i++){ *p++ = val; } }

void primefactors(int n){
	if (n == 1){ pint(1); return; }while (n % 2 == 0){ pint(2); n = n / 2; }
	for (int i = 3; i <= sqrt(n); i = i + 2){ while (n%i == 0){ pint(i); n = n / i; } }if (n > 2)pint(n);
}


using namespace std;
bool istidy(ll num)
{
	if (num < 10)
		return true;
	string xx;
	xx = to_string(num);

	for (size_t i = 0; i < xx.length()-1; i++)
	{
		if (xx[i + 1] < xx[i])
			return false;
	}
	return true;
	
}
int main()
{
	//optimize();
	
	
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("out.out", "w", stdout);

	int t;
	ll num;

	cin >> t;

	for (size_t i = 1; i <= t; i++)
	{
		cin >> num;
		for (ll j = num; j > 0; j--)
		{
			if (istidy(j))
			{
				printf("Case #%d: %lld\n", i, j); 
				break;
			}
		}
		
	}
	return 0;
}