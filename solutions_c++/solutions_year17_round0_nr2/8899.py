#include <stdio.h>
#include <string.h>

int main()
{
	int t, len, arrd[ 21 ], index1, index2, flag;
	long long int sum;
	char arrc[ 21 ]; 
	scanf( "%d", &t );
	for( int i = 1; i <= t; i++ )
	{
		sum =0 ;
		index1 = 0;
		index2 = 0;
		flag = 0;
		scanf( "%s", arrc );
		len  = strlen( arrc );
		int j = 0;
		while(  j < len )
		{
			arrd[ j ] = arrc[ j ] - '0';
			j++;
		}
		j =0;
		while( arrd[ j ] == 0 )
		{
			index1++;
			index2++;
			j++;
		}
		index2++;
		
		while( index2 < len )
		{ 
				
			if( arrd[ index2 ] > arrd[ index1 ] )
			{
				index1 = index2;
				index2++;
			}
			else if( arrd[ index2 ] == arrd[ index1 ] )
			{
				index2++;
			}
			else if( ( arrd[ index2 ] < arrd[ index1 ] ) || ( arrd[ index2 ] == 0 ) )
			{
				flag = 1;
				break;
			}
		}

		if( flag == 1 )
		{
			arrd[ index1 ]--;
			for( int k = index1 + 1; k < len; k++  )
			{
				arrd[ k ] = 9;
			}
		}

		index2 = 0;
		while( arrd[ index2 ] == 0 )
		{
			index2++;
		}

		for( int k = index2; k <= len -1; k++ )
		{
			sum = arrd[ k ] + ( sum *10 );
		}

		printf("Case #%d: %lld\n",i, sum );

	}
}