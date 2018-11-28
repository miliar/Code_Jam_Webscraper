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

struct Cosa
{
	tint ingrediente, paquete, prioridad;
	Cosa (tint ii, tint pp, tint pepe)
	{
		ingrediente = ii;
		paquete = pp;
		prioridad = pepe;
	}
};

bool operator < (Cosa c1, Cosa c2)
{
	return make_tuple(c1.prioridad, c1.ingrediente, c1.paquete) < make_tuple(c2.prioridad, c2.ingrediente, c2.paquete);
}

int main()
{
	ifstream input ("B.in");
	ofstream output ("B.out");
	tint t;
	input >> t;
	forsn(caso,1,t+1)
	{
		
		tint n,p;
		input >> n >> p;
		vector<tint> r (n);
		forn(i,n)
			input >> r[i];
		vector<vector<tint> > q (n, vector<tint> (p));
		map<tint, vector<Cosa> > w;
		map<tint, vector<tint> > hist;
		
		forn(i,n)
		{
			
			forn(j,p)
			{
				input >> q[i][j];
				tint maxKInf = 0, maxKSup = 1e9;
				tint minKInf = 0, minKSup = 1e9;
				while (maxKSup - maxKInf > 1)
				{
					tint k = (maxKSup + maxKInf) / 2;
					if (10*q[i][j] <= 11*k*r[i])
						maxKSup = k;
					else
						maxKInf = k;
				}
				while (minKSup - minKInf > 1)
				{
					tint k = (minKSup + minKInf) / 2;
					if (10*q[i][j] >= 9*k*r[i])
						minKInf = k;
					else
						minKSup = k;
				}
				swap(minKInf,maxKSup);
				
				forsn(k,minKInf,maxKSup+1)
				{
					w[k].push_back(Cosa(i,j,maxKSup-k));
					if (hist[k].empty())
						hist[k] = vector<tint> (n);
					hist[k][i]++;
				}
			}
		}
		
		vector<vector<tint> > usado (n, vector<tint> (p));
		tint ans = 0;
		
		map<tint, vector<tint> > debo;
		for (auto x : w)
		{
			if (x.first > 0)
			{
				if (!debo[x.first].empty())
					forn(i,n)
						hist[x.first][i] -= debo[x.first][i];
				
				tint z = *min_element(hist[x.first].begin(),hist[x.first].end());
				ans += z;
				
				sort(x.second.begin(),x.second.end());
				vector<tint> l (n,0);
				for (auto y : x.second)
				{
					if (l[y.ingrediente] < z && !usado[y.ingrediente][y.paquete])
					{
						l[y.ingrediente]++;
						usado[y.ingrediente][y.paquete] = 1;
						if (y.prioridad > 0)
						{
							forn(k,y.prioridad)
							{
								if (debo[x.first+k+1].empty())
									debo[x.first+k+1] = vector<tint> (n);
								debo[x.first+k+1][y.ingrediente]++;
							}
						}
						
					}
				}
			}
		}
		
		
		
		output << "Case #" << caso << ": " << ans << "\n";

	}
	return 0;
}




