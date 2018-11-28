#include <vector>
#include <iostream>
#include <algorithm>
#include <assert.h>

using namespace std;

static bool findInterval( int Q, int R, int& t0, int& t1 )
{
  t0 = ( 10 * Q + 11 * R - 1 ) / ( 11 * R );
  t1 = 10 * Q / ( 9 * R );
  return t0 <= t1;
}

static int solve1( int P, int R, const vector<int>& Q )
{
  int result = 0;
  for( int i = 0; i < P; ++i ) {
    int t0, t1;
    if( findInterval( Q[i], R, t0, t1 ) ) {
      result++;
    }
  }
  return result;
}

static int maxFlow( const vector< vector<int> >& c )
{
  const int n = c.size();

  const int inf = 1000*1000*1000;


  typedef vector<int> graf_line;
  typedef vector<graf_line> graf;

  typedef vector<int> vint;
  typedef vector<vint> vvint;

  vvint f (n, vint(n));
	for (;;)
	{
		
		vint from (n, -1);
		vint q (n);
		int h=0, t=0;
		q[t++] = 0;
		from[0] = 0;
		for (int cur; h<t;)
		{
			cur = q[h++];
			for (int v=0; v<n; v++)
				if (from[v] == -1 &&
					c[cur][v]-f[cur][v] > 0)
				{
					q[t++] = v;
					from[v] = cur;
				}
		}

		if (from[n-1] == -1)
			break;
		int cf = inf;
		for (int cur=n-1; cur!=0; )
		{
			int prev = from[cur];
			cf = min (cf, c[prev][cur]-f[prev][cur]);
			cur = prev;
		}

		for (int cur=n-1; cur!=0; )
		{
			int prev = from[cur];
			f[prev][cur] += cf;
			f[cur][prev] -= cf;
			cur = prev;
		}

	}

	int flow = 0;
	for (int i=0; i<n; i++)
		if (c[0][i])
			flow += f[0][i];

	return flow;
}

static bool shouldConnect( int R0, int R1, int Q0, int Q1 )
{
  int t00, t01;
  if( !findInterval( Q0, R0, t00, t01 ) ) {
    return false;
  }
  int t10, t11;
  if( !findInterval( Q1, R1, t10, t11 ) ) {
    return false;
  }
  return t01 >= t10 && t00 <= t11;
}

static int solve2( int P, int R0, int R1, const vector<int>& Q0, const vector<int>& Q1 )
{
  const int n = 2 * P + 2;
  vector< vector<int> > c( n, vector<int>( n, 0 ) );
  for( int i = 1; i <= P; ++i ) {
    c[0][i] = 1;
  }
  for( int i = P+1; i <= 2*P; ++i ) {
    c[i][2*P+1] = 1;
  }
  for( int i = 1; i <= P; ++i ) {
    for( int j = P+1; j <= 2*P; ++j ) {
      if( shouldConnect( R0, R1, Q0[i-1], Q1[j-P-1] ) ) {
        c[i][j] = 1;
      }
    }
  }
  return maxFlow( c );
}

static int solve( int N, int P, const vector<int>& R, const vector< vector<int> >& Q )
{
  if( N == 1 ) {
    return solve1( P, R[0], Q[0] );
  }
  assert( N == 2 );
  return solve2( P, R[0], R[1], Q[0], Q[1] );
}

int main()
{
  int t;
  cin >> t;

  for( int testCase = 0; testCase < t; ++testCase ) {
    int N, P;
    cin >> N >> P;
    assert( N <= 2 );
    vector<int> R(N);
    for( int i = 0; i < N; ++i ) {
      cin >> R[i];
    }
    vector< vector<int> > Q( N, vector<int>( P ) );
    for( int i = 0; i < N; ++i ) {
      for( int j = 0; j < P; ++j ) {
        cin >> Q[i][j];
      }
    }
    cout << "Case #" << testCase + 1 << ": " << solve( N, P, R, Q ) << endl;
  }

  return 0;
}