// basic file operations
#include <iostream>
#include <fstream>
using namespace std;

#define DEBUG 0
#define trace if( DEBUG ) printf

int ind[1000];
int ind2[1000];
double R[1000];
double H[1000];

int compare (const void * a, const void * b)
{
  int n1 = *(int*)a;
  int n2 = *(int*)b;

  if( R[n1] < R[n2] ) return 1;
  else if( R[n1] > R[n2] ) return -1;
  else
  {
    if( H[n1] < H[n2] ) return 1;
    else if( H[n1] > H[n2] ) return -1;
    else return 0;
  }
}

int compare2 (const void * a, const void * b)
{
  int n1 = *(int*)a;
  int n2 = *(int*)b;

  if( R[n1] * H[n1] < R[n2] * H[n2] ) return 1;
  else if( R[n1] * H[n1] > R[n2] * H[n2] ) return -1;
  else
  {
    if( H[n1] < H[n2] ) return 1;
    else if( H[n1] > H[n2] ) return -1;
    else return 0;
  }
}
#define PI 3.141592653589793238

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
		myfile >> N >> K;

		for(int j = 0; j < N; j++)
		{
			ind[j] = j;
			ind2[j] = j;
			myfile >> R[j] >> H[j];
		}
		qsort( ind, N, sizeof(int), compare );
		qsort( ind2, N, sizeof(int), compare2 );

		double max = 0;
		for(int j = 0; j <= N - K; j++)
		{
			int cur = ind[j];
			double sum = PI * R[cur] * R[cur] + 2 * PI * R[cur] * H[cur];
			trace("Base = %f\n", sum);

			int k = K - 1, stack = 0;
			while(k > 0 && stack < N)
			{
				int big = ind2[stack];
				trace("\tCur = %d, stack = %d, Big = %d\n", cur, stack, big);
				if( big != cur && R[big] <= R[cur] )
				{
					double surface = 2 * PI * R[big] * H[big];
					sum += surface;
					k--;
					trace("\t%f %f\n", surface, sum);
				}
				stack++;
			}
			if(sum > max) max = sum;
			trace("Max = %f\n\n", max);
		}

      printf( "Case #%d: %f\n", i, max );
   }

   myfile.close();
   return 0;
}
