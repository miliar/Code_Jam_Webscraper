// basic file operations
#include <iostream>
#include <fstream>
using namespace std;

#define DEBUG 0
#define trace if( DEBUG ) printf

int compare (const void * a, const void * b)
{
  double diff = *(double*)a - *(double*)b;
  if(diff < 0) return -1;
  else if(diff > 0) return 1;
  else return 0;
}

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

		int N, K;
		myfile >> K >> N;
		trace("N = %d, K = %d\n", N, K );

		double U;
		myfile >> U;
		trace("U = %f\n", U);

		double P[52];
		for(int n = 0; n < N; n++ )
			myfile >> P[n];
		P[N] = 1;
		P[N+1] = 2;

		qsort( P, N, sizeof(double), compare );

		double next = 1.0;
		double cur = P[0];

		int n = 1;
		while(cur == P[n]) n++;
		if( n < N ) next = P[n];

		trace("P = %f\n", cur);
		while( U > 1e-9 )
		{
			double alloc = next - cur;
			trace("n = %d, Cur = %f, Next = %f, Alloc = %f ", n, cur, next, alloc);
			if(alloc * n > U) alloc = U / n;
			trace("%f\n", alloc);

			for(int j = 0; j < n; j++)	P[j] += alloc;
			U -= alloc * n;

			trace("U = %f, P = %f\n", U, P[0]);

			cur = P[n];
			n++;
			while(cur == P[n]) n++;
			next = P[n];
		}

		double prod = 1;
		for(int n = 0; n < N; n++)
			prod *= P[n];
      printf( "Case #%d: %f\n", i, prod );
   }

   myfile.close();
   return 0;
}
