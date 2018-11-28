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
	ifstream input ("B.in");
	ofstream output ("B.out");
	tint t;
	input >> t;
	map<char,char> anterior = {{'0','9'},{'1','0'},{'2','1'},{'3','2'},{'4','3'},{'5','4'},{'6','5'},{'7','6'},{'8','7'},{'9','8'}};
	forsn(caso,1,t+1)
	{
		string s;
		input >> s;
		tint n = s.size();
		forn(k,100)
		forsn(i,1,n)
		{
			if (s[i] < s[i-1])
			{
				forsn(j,i,n)
					s[j] = '9';
				tint j = i;
				while (j > 0 && s[j] == '9')
				{
					s[j-1] = anterior[s[j-1]];
					j--;
				}
				break;	
			}
		}
		tint p = 0;
		while (s[p] == '0')
			p++;
		s = s.substr(p,n);
			
		output << "Case #" << caso << ": " << s << "\n";
	}
	return 0;
}



