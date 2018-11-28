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
 int r , c ;
 vector<string> answer ;
 vector<string> cake ;
// ****************************************************************************
bool col_marked ( int j , int i1 , int i2 )
// ****************************************************************************
{
  for ( int i = i1 ; i <= i2 ; ++i )
      if ( cake[i][j] != '?' )
	return true ;
  return false ;
}
// ****************************************************************************
char get_name ( int i1 , int i2 , int j1 , int j2 )
// ****************************************************************************
{
  for ( int i = i1 ; i <= i2 ; ++i )
    for ( int j = j1 ; j <= j2 ; ++j )
      if ( cake[i][j] != '?' )
	return cake[i][j] ;
  return '?' ;
}
// ****************************************************************************
bool row_marked ( int row )
{
  for ( int i = 0 ; i < c ; ++i )
    if ( cake[row][i] != '?' )
      return true ;
  return false ;
} ;
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
  cin >> r >> c ;
  cerr << r << " rows " << c <<  " cols in cake" << endl ;
 cake.resize(r) ;
 answer.resize(r) ;
 for ( int i = 0 ; i < r ; ++i )
   cin >> cake[i] ;
for ( int i = 0 ; i < r ; ++i )
  {
    answer[i]=cake[i] ;
    cerr << answer[i] << endl ;
  }
 cerr << "case "<< case_number << endl ;

 int last_row = 0 ;
int first_row = 0 ;
 int cr = 0 ;
 while ( first_row < r )
   {
     for ( cr = first_row ; cr < r ; ++cr )
       if ( row_marked(cr) )
	 break ;
     // cr == marked row
     for ( cr = cr+1 ; cr < r ; ++cr )
       if ( row_marked(cr) )
	 break ;
     last_row = cr - 1 ;
     cerr << "row  " << first_row << " to " << last_row << endl ;


     int first_col = 0 ;
     int last_col  = 0 ;
     while ( first_col < c )
       {
	 int cc ;
	 for ( cc = first_col ; cc < c ; ++cc )
	   if ( col_marked(cc , first_row , last_row ) )
	     break ;
	 for ( cc = cc+1 ; cc < c ; ++cc )
	   if ( col_marked(cc , first_row , last_row ) )
	     break ;
	 last_col = cc - 1 ;

	 cerr << "        col = " << first_col << "  to " << last_col << endl ;
	 
	 char ch = get_name ( first_row , last_row , first_col , last_col ) ;
	 for ( int i = first_row ; i <= last_row ; ++i )
	   for ( int j = first_col ; j <= last_col ; ++j )
	     answer[i][j] = ch ;
	 first_col = last_col + 1 ;
       }
     first_row = last_row + 1 ;
   }
 
cout << "Case #" << case_number << ": " ;
cout << endl ;
 for ( int i = 0 ; i < r ; ++i )
   {
     cout << answer[i] << endl ;
     cerr << answer[i] << endl ;
   }
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
