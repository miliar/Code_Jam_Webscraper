#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

//freopen( "input.txt", "r", stdin );
//freopen( "output.txt", "w", stdout );
//fflush( stdin );
//__builtin_popcount()

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define INF 1000000000 //1 Billon
#define EPS 1e-9
#define MOD 1000000007
#define WHITE -1
#define BLACK 1
#define GRAY 2
#define PI acos(-1.0)

//int num_length( int n ) { return int( log10( n ) ) + 1; }
int gcd( int a, int b ){ return b == 0 ? a : gcd( b, a % b ); }
int lcm( int a, int b ){ return a * ( b / gcd( a, b ) ); }
string tos( unsigned long long a ){ ostringstream st; st<<a; string ans = st.str(); return ans; }

#define FOR(i,a,b) for(int i=(a), _b=(b);i<=_b;i++)
#define DOW(i,b,a) for(int i=(b), _a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define mem(A,x) memset(A, x, sizeof A)
#define pb push_back
#define all(A) A.begin(),A.end()
#define si(n) scanf("%d",&n)
#define sf(n) scanf("%f",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define pnl printf("\n")
#define scs(x) gets(x);
#define ub(X,v) upper_bound(X.begin(),X.end(),v)
#define lb(X,v) lower_bound(X.begin(),X.end(),v)

int main( void ) 
{
	int t, icase = 1, len;
	string snumber;
	cin >> t;
	
	while( t-- ){
		cin >> snumber;
		len = (int)snumber.length();
		if( len == 1 )
			cout << "Case #" << icase << ": " << snumber << "\n";
		else{
			REP( i, len - 1 ){
				if( snumber[ i ] > snumber[ i + 1 ] ){
					int num = int( snumber[ i ] ) - 48;
					num--;
					snumber[ i ] = char( num + 48 );
					int j = i + 1;
					int indext = i;
					while( j < len ){
						snumber[ j ] = '9';
						++j;
						++i;
					}
					while( snumber[ indext ] > 0 && snumber[ indext ] < snumber[ indext - 1 ] )	{
						snumber[ indext ] = '9';
						int num = int( snumber[ indext - 1 ] - 48 );
						num--;
						snumber[ indext - 1 ] = char( num + 48 );
						indext--;
					}
				}
			}
			if( snumber[ 0 ] == '0' )
				snumber = snumber.substr( 1, len );
			cout << "Case #" << icase << ": " << snumber << "\n";
		}
		icase++;
	}
	return 0;
}
