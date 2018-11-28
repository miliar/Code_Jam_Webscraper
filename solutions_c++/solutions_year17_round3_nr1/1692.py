                    
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<limits>
#include <list>
#include <stack>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<memory.h>
using namespace std;


#define vi vector<int>
#define pb push_back
# define MEM(array,w)   memset(array,w,sizeof array)
# define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define S  size()
# define SET set<int>::iterator it = s.begin(); it != s.end();it++
# define ULL unsigned long long
# define eps 1e-9
# define LL  long long 
# define IS istringstream 
# define FORI(i,a,b) for(int i = a ; i <= b ; i++)
# define MFOR(i,a,b) for(int i = a ; i > b ; i--)
# define MFORI(i,a,b) for(int i = a ; i >= b ; i--)
# define PII pair<int , int>
#define all(c) (c).begin(), (c).end() 
#define maxint 1 << 31 - 1

bool pairCompare(const std::pair<double, double>& a, const std::pair<double, double>& b) {
  return a.first > b.first;

}
double dp[ 1001 ][ 1001 ];

vector<pair<double,double> > v;

    double pi = 3.14159265359;

double func(int i, int j){
	if(dp[ i ][ j ] > 0)
	   return dp[ i ][ j ];
	if(!j)
	    return dp[ i ][ j ] = 0;
	if(!i)
	   return  dp[ i ][ j ] =  pi * v[ i ].first * v[ i ].first + 2 * pi * v[ i ].first * v[ i ].second;
	 if( j == 1)
	     return dp[ i ][ j ] = max(func(i - 1, j), pi * v[ i ].first * v[ i ].first
				   + 2 * pi * v[ i ].first * v[ i ].second);
		 else
		 dp[ i ][ j ] = max(func(i - 1, j), func(i - 1, j - 1) + 2 * pi * v[ i ].first * v[ i ].second);
	 return dp[ i ][ j ];
	
	}
int main(){
	int t, test = 0;
	ifstream fin("A.in");
	ofstream fout("Al.out");
	fin >> t; 
	
	while(t--){
		test++;
		v.clear();
		int n,k;
		double r, h;
		fin >> n >> k;
		for(int i = 0; i < n; i++){
			fin >> r >> h;
			pair<int,int> p;
			p.first = r;
			p.second = h;
			v.push_back(p);
		}
		sort(v.begin(), v.end(), pairCompare); 
		FOR(i, 0, n)
		    FOR(j, 0, k + 1) 
		       dp[ i ][ j ] = -1.;
		       
		FOR(i, 0, n) 
		       dp[ i ][ 0 ] = 0.;    
		/*FOR(i, 0, n){
			FOR(j, 1, k + 1){
				if(i && k > 1)
				dp[ i ][ j ] = max(dp[ i - 1 ][ j ], dp[ i - 1 ][ j - 1 ] + 2 * pi * v[ i ].first * v[ i ].second);
				else if( i && k == 1)
				   dp[ i ][ j ] = max(dp[ i - 1 ][ j ], dp[ i - 1 ][ j - 1 ] +  pi * v[ i ].first * v[ i ].first
				   + 2 * pi * v[ i ].first * v[ i ].second);
				   else if(!i)
				   dp[ i ][ j ] =  pi * v[ i ].first * v[ i ].first
				   + 2 * pi * v[ i ].first * v[ i ].second;
				}
			}*/
			func(n - 1, k);
			  fout.flags(ios::fixed);

			  fout.precision(9);

			fout << "Case #"<<test<<": "<<dp[ n - 1 ][ k ]  << endl;
		//   cout << dp[ n - 1 ][ k ] << endl;
	}

		
	
	}


/*
 
 4
 1 1
 3 2
 
 */
