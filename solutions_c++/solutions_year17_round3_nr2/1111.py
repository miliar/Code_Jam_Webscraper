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
class Interval { public:
  int start , finish ;
  int who ;
  bool operator< ( const Interval & o ) const
  {
    return start < o.start ;
  } ;
} ;
// ****************************************************************************
int flips [ 1441 ][1441][2] ; // [total][a_time] [prev who]
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
int answer ;
 int a_count , b_count ;
 vector<Interval> a ;
 vector<Interval> b ;

 cin >> a_count >> b_count ;
 a.resize(a_count) ;
 b.resize(b_count) ;

 for ( int i = 0 ; i < a_count ; ++i )
   cin >> a[i].start >> a[i].finish;
 for ( int i = 0 ; i < b_count ; ++i )
   cin >> b[i].start >> b[i].finish;

 sort ( a.begin() , a.end() ) ;
sort (b.begin() , b.end() ) ;
 vector<Interval> inter ;
 for ( int i = 0 ; i < a_count ; ++i )
   {
     a[i].who = 0 ;
     inter.push_back ( a[i] ) ;
   }
 
 for ( int i = 0 ; i < b_count ; ++i )
   {
     b[i].who = 1 ;
     inter.push_back ( b[i] ) ;
   }

 sort ( inter.begin() , inter.end() ) ;

  for ( int i = 0 ; i < 1441 ; ++i )
    for ( int j = 0 ; j < 1441 ; ++j )
      flips[i][j][0]= flips[i][j][1] = -1 ;
 
  int must [1441] ;
  for ( int i = 0 ; i < 1441 ; ++i )
    must [i] = 3 ;
  for ( int i = 0 ; i < a.size() ; ++i )
    for ( int j = a[i].start ; j < a[i].finish ; ++j )
      must[j] = 1 ;
  for ( int i = 0 ; i < b.size() ; ++i )
    for ( int j = b[i].start ; j < b[i].finish ; ++j )
      must[j] = 2 ;

  
  // int bi = 0 ;
  // int ai = 0 ;
  // int off = a[1]
  // for ( int m = 1 ; m < 1440 ; ++m )
  //   {
  //     for ( int amin = 0 ; amin <= m ; ++amin  )
  // 	{
  // 	  // 0
  // 	  int f ;
  // 	  if ( flips[m-1][amin][0] != -1 )
  // 	    {
  // 	      f = flips[m-1][amin][0] ;
  // 	      if ( flips[m][amin+1][0] == -1 ||
  // 		   flips[m][amin+1][0] > f )
  // 		flips[m][amin+1][0] = f ;
  // 	    }

  // 	  if ( flips[m-1][amin][1] != -1 )
  // 	    {
  // 	      f = flips[m-1][amin][1] + 1 ;
  // 	      if ( flips[m][amin+1][0] == -1 ||
  // 		   flips[m][amin+1][0] > f )
  // 		flips[m][amin+1][0] = f ;
  // 	    }
  
  // 	  // 1
  // 	  if ( flips[m-1][amin][1] != -1 )
  // 	    {
  // 	      f = flips[m-1][amin][1] ;
  // 	      if ( flips[m][amin+1][1] == -1 ||
  // 		   flips[m][amin+1][1] > f )
  // 		flips[m][amin+1][1] = f ;
  // 	    }

  // 	  if ( flips[m-1][amin][0] != -1 )
  // 	    {
  // 	      f = flips[m-1][amin][0] + 1 ;
  // 	      if ( flips[m][amin+1][1] == -1 ||
  // 		   flips[m][amin+1][1] > f )
  // 		flips[m][amin+1][1] = f ;
  // 	    }
  // 	}
  //   }

  // answer = min ( flips [ 1440 ] [ 720 ] [ 0 ] ,
  // 		 flips [ 1440 ] [ 720 ] [ 1 ] ) ;

  answer = 2 ;

  if ( a.size() == 2 )
    {
      int e = a[1].finish ;
      if ( a[1].finish < a[1].start )
	e += 1440 ;

      if ( e - a[0].start <= 720 )
	answer = 2 ;
      else if ( a[0].finish - a[1].start + 1440 <= 720 )
	answer = 2 ;
      else
	answer = 4 ;
    }
  if ( b.size() == 2 )
    {
      int e = b[1].finish ;
      if ( b[1].finish < b[1].start )
	e += 1440 ;

      if ( e - b[0].start <= 720 )
	answer = 2 ;
      else if ( b[0].finish - b[1].start + 1440 <= 720 )
	answer = 2 ;
      else
	answer = 4 ;
    }
    
  
cout << "Case #" << case_number << ": " ;
cout <<  answer ;
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
