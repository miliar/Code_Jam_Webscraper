#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
typedef unsigned long long ll;

int main( int argc, char * argv[] ) {
  ifstream fin;
  ofstream fout;
  fin.open( argv[1] );
  fout.open( "output.txt" );

  ll t;
  fin >> t;





  // number N from problem statement
  ll n;
  for( ll g = 0; g < t; g++ ) { 
      fin >> n;

      // vector of integers
      vector < ll > grr;

      while( n != 0 ) {
	  grr.push_back( n%10 );
	  n /= 10;
      }
      
      // reverse the vector
      for( ll r = 0; r < grr.size()/2; r++ ) {
	  swap( grr[r], grr[grr.size()-r-1] );
      }

        
      // store the position to change to 9s
      ll pos = -7;
      for( ll r = (grr.size()-1); r > 0; r-- ) {
	  if( grr[r-1] > grr[r] ) {
	      grr[r] = 9;
	      grr[r-1] -= 1;
	      pos = r;
	  }
      }
      
      if( pos == -7 ) {
	  fout << "Case #" << g+1 << ": ";
	  for( ll t = 0; t < grr.size(); t++ ) {
	      fout << grr[t];
	  }
	  fout << endl;
      }

      if( pos != -7 ) {
	  for( ll y = pos; y < grr.size(); y++ ) {
	      grr[y] = 9;
	  }
      
     	  

	  
      // get rid of the leading zeros;
      ll found = 0;
      ll j = 0;
      while( grr[j] == 0 ) {
	  j++;
      }
      
      // debugging
      fout << "Case #" << g+1 << ": ";
      for( ll i = j; i < grr.size(); i++ ) {	  
	  fout << grr[i];	  
      }
      fout << endl;
            
      }
  }
  return 0;
    }







  
/*
int main() {

  
  ofstream fout;
  fout.open( "output.txt" );
  
  ll t;
  cin >> t;

  ll n;
  for( ll i = 0 ; i < t; i++ ) {
    fin >> n;
    // find the length of the digit string
    ll digits = ceil( log( n ) / log( 10 ) );
    
    for( ll g = n; g > 0; g-- ) {
      bool found = 1;
      
      ll g_cpy = g;
      // units digit
      ll current = g_cpy%10;
      for( ll j = 0; j < digits && found; j++ ) {
	g_cpy /= 10;	
	ll compare = g_cpy%10;
	if( compare > current ) {
	  found = 0;
	}
	current = compare;       
      }

      if( found == 1 ) {
        fout << "Case #" << i << ": " << g << endl;
	// break the loop
	g = 0;
      }
    }   
  }

  fin.close();
  fout.close();
  return 0;
}
*/      
  
