// ****************************************************************************
// Code developed starting from Rustyoldman's Google Code jam template
// May 8, 2016
// I am coding from a campground in Colorado at 3AM for this contest.
// I didn't remember to load any of my library code onto this new laptop
// before starting this trip. I reconstructed this boilerplate by downloading
// a previous GCJ round's submission and editing out the solution.
//
// This should be interesting.
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
long tidy_up ( long n )
// ****************************************************************************
{
 long d [20] ;
 int dc = 0 ;
    for ( int i = 0 ; i < 20 ; ++i )
       d[i] = 0 ;

 long r = n ;
 int p = 0 ;
 while ( r > 0 )
    {
    d[p] = r%10 ;
    r /= 10 ;
    ++p ;
    }
 for ( int i = 19 ; i > 0 ; --i )
    {
    if ( d[i] > d[i-1] )
       {
       --d[i] ;
       for ( int k = i-1 ; k >= 0 ; --k )
	  d[k] = 9 ;
       long m = 0 ;
       for ( int j = 19 ; j >= 0 ; --j )
	  m = m*10+d[j] ;
       return tidy_up ( m ) ;
       }
    }
 return n ;
} ;
// ****************************************************************************
// ****************************************************************************
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
long answer ;
cin >> answer ;

    
 
cout << "Case #" << case_number << ": " ;
cout <<  tidy_up ( answer ) ;
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
