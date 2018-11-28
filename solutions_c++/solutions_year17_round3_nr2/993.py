// basic file operations
#include <iostream>
#include <fstream>
using namespace std;

#define DEBUG 0
#define trace if( DEBUG ) printf

int C[2], D[2], J[2], K[2];
int AC, AJ;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
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

		myfile >> AC >> AJ;
		for(int j = 0; j < AC; j++) myfile >> C[j] >> D[j];
		for(int j = 0; j < AJ; j++) myfile >> J[j] >> K[j];

		
		trace("Before sort\n");
		qsort( C, AC, sizeof(int), compare );
		qsort( D, AC, sizeof(int), compare );
		qsort( J, AJ, sizeof(int), compare );
		qsort( K, AJ, sizeof(int), compare );
		trace("After sort\n");

		int res = 2;
		if( AC < 2 && AJ < 2 ) res = 2;
		else if( AC == 2 )
		{
			if(D[1] - C[0] > 720 && D[0] - C[1] + 1440 > 720)
				res = 4;
		}
		else if( AJ == 2 )
		{
			if(K[1] - J[0] > 720 && K[0] - J[1] + 1440 > 720 )
				res = 4;
		}
		else
		{
			printf("Error!!!\n");
			res = 4;
		}
      printf( "Case #%d: %d\n", i, res );
   }

   myfile.close();
   return 0;
}
