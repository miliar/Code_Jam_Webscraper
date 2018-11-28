#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm> 
#include <iomanip>

using namespace std;

struct Horse { double K; double S; double t; };
bool myless ( Horse a, Horse b ) { return (a.K < b.K); }

int main( int argc, char* argv[] )
{
  int T;
  long long N;
  double D;
  Horse H[1000];

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
    input >> D;
    input >> N;
    for ( int i=0; i<N; i++ )
    {
      input >> H[i].K;
      input >> H[i].S;
    }

    std::sort( H, H+N, myless );

    H[0].t = ( D-H[0].K ) / H[0].S;
    for ( int i=1; i<N; i++ )
    {
      H[i].t = ( D-H[i].K ) / H[i].S;
      if ( H[i].t < H[i-1].t ) H[i].t = H[i-1].t;
    }

    output << std::fixed ;
    output << "Case #" << t+1 << ": " << std::setprecision(6) << ( D/H[N-1].t );
    output << endl;
  }

  input.close();
  output.close();

  return 0;
}

