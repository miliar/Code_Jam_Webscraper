#include<iostream>
using namespace std;

string M[5000];
  int R , C;

void go( int i , int j )
{
   for( int w = j - 1 ; w >= 0 && M[i][w] == '?'; --w )
     M[i][w] = M[i][j] ;
   for( int w = j + 1 ; w < C && M[i][w] == '?'; ++w )
     M[i][w] = M[i][j] ;

}

void go2( int i )
{
   for( int w = i - 1 ; w >= 0 && M[w][0] == '?'; --w )
     M[w] = M[i]; 
   for( int w = i + 1 ; w < R && M[w][0] == '?'; ++w )
     M[w] = M[i]; 

}

int main()
{
  int t;

  cin >> t;
  for( int tc = 1 ; tc <= t ; ++tc )
  {
    cout << "Case #"<<tc<<":"<<endl;
    cin >> R >> C;
    for( int i = 0 ; i < R ; ++i )
    {
      M[i] = string( C , '?');
      for( int j = 0 ; j < C ; ++j )
      {
	cin >> M[i][j];
      }
    }
    for( int i = 0 ; i < R ; ++i )
    {
      for( int j = 0 ; j < C ; ++j )
      {
	if( M[i][j] != '?' ) 
	   go( i , j );
      }
    }
    for( int i = 0 ; i < R ; ++i )
        if( M[i][0] != '?')
            go2(i);	  
    for( int i = 0 ; i < R ; ++i )
      cout << M[i] <<endl;
  }
  return 0;
}
