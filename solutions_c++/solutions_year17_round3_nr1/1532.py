#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <tuple>
#include <functional>
#include <unordered_set>
#include <unordered_map>
#include <sstream>
#include <stdio.h>
#include <valarray>
#include <iomanip>

typedef long long tint;
typedef unsigned long long utint;
typedef long double ldouble; 


#define forn(i,n) for(tint i=0;i<(tint)(n); i++)
#define forsn(i,s,n) for(tint i=(s);i<(tint)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl



using namespace std;



void imprimirVector (vector<tint> v)
{
	if (!v.empty())
	{ 
		tint p = tint(v.size());
		cout << "[";
		forn(i,p-1)
			cout << v[i] << ",";
		cout << v[p-1] << "]" << endl;
	}
	else
		cout << "[]" << endl;
}

tint toNumber (string s)
{
	tint Number;
	if ( ! (istringstream(s) >> Number) )
		Number = 0; // el string vacio lo manda al cero
	return Number;
}

string toString (tint number)
{    
    ostringstream ostr;
    ostr << number;
    return  ostr.str();
}

// CRIBA

//const tint maxN = 1000500;
//int p[maxN + 1] = {1, 1};
//tint phi[maxN]; // DAR CHANGUI DE 500 O MAS

//
//map<tint,tint> factorizar (tint n)
//{
//	map<tint,tint> f;
//	while (n > 1) 
//	{ 
//		f[p[n]]++;
//		n /= p[n]; 
//	}
//	return f;
//}
// ESTO VA EN EL MAIN
//	for (int i = 1; i <= maxN; ++i)
//		if (p[i] == 1)
//			for (int j = i; j <= maxN; j += i)
//				p[j] = i;
//for (tint i = 0; i < maxN; i++) 
//		phi[i] = i;	
//	for (tint i = 1; i < maxN; i++)
//		for (tint j = 2 * i; j < maxN; j += i)
//			phi[j] -= phi[i];

struct Panqueque
{
	ldouble r,h;
	tint indice;
	Panqueque (ldouble rr, ldouble hh, tint ii)
	{
		r = rr;
		h = hh;
		indice = ii;
	}
};

bool operator < (Panqueque p1, Panqueque p2)
{
	return make_tuple(p2.r, p2.h, p1.indice) < make_tuple(p1.r, p1.h, p2.indice);
}

const ldouble INFINITO = 1e15;

const ldouble pi = acos(-1);

int main()
{
	ifstream input ("A.in");
	ofstream output ("A.out");
	tint t;
	input >> t;
	
	forsn(caso,1,t+1)
	{
		
		tint n,kk;
		input >> n >> kk;
		vector<Panqueque> p (n, Panqueque (0.0,0.0,0));
		forn(i,n)
		{
			ldouble rr,hh;
			input >> rr >> hh;
			p[i] = Panqueque(rr,hh,i+1);
		}
		sort(p.begin(),p.end());
		vector<vector<ldouble> > bestSurface (n, vector<ldouble> (kk,-INFINITO));
		
		forn(i,n)
		forn(k,kk)
		{
			if (k == 0)
				bestSurface[i][k] = pi*p[i].r*p[i].r + 2*pi*p[i].r*p[i].h;
			else
				forn(j,i)
					bestSurface[i][k] = max(bestSurface[i][k],bestSurface[j][k-1] + 2*pi*p[i].r*p[i].h);
		}
		ldouble ans = -INFINITO;
		forn(i,n)
			ans = max(ans,bestSurface[i][kk-1]);
		//~ cout.precision(17);
		
		output << "Case #" << caso << ": " << fixed << showpoint << setprecision(16) << ans << "\n";
		
	}
	return 0;
}




