
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;



int main( int argc, char* argv[] )
{
  int T;
  unsigned long long K, N, K0, K1, mask, S, u;
  unsigned long long p, Ls, Lr;

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
    input >> N;
    input >> K;

    mask = 1ll << 60;
    while ( !( mask & K ) ) mask >>=1;

    K0 = mask - 1;
    K1 = K - K0;

    S = ( N-K0 ) / mask;
    u = ( N-K0 ) % mask;

    if ( K1 <= u )
    {
      Ls = S/2;
      Lr = (S+1)/2;
    }
    else
    {
      Ls = (S-1)/2;
      Lr = S/2;
    }

    output << "Case #" << t+1 << ": " << max( Ls, Lr) << " " << min( Ls, Lr ) << endl;  
  }

  input.close();
  output.close();

  return 0;
}

