                    
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

int main(){
	int t, test = 0, D, n;
	ifstream fin("a.in");
	ofstream fout("out.out");
	fin >> t;
	int ds[ 1001 ];
	int v[ 1001 ];
	while(t--){
		double T = eps;

		test++;
		fin >> D >> n;
		FOR(i, 0, n){
		   fin >> ds[ i ] >> v[ i ];
		   double tim = (double)(D - ds[ i ]) / v[ i ];
		   if(tim - T > eps )
		         T = tim; 
	   }
	   fout.flags(ios::fixed);
	   fout.precision(6);
	   double slv = (double)((double)D / T);
	   fout << "Case #"<<test<<": "<<slv << endl;
		}
	
	}
