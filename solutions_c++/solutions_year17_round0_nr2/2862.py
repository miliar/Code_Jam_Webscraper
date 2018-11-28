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

      char N[40];
		myfile >> N;

		trace("%s\n", N);

		int len =strlen(N);
		bool bSet9 = false;
		trace("Foreard\n");
		for( int j = 0; j < len; j++ )
		{
			if(bSet9)
			{
				N[j] = '9';
				trace("%s\n", N);
			}
			else if(j == len - 1)
				break;
			else if(N[j] > N[j+1])
			{
				N[j]--;
				bSet9 = true;
				trace("%s\n", N);
			}
		}

		trace("Backward\n");
		for( int j = strlen(N) - 1; j > 0; j-- )
		{
			if( N[j] < N[j-1])
			{
				N[j] = '9';
				N[j-1]--; // it is at least 1 since > N[j]
				trace("%s\n", N);
			}
		}

      char *res = N;
		while(*res == '0' && *res != '\0') res++;
      printf( "Case #%d: %s\n", i, res );
   }

   myfile.close();
   return 0;
}
