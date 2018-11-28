// basic file operations
#include <iostream>
#include <fstream>
using namespace std;

#define DEBUG 0
#define trace if( DEBUG ) printf

/*
qsort( device, N, sizeof(uint64_t), compare );
int compare (const void * a, const void * b)
{
  return ( *(uint64_t*)a - *(uint64_t*)b );
}
*/

int main (int argc, char **argv)
{
   if( argc != 2 ) return -1;
   ifstream myfile;
   int ntests;

   myfile.open( argv[1] );
   myfile >> ntests;
   trace( "Ntests = %d\n", ntests );

   for( int i = 1; i <= ntests; i++ )
   {
      trace( "------------\n" );
      trace( "| Test #%02d |\n", i );
      trace( "------------\n" );

		double D, N, arrival = 0;
		myfile >> D >> N;

		for( int j = 0; j < N; j++ )
		{
			double K, S;
			myfile >> K >> S;

			double arr = (D - K) / S;
			if( arr > arrival)
			{
				arrival = arr;
			}
			trace("%f %f %f %f\n", K, S, arr, arrival);
		}
		double res = D / arrival;
      printf( "Case #%d: %0.6f\n", i, res );
   }

   myfile.close();
   return 0;
}
