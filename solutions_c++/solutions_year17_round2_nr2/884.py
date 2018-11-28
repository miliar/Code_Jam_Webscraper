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

int cols[6];
char labels[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
int compat[6][3] =
{
	{ 2,  3,  4 },
	{ 4, -1, -1 },
   { 0,  4,  5 },
   { 0, -1, -1 },
   { 0,  1,  2 },
   { 2, -1, -1 }
};
int sol[1000];
int first[6];

int next(int cur)
{
	int max = -1, res = -1;
	for(int i = 0; i < 6; i += 2)
	{
		if( i == cur ) { continue; }
		if(cols[i] > max)
		{
			max = cols[i];
			res = i;
		}
	}
	return res;
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

		int N;
		myfile >> N;
		for(int j = 0; j < 6; j++) { myfile >> cols[j]; first[j] = 1; }

		for(int j = 0; j < 1000; j++) { sol[j] = 0; }

		string res = "IMPOSSIBLE";

		int cont = true;
		for( int j = 1; j < 6; j += 2 )
		{
			int comp = (j + 3) % 6;
			if(cols[j] > 0)
			{
				if( cols[j] > cols[j] ||
					 (cols[j] == cols[comp] && cols[j] * 2 < N))
				{
					trace("Fail on %d(%d): %d %d\n", j, N, cols[comp], cols[j]);
					cont = false;
					break;
				}

				if(cols[j] == cols[comp])
				{
					res = "";
					for(int k = 0; k < cols[j]; k++)
					{
						res += labels[j];
						res += labels[comp];
					} 
					cont = false;
					break;
				}
				cols[comp] -= cols[j];
			}
		}

		if( cont )
		{
			for(int j = 0; j < 6; j += 2)
			{
				int comp1 = (j + 2) % 6;
				int comp2 = (j + 4) % 6;
				if(cols[j] > cols[comp1] + cols[comp2])
				{
					trace("Fail2 on %d: %d %d %d\n", j, cols[j], cols[comp1],
						cols[comp2]);
					cont = false;
					break;
				}
			}
		}

		if(cont)
		{
			int cur = next(-1);
			if(cols[0] > 0) cur = 0;
			else if(cols[2] > 0) cur = 2;
			else cur = 4;

			int pos = 0;
			for(int j = 0; j < N && cols[cur] > 0; j++, pos++)
			{
				cols[cur]--;
				sol[pos] = cur;

				if(first[ cur ] == 1)
				{
					first[ cur ] = 0;
					int comp = (cur + 3) % 6;
					for(int k = 0; k < cols[ comp ]; k++)
					{
						pos++;
						sol[pos] = comp;
						pos++;
						sol[pos] = cur;
					}
				}
				cur = next(cur);
			}

			res = "";
			for(int j = 0; j < N; j++ ) { res += labels[ sol[j] ]; }
		}

      printf( "Case #%d: %s\n", i, res.c_str() );
   }

   myfile.close();
   return 0;
}
