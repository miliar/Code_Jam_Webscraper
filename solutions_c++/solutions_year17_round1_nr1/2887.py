#include  <bits/stdc++.h>

#define F0(i,N) for(int i=0; i<N; ++i)
#define F1(i,N) for(int i=1; i<=N; ++i)

using namespace std;
int t=0;

template<class T> inline ostream& operator<<( ostream& os, const vector<T>& v )
{
	for( auto& e:v )
		os << ' ' << e;
	return os;
}

bool isValid( vector<string>& v, char& c, long r1, long c1, long r2, long c2 )
{
	const bool cnull = (c == 0);
	F0( i, r2-r1+1 )
	{
		F0( j, c2-c1+1 )
		{
			if( v[ r1 + i ][ c1 + j ] != '?' )
			{
				if ( c == 0 )
					c = v[ r1 + i ][ c1 + j ];
				else if( v[ r1 + i ][ c1 + j ] != c )
				{
					if( cnull )
						c = 0;
					return false;
				}
			}
		}
	}
	return true;
}

void fill( vector<string>& v, char c, long r1, long c1, long r2, long c2 )
{
	for( int i = r1; i<=r2; i++ )
		for( int j = c1; j<=c2; j++ )
			v[i][j] = c;
}


void solve()
{
	cout << "Case #" << t << ":" << endl;
	long R,C; cin >> R >> C;
	vector<string> v(R);
	set<char> s;
	F0(i, R)
	{
		cin >> v[i];
	}
	//max row
	char c = 0;
	F0( i, R )
	{
		F0( j, C )
		{
			if( s.find(v[i][j]) != s.end()  )
				continue;
			long ri=0, rj=0;
			int k = 0;
			for( k= 0; k < min( R-i, C-j ); k++)
			{
				if( ! isValid( v, c, i, j, i+k, j+k ) )
				{
					if(c)
						ri = rj = k - 1;
					break;
				}
			}
			for( k = ri + 1; k < R-i; k++ )
			{
				if( ! isValid( v, c, i, j, i+k, j+rj ) )
				{
					break;
				}
			}
			if( c )
				ri = k-1;
			for( k = rj + 1; k < C-j; k++ )
			{
				if( ! isValid( v, c, i, j, i+ri, j+k ) )
				{
					break;
				}
			}
			rj = k-1;
			fill( v, c, i,j, i+ri, j+rj );
			s.insert(c);
			c = 0;
		}
	}
	F0( i, R )
	{
		cout << v[i] << endl;
	}
}

int main(int argc, char * argv[] )
{
	//stdin = freopen("A.in", "r", stdin); 
	stdin = freopen("A-small-attempt2.in", "r", stdin); stdout = freopen("A-small.out", "w", stdout);
	//stdin = freopen("A-large.in", "r", stdin); stdout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for( t=1; t<=T; ++t )
		solve();
	return 0;
}
