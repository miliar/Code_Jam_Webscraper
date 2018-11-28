#include <stdio.h>
#include  <string.h>


int main()
{
	int  t, k, flips[ 102 ], len, flag, fcounter, buffer;
	char arr[ 102 ];
	scanf( "%d", &t );
	for( int i = 0; i < t; i++ )
	{
		flag = 0;
		fcounter = 0;
		scanf( "%s", arr );
		scanf( "%d", &k );
		for( int x = 0; x < 102; x++ )
		{
			flips[ x ] = 0;
		}

		int j = 0;
		len = strlen( arr );
		while( arr[ j ] != '-' && j <= len - k )
		{
			j++;
		}
		
		while( j <= len -k )
		{			
			if( arr[ j ] == '-' && flips[ j ]%2 == 0 )
			{
				for( int x = j+1; x < j + k; x++ )
				{
					flips[ x ]++;
				}
				fcounter++;
			}
			else if( arr[ j ] == '+' && flips[ j ]%2 == 1 )
			{
				for( int x = j+1; x < j + k; x++ )
				{
					flips[ x ]++;
				}
				fcounter++;
			}
			j++;
		}
		while( j < len )
		{
			if( arr[ j ] == '-' && flips[ j ]%2 == 0 )
			{
				flag = 1;
			}
			else if( arr[ j ] == '+' && flips[ j ]%2 == 1 )
			{
				flag = 1;
			}
			j++;
		}
		
		if( flag == 1 )
		{
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		}
		else 
		{
			printf("Case #%d: %d\n", i+1, fcounter);
		}


	}

}
