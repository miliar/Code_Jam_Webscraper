#include <stdio.h>
#include <cstring>

char cake[1001];
int cake_cnt, happy_cnt;

void flip( int pos, int S )
{
	for( int i = pos; i < pos + S; i++ )
	{
		if( cake[i] == '-' )
		{
			happy_cnt++;
			cake[i] = '+';
		}
		else
		{
			happy_cnt--;
			cake[i] = '-';
		}
	}
}

int main()
{
	freopen( "A-large.in", "r", stdin );
	FILE *output = fopen( "gsan.out", "w" );

	int T;
	scanf( "%d", &T );

	for( int tc = 1; tc <= T; tc++ )
	{	
		int s;

		memset( cake, 0 , sizeof(cake) );
		happy_cnt = 0;

		scanf( "%s", cake );
		scanf( "%d", &s );

		cake_cnt = strlen( cake );

		for( int i = 0; i < cake_cnt; i++ )
		{
			if( cake[i] == '+' )
			{
				happy_cnt++;
			}
		}

		int ans = 0;

		for( int i = 0; i < cake_cnt - s + 1; i++ )
		{
			if( cake[i] == '-' )
			{
				ans++;
				flip( i, s );
			}
		}

		if( happy_cnt == cake_cnt )
		{
			printf( "Case #%d: %d\n", tc, ans );
			fprintf( output, "Case #%d: %d\n", tc, ans );
		}
		else
		{
			printf( "Case #%d: IMPOSSIBLE\n", tc );
			fprintf( output, "Case #%d: IMPOSSIBLE\n", tc );
		}
		
	}

	fclose( output );

	return 0;
}