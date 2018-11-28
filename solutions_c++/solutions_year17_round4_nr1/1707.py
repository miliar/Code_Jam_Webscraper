#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	fstream fs( "sample.in", ios_base::in );
	fstream fout( "out.txt", ios_base::out );
	int T;
	fs >> T;
	for( int i = 0; i < T; i++ )
	{
		int N, P;
		fs >> N;
		fs >> P;

		int* modulos = new int[P];
		for( int j = 0; j < N; j++ )
		{
			int v;
			fs >> v;
			modulos[ v % P ]++;
		}

		int max = 0;
		if( P == 2 )
		{
			max = modulos[0];
			if( modulos[1] % 2 == 0 )
			{
				max += modulos[1] / 2;
			}
			else
			{
				max += ( modulos[1] + 1 ) / 2;
			}
			
		}
		else if( P == 3 )
		{
			max = modulos[0];
			if( modulos[1] > modulos[2] )
			{
				max += modulos[2];
				int iRemain = modulos[1] - modulos[2];
				max += ( iRemain / 3 );
				if( iRemain % 3 != 0 )
				{
					max++;
				}
			}
			else
			{
				max += modulos[1];
				int iRemain = modulos[2] - modulos[1];
				max += ( iRemain / 3 );
				if( iRemain % 3 != 0 )
				{
					max++;
				}
			}
		}
		else if( P == 4 )
		{
			max += modulos[0];
			if( modulos[1] > modulos[3] )
			{
				max += modulos[3];
				int iRemain = modulos[1] - modulos[3];
				max += modulos[2] / 2;
				if( modulos[2] % 2 == 0 )
				{
					max += iRemain / 4;
					if( iRemain % 4 != 0 )
					{
						max++;
					}
				}
				else
				{
					max++;
					iRemain - 2;
					if( iRemain > 0 )
					{
						max += iRemain / 4;
						if( iRemain % 4 != 0 )
						{
							max++;
						}
					}
				}
			}
			else
			{
				max += modulos[1];
				int iRemain = modulos[3] - modulos[1];
				max += modulos[2] / 2;
				if( modulos[2] % 2 == 0 )
				{
					max += iRemain / 4;
					if( iRemain % 4 != 0 )
					{
						max++;
					}
				}
				else
				{
					max++;
					iRemain - 2;
					if( iRemain > 0 )
					{
						max += iRemain / 4;
						if( iRemain % 4 != 0 )
						{
							max++;
						}
					}
				}
			}
		}
		fout << "Case #" << (i+1) << ": " << max << endl;


	}



		fout.close();
	fs.close();

	return 0;
}
