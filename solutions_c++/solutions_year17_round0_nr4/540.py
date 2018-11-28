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
int row_non [1000] ;
int col_non [1000] ;
int dia_dif_static [5000] ;
int diag_sum_non [2000] ;
int * diag_dif_non = dia_dif_static+2500 ;
int style_points = 0 ;
// ****************************************************************************
vector<int> orig_r_x ;
vector<int> orig_c_x ;
vector<int> orig_r_o ;
vector<int> orig_c_o ;
vector<int> orig_r_plus ;
vector<int> orig_c_plus ;
vector<int> new_x_r ;
vector<int> new_x_c ;
vector<int> new_o_r ;
vector<int> new_o_c ;
vector<int> new_plus_r ;
vector<int> new_plus_c ;
char orig [1000][1000] ;
char maxed [1000][1000] ;
int n ;
int n_mods = 0 ;
// ****************************************************************************
void load ( )
// ****************************************************************************
{
  cin >> n ;
  int k ;
  cin >> k ;
  style_points = 0 ;

  for ( int i = 0 ; i < n ; ++i )
    for ( int j = 0 ; j < n ; ++j )
      maxed[i][j] = orig[i][j] = ' ' ;
  for ( int i = 0 ; i < n ; ++i )
    row_non [i] = col_non[i] = 0 ;
  for ( int i = 0 ; i < 2*n ; ++i )
    diag_sum_non[i] = 0 ;
  for ( int i = 0 ; i < n ; ++i )
    diag_dif_non[i] = diag_dif_non[-i] = 0 ;
  
  for ( int i = 0 ; i < k ; ++i )
    {
      char kind ;
      int r , c ;
      cin >> kind >> r >> c ;
      --r ;
      --c ;
      if ( kind == 'o' )
	{
	  ++row_non[r] ;
	  ++col_non[c] ;
	  ++diag_sum_non[r+c] ;
	  ++diag_dif_non[r-c] ;
	  orig_r_o.push_back(r) ;
	  orig_r_o.push_back(c) ;
	  style_points += 2 ;
	}
      if ( kind == '+' )
	{
	  ++diag_sum_non[r+c] ;
	  ++diag_dif_non[r-c] ;
	  orig_r_plus.push_back(r) ;
	  orig_r_plus.push_back(c) ;
	  ++style_points ;
	}
      if ( kind == 'x' )
	{
	  ++row_non[r] ;
	  ++col_non[c] ;
	  orig_r_x.push_back(r) ;
	  orig_r_x.push_back(c) ;
	  ++style_points ;
	}
      orig[r][c] = maxed[r][c] = kind ;
    }

  // cerr << "row nons " ;
  // for ( int i = 0 ; i < n ; ++i )
  //   cerr << row_non[i] << " " ;
  // cerr << endl ;
  // cerr << "col nons " ;
  // for ( int i = 0 ; i < n ; ++i )
  //   cerr << col_non[i] << " " ;
  // cerr << endl ;

  // cerr << "pri nons " ;
  // for ( int i = -n+1 ; i < n ; ++i )
  //   if ( i == 0 )
  //     cerr << "|" << diag_dif_non[i] << "| " ;
  //   else
  //   cerr << diag_dif_non[i] << " " ;
  // cerr << endl ;
  // cerr << "sec nons " ;
  // for ( int i = 0 ; i < 2*n-1 ; ++i )
  //   if ( i == n-1 )
  //     cerr << "|" << diag_sum_non[i] << "| " ;
  //   else
  //     cerr << diag_sum_non[i] << " " ;
  // cerr << endl ;
}
// ****************************************************************************
void print_maxed ( )
// ****************************************************************************
{
  // for ( int i = 0 ; i < n ; ++i )
  //   {
  //     cerr << "|" ;
  //     for ( int j = 0 ; j < n ; ++j )
  // 	cerr << maxed[i][j] << " " ;
  //     cerr << "|" << endl ;
  //   }
  // for ( int i = -2 ; i < n ; ++i )
  //   cerr << "-" ;
  // cerr << endl ;
}
// ****************************************************************************
int get_score ( )
// ****************************************************************************
{
  int style_points = 0 ;
  for ( int i = 0 ; i < n ; ++i )
    for ( int j = 0 ; j < n ; ++j )
      if ( maxed[i][j] == 'x' ||
	   maxed[i][j] == 'X' ||
	   maxed[i][j] == '+' ||
	   maxed[i][j] == 'H' )
	++style_points ;
      else if ( maxed[i][j] == 'o' ||
		maxed[i][j] == 'O' ||
		maxed[i][j] == '0' )
	style_points += 2 ;
       
  return style_points ;
} ;
// ****************************************************************************
bool test_o ( int i , int j )
// ****************************************************************************
{
if ( maxed[i][j] == ' ' &&
     row_non[i] < 1 &&
     col_non[j] < 1 &&
     diag_sum_non[i+j] < 1 &&
     diag_dif_non[i-j] < 1 )
   {
   ++row_non[i] ;
   ++col_non[j] ;
   ++diag_sum_non[i+j] ;
   ++diag_dif_non[i-j] ;
   new_plus_r.push_back(i) ;
   new_plus_c.push_back(j) ;
   maxed[i][j] = 'O' ; // two point increase O
   return true ;
   }
return false ;
}
// ****************************************************************************
bool test_plus ( int i , int j )
// ****************************************************************************
{
if ( maxed[i][j] == ' ' &&
     diag_sum_non[i+j] < 1 &&
     diag_dif_non[i-j] < 1 )
   {
    ++diag_sum_non[i+j] ;
    ++diag_dif_non[i-j] ;
    new_plus_r.push_back(i) ;
    new_plus_c.push_back(j) ;
    maxed[i][j] = 'H' ;
    return true ;
   }
return false ;
} ;
// ****************************************************************************
bool test_x ( int i , int j )
// ****************************************************************************
{
if ( maxed[i][j] == ' ' &&
     col_non[j] < 1 &&
     row_non[i] < 1 )
   {
    ++row_non[i] ;
    ++col_non[j] ;
    new_plus_r.push_back(i) ;
    new_plus_c.push_back(j) ;
    maxed[i][j] = 'X' ;
    return true ;
   }
return false ;
} ;
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
 load() ;

 for ( int ii = 0 ; ii < n/2+1 ; ++ii )
    {
    int i = ii ;
    for ( int jj = 0 ; jj < n ; ++jj )
       {
	 int j = jj ;
	 test_x(i,j) ;
	 j = n-1-jj ;
	 test_x(i,j) ;
       }
    i = n-1-ii ;
    for ( int jj = 0 ; jj < n ; ++jj )
       {
	 int j = jj ;
	 test_x(i,j) ;
	 j = n-1-jj ;
	 test_x(i,j) ;
       }
    }

  for ( int ii = 0 ; ii < n/2+1 ; ++ii )
    {
    int i = ii ;
    for ( int jj = 0 ; jj < n/2+1 ; ++jj )
       {
	 int j = jj ;
	 test_o ( i , j ) ;
	 j = n-1-jj ;
	 test_o ( i , j ) ;
       }
    i = n-1-ii ;
    for ( int jj = 0 ; jj < n/2+1 ; ++jj )
       {
	 int j = jj ;
	 test_o ( i , j ) ;
	 j = n-1-jj ;
	 test_o ( i , j ) ;
       }
    }


  for ( int ii = 0 ; ii < n/2+1 ; ++ii )
    {
    int i = ii ;
    for ( int jj = 0 ; jj < n/2+1 ; ++jj )
       {
	 int j = jj ;
	 test_plus ( i , j ) ;
	 j = n-1-jj ;
	 test_plus ( i , j ) ;
       }
    i = n-1-ii ;
    for ( int jj = 0 ; jj < n/2+1 ; ++jj )
       {
	 int j = jj ;
	 test_plus ( i , j ) ;
	 j = n-1-jj ;
	 test_plus ( i , j ) ;
       }
    }
	  
  for ( int i = 0 ; i < n ; ++i )
      for ( int j = 0 ; j < n ; ++j )
	{
	  if ( ( maxed[i][j] == 'H' || maxed[i][j] == '+' ) &&
	       row_non[i] < 1 && col_non[j] < 1 )
	    {
	      ++row_non[i] ;
	      ++col_non[j] ;
	      new_o_r.push_back(i) ;
	      new_o_c.push_back(j) ;
	      if ( orig[i][j] == ' ' )
		maxed[i][j] = 'O' ; // new O
	      else
		maxed[i][j] = '0' ; // upgrade existing x or +
	      break ;
	    }
	  if ( ( maxed[i][j] == 'X' || maxed[i][j] == 'x' ) &&
	       diag_sum_non[i+j] < 1 && diag_dif_non[i-j] < 1 )
	    {
	      ++diag_sum_non[i+j] ;
	      ++diag_dif_non[i+j] ;
	      new_o_r.push_back(i) ;
	      new_o_c.push_back(j) ;
	      if ( orig[i][j] == ' ' )
		maxed[i][j] = 'O' ; // new O
	      else
		maxed[i][j] = '0' ; // upgrade existing x or +
	      break ;
	    }
	}
	  
 print_maxed ( ) ;
 style_points = get_score ( ) ;

 n_mods = 0 ;
 for ( int i = 0 ; i < n ; ++i )
   for ( int j = 0 ; j < n ; ++j )
     if ( orig[i][j] != maxed[i][j] )
       ++n_mods ;
  
 cout << "Case #" << case_number << ": " ;
 cout << style_points << " " << n_mods ;
 cout << endl ;
 for ( int i = 0 ; i < n ; ++i )
   for ( int j = 0 ; j < n ; ++j )
     if ( orig[i][j] != maxed[i][j] )
       {
       if ( maxed[i][j] == 'X' )
	 cout << "x " << i+1 << " " << j+1 << endl ;
       else if ( maxed[i][j] == 'H' )
	 cout << "+ " << i+1 << " " << j+1 << endl ;
       else 
	 cout << "o " << i+1 << " " << j+1 << endl ;
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
