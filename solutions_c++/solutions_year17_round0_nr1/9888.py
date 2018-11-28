/*
  by asas
*/
#include <bits/stdc++.h>
#define CASET int ___T, Case = 1; scanf("%d ", &___T); while (___T-- > 0)
#define SZ(X) ((int)(X).size())
#define PHB push_back
#define PPB pop_back
#define LL long long
#define ULL unsigned long long
#define ALL(X) (X).begin(), (X).end()
#define MP make_pair
#define PII pair<int,int>
#define VPII vector<pair<int,int>>
#define PLL pair<long long,long long>
#define F first
#define S second
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define DRI(X) int (X) = in()
#define DRII(X, Y) int X = in() , Y = in()
#define DRIII(X, Y, Z) int X = in() , Y = in() , Z = in()
using namespace std ;
const int MOD = 1e9+7;
const int SIZE = 1e5+10;
inline int in(int d=0,char q=0,int c=1){while(q!='-'&&q!=EOF&&(q<48||q>57))q=getchar();if(q==EOF)return EOF;if(q=='-')c=-1,q=getchar();do d=d*10+(q^48),q=getchar();while(q<58&&q>47);return c*d;}
// template end here
void small() ;
int main()
{
	small() ;
	return 0 ;
}
#define CHANGE(X) X=(X=='+')?'-':'+';
void small()
{
	CASET
	{
		map<string,int> M ;
		queue<string> Q ;
		string s , SE ;
		M.clear() ;
		while (!Q.empty())Q.pop() ;
		int k , step ;
		cin >> s >> k ;
		SE = string( SZ( s ) , '+' ) ;
//cout << "SE: " << SE << endl ;
		Q.push( s ) ;
		M[ s ] = 0 ;
		while ( !Q.empty() )
		{
			s = Q.front() ;
			Q.pop() ;
			step = M[ s ] + 1 ;
//cout << "step: " << step << endl ;
//cout << "s\t" << s << endl ;
			for ( int i = 0 ; i < k ; ++ i )
			{
				CHANGE( s[ i ] ) ;
			}
//cout << k - 1 << "\t" << s << endl ;
			if ( M.count( s ) <= 0 ) M[ s ] = step , Q.push( s ) ;
			for ( int i = k ; i < s.size() ; ++ i )
			{
				CHANGE( s[ i - k ] ) ;
				CHANGE( s[ i ] ) ;
//cout << i << "\t" << s << endl ;
				if ( M.count( s ) <= 0 ) M[ s ] = step , Q.push( s ) ;
			}
			if ( M.count( SE ) > 0 ) break ;
		}
		if ( M.count( SE ) > 0 )
		{
			printf( "Case #%d: %d\n" , Case ++ , M[ SE ] ) ;
		}
		else
		{
			printf( "Case #%d: IMPOSSIBLE\n" , Case ++ ) ;
		}
	}
}
