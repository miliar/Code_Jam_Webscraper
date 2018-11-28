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



int main()
{
	ifstream input ("A.in");
	ofstream output ("A.out");
	tint t;
	input >> t;
	
	forsn(caso,1,t+1)
	{
		
		tint r,c;
		input >> r >> c;
		
		vector<string> board (r);
		forn(i,r)
			input >> board[i];
		forn(j,c) // para cada columna
		{
			tint last = -1;
			forn(i,r) // la rellenamos
			{
				if (board[i][j] != '?')
				{
					forsn(q,last+1,i)
						board[q][j] = board[i][j];
					last = i;
				}
			}
			if (last != -1)
			{
				forsn(q,last+1,r)
					board[q][j] = board[last][j];
			}
		}
		
		forn(k,c) // pasadas copiando columnas vacias a derecha
		{
			forn(j,c)
			{
				tint last = -1;
				forn(i,r) // la rellenamos
					if (board[i][j] != '?')
						last = i;
				if (last == -1 && j < c-1)
					forn(i,r)
						board[i][j] = board[i][j+1];
			}
		}
		
		forn(k,c) // pasadas copiando columnas vacias a izquierda
		{
			forn(j,c)
			{
				tint last = -1;
				forn(i,r) // la rellenamos
					if (board[i][j] != '?')
						last = i;
				if (last == -1 && j > 0)
					forn(i,r)
						board[i][j] = board[i][j-1];
			}
		}
		
		output << "Case #" << caso << ":\n";
		forn(i,r)
		{
			forn(j,c)
				output << board[i][j];
			output << "\n";
		}
	}
	return 0;
}




