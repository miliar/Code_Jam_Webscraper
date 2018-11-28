
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;



int main( int argc, char* argv[] )
{
  int T;
  unsigned nDigits;
  char aDigits[20];
  char *p;
  string str;

  ifstream input;
  ofstream output;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> str;
    strcpy( aDigits, str.c_str() );
    nDigits = str.length();

    for ( p = aDigits; ( p < aDigits+nDigits-1 ) && ( p[0] <= p[1] ) ; p++ );

    if ( p == aDigits+nDigits-1 )
    {
      output << "Case #" << t+1 << ": " <<  str << endl; 
    }
    else
    {
      for ( ; ( p>aDigits ) && ( p[0] == p[-1] ) ; p-- );
      for ( --(*p++); p < aDigits+nDigits; (*p++) = '9' );
      output << "Case #" << t+1 << ": " << ( aDigits[0] == '0' ? aDigits+1 : aDigits ) << endl;
    }
  }

  input.close();
  output.close();

  return 0;
}

