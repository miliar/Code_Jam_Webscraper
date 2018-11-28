/*
B name oooo
ID: amin_un1
PROG: ride
LANG: C++

my ID
uva = "sir sbu"
codforsec = "sir_sbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <complex>
#include <iomanip>
#include <time.h>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX = 100001;
const long long mod = 1000 * 1000 * 1000 + 7;

#define mp make_pair
#define pb(a) push_back(a)
#define L(s) (int)((s).size())
#define all(c) (c).begin(), (c).end()

#define INF (1e14)
#define EPS (1e-6)
#define E (2.718281828459045)


////////////////////////////////////////////////////code///////////////////////////////////////

vector< double> k;
vector< double> s;
long long n;
long double d;


bool check( double a)
{
	 double h = d / a;
	for (int i = 0; i < n; i++)
	{
		if (s[i] * h + k[i] < d)return false;
	}
	return true;
}
double binery( double first,  double second)
{
	if (second - first < EPS) return second;
	if (second < first)return second;
	 double temp = (first + second) / 2;
	if (second - temp < EPS) return temp;
	if (check(temp))
	{
		return binery(temp, second);
	}
	return binery(first, temp);

}


int main()
{
	//ofstream cout ("Aout.out");
	//ifstream cin ("A.in");
	freopen("AA.txt" ,"r" , stdin);
	freopen( "outputAA.txt" , "w" , stdout );

	int test;
	cin >> test;
	int t = 0;
	while (test--)
	{
		cin >> d >> n;
		k.clear();
		s.clear();
		t++;
		for (int i = 0; i < n; i++)
		{
			long long a, b;
			cin >> a >> b;
			k.push_back(a);
			s.push_back(b);
		}
		 double ans = binery(0, INF +1000);
		cout << "Case #" << t << ": ";
		printf("%.6f\n", ans);

	}
}
