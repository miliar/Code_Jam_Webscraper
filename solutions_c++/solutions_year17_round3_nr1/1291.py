// ****************************************************************************
// Code developed starting from Rustyoldman's Google Code jam template
// ****************************************************************************
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cstdlib>
#define enld endl
using namespace std ;
// ****************************************************************************
int getchar ( )
// ****************************************************************************
{
if ( cin.eof() )
   return -1 ;
int ch = cin.get() ;
if ( cin.fail() )
   return -1 ;
return ch ;
}
// ****************************************************************************
string tokenstartchars 
= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
string tokenchars 
= ".0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
// ****************************************************************************
string gettoken ( )
// ****************************************************************************
{
int ch ;

ch = cin.get() ;

while ( ! cin.eof () && (ch == ' ' || ch == '\n') )
   ch = getchar ( ) ;

if ( ch == -1 )
   return "ERROR" ;

string ans = "" ;
if ( tokenstartchars.find( (char) ch ) != string::npos ) 
   {
   while ( tokenchars.find ( (char) ch ) != string::npos)
      {
      ans.push_back((char) ch) ;
      ch = getchar ( ) ;
      }
   cin.putback((char)ch) ;
   return ans ;
   }

ans = "" ;
ans.push_back ( (char) ch ) ;
return ans ;
}
// ****************************************************************************
double getdouble ( ) 
// ****************************************************************************
{
double a ;
cin >> a ;
return a ;
}
// ****************************************************************************
int getint ( ) 
// ****************************************************************************
{
while ( cin.peek ( ) == ' ' || cin.peek ( ) == '\n' )
   getchar ( ) ;
int sign = 1 ;
if ( cin.peek ( ) == '-' )
   {
   sign = -1 ;
   getchar ( ) ;
   }
string toke = gettoken ( ) ;
if ( sign == -1 && toke == "2147483648" )
   return -2147483648 ;

return sign * atoi ( toke.c_str() ) ;
}
// ****************************************************************************
class Cake { public:
  double r , z ;
  double area ;
  double base ;
  bool operator< ( const Cake & o ) const
  {
    if ( r < o.r ) return true ;
    if ( r == o.r && z < o.z ) return true ;
    return false ;
  } ;
} ;
   
// ****************************************************************************
double area [ 1000 ] [ 1001 ] ;
// ****************************************************************************
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
double answer ;
 int want ;
 int have ;
 vector<Cake> p ;
 cin >> have >> want ;
p.resize(have) ;
 for ( int i = 0 ; i < have ; ++i )
   {
     cin >> p[i].r >> p[i].z ;
     p[i].area =  M_PI * p[i].z*2*p[i].r ;
     p[i].base = M_PI * p[i].r*p[i].r ;
   } ;
 
 sort ( p.begin() , p.end() ) ;

 for ( int i = 0 ; i < 1000 ; ++i )
   for ( int j = 0 ; j < 1001 ; ++j )
     area[i][j] = 0 ;
 
 for ( int i = 0 ; i < have ; ++i )
   {
     area [ i ] [ 1 ] = p[i].area ;
     //cout << i << " , 1 = " << p[i].area << endl ;
   }
 for ( int n_cs = 2 ; n_cs <= want ; ++n_cs )
   for ( int new_c = 0 ; new_c < have ; new_c++ )
     {
       area[new_c][n_cs] = 0 ;
       double ac = p[new_c].area ;
       for ( int last = 0 ; last < new_c ; ++last )
	 {
	   if ( area[last][n_cs-1] + ac > area[new_c][n_cs] )
	     area[new_c][n_cs] = area[last][n_cs-1] + ac ;
	 }
       //cout << new_c << " , " << n_cs << " = " << area[new_c][n_cs] << endl ;
	}
 
 answer = 0 ;
 for ( int last = 0 ; last < have ; ++last )
   answer = max ( answer , area [ last ] [ want ] + p[last].base ) ;
		  
cout << "Case #" << case_number << ": " ;
 cout <<  setprecision(24) << answer ;
cout << endl ;
}
// ****************************************************************************
int main ( int argc , char ** argv )
// ****************************************************************************
{
int n ;
cin >> n ; getchar() ;
for ( int i = 1 ; i <= n ; i ++ )
   do_case ( i ) ;
}
// ****************************************************************************
