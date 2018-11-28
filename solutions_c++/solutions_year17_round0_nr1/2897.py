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

   char S[1100];
   int K;
   myfile.open( argv[1] );
   myfile >> ntests;
   trace( "Ntests = %d\n", ntests );

   for( int i = 1; i <= ntests; i++ )
   {
      trace( "------------\n" );
      trace( "| Test #%02d |\n", i );
      trace( "------------\n" );

		int res = 0;
      myfile >> S >> K;

      trace( "%d %s\n", K, S );

      int len = strlen(S);
      for( int j = 0; j < len - K + 1; j++ )
      {
			if(S[j] == '-')
			{
				res++; // flipping
				for(int k = 0; k < K; k++)
				{
					switch(S[j+k])
					{
						case '-': S[j+k] = '+'; break;
						case '+': S[j+k] = '-'; break;
						default:
							trace( "Error at index %d while %d\n", k, j );
							j = len;
							break;
					}
				}
				trace( "%s\n", S );
			}
      }

		trace( "%s\n", S );

		bool bOK = true;
		for( int j = 0; j < len; j++ )
			if(S[j] != '+')
			{
				bOK = false;
				break;
			}

      printf( "Case #%d: ", i );
		if(bOK)
			printf("%d", res);
		else
			printf("IMPOSSIBLE");
		printf("\n");
   }

   myfile.close();
   return 0;
}
