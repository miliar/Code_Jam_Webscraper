#include <stdio.h>
#include <cstring>

char ary[20];		
int len;

bool isTidy()
{
	if( len == 1)
	{
		return true;
	}

	int i = 0;
	if( ary[0] == '0' )
	{
		i = 1;
	}

	for( i; i < len -1; i++ )
	{
		if( ary[i] > ary[i + 1] )
		{
			return false;
		}
	}

	return true;
}

void print( int tc, FILE* output )
{	
	int i = 0;
	if( ary[0] == '0' )
	{
		i = 1;
	}

	printf( "Case #%d: ", tc );
	fprintf( output, "Case #%d: ", tc );

	for( i; i < len; i++)
	{
		printf( "%c", ary[i] );
		fprintf( output, "%c", ary[i] );
	}
	
	printf( "\n" );
	fprintf( output, "\n" );

}

int main()
{
	freopen( "B-large.in", "r", stdin );	
	FILE *output = fopen( "gsan.out", "w" );

	int T;
	scanf( "%d", &T );

	for( int tc = 1; tc <= T; tc++ )
	{
		scanf( "%s", ary );
		len = strlen( ary );	

		if( isTidy() )
		{
			//그대로 출력
			print( tc, output );
		}
		else
		{			
			while( !isTidy() )
			{
				for( int i = len-1; i > 0; i-- )
				{
					if( ary[i] < ary[i - 1] )
					{
						ary[i - 1] -= 1;
						if( ary[i - 1] == '0' && (i - 1) != 0 )
						{
							ary[i - 1] = '9';
							ary[i - 2] = '0';
						}
						for( int j = i; j < len; j++ )
						{
							ary[j] = '9';
						}
						break;
					}
				}
			}
			
			print( tc, output );
		}
	}
	
	fclose( output );
	return 0;
}