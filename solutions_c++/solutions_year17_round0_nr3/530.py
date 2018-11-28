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
class Runs { public: // "runs" ha ha
long width ;
long count ;
} ;
// ****************************************************************************
vector<Runs> runs ;
// ****************************************************************************
long find_width ( long w )
// ****************************************************************************
{
 for ( long i = 0 ; i < runs.size() ; ++i )
    if ( runs[i].width == w )
       return i ;
 Runs r ;
 r.width = w ;
 r.count = 0 ;
 runs.push_back(r) ;
 return runs.size() - 1 ;
} ;
// ****************************************************************************
long largest ( )
// ****************************************************************************
{
 long maxw = 0 ;
 long maxi = -1 ;
 
 for ( long i = 0 ; i < runs.size() ; ++i )
    if ( runs[i].width > maxw && runs[i].count > 0 )
       {
       maxw = runs[i].width ;
       maxi = i ;
       }
 return maxi ;
}
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
 long stalls ;
 long people ;
 cin >> stalls >> people ;
 long remaining = people ;
 runs.resize(0) ;
 Runs run ;
 run.width = stalls ;
 run.count = 1 ;
 runs.push_back(run) ;
 long a1 = 0 ;
 long a2 = 0 ;
 while ( remaining > 0 )
    {
    long li = largest() ;
    long lw = runs[li].width ;
    long lc = runs[li].count ;
    //cout << "largest = " << lw << " (" << lc << ")" << endl ;

    long dc = min ( remaining , lc ) ;
    //cout << "splitting " << dc << endl ;

    long w1 = (lw - 1 )/ 2 ;
    long w2 = lw - w1 - 1 ;

    //cout << lw << "->" << w1 << "," << w2 << endl ;
    runs[li].count -= dc ;
    long i1 = find_width(w1) ;
    runs[i1].count += dc ;
    

    long i2 = find_width(w2) ;
    runs[i2].count += dc ;
    remaining -= dc ;
    a1 = w2 ;
    a2 = w1 ;
    }
 
cout << "Case #" << case_number << ": " ;
 cout <<  a1 << " " << a2 ;
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
