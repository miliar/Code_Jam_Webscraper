#include<iostream>
#include<map>
#include<cassert>
#include<vector>
#include<numeric>
#include<algorithm>
using namespace std;

pair< long long, long long > get( long long n )
{
  long long maxi = n / 2 ;
  return make_pair( maxi , n - 1 - maxi );
}

int main()
{
  int t;
  cin >> t;
  for( int tc = 1 ; tc <= t ; ++tc )
  {
    cout << "Case #"<<tc<<": ";
    long long n,k;
    map<long long ,long long> M;

    cin >> n >> k;

    M[n] = 1;
    pair< long long, long long  > qn = get( n );
    if( qn.first )
      M[ qn.first ] += M[n];
    if( qn.second )
      M[ qn.second ] += M[n];

    while( qn.first > 1 )
    {

      pair< long long, long long  >  P[2] = { get( qn.first ) , get( qn.second ) } ;
      long long parent[2]  = { qn.first ,  qn.second  } ;
      for( int i = 0 ; i < 1 + ( qn.first != qn.second )? 1 :0 ; ++i )
      {
         pair< long long, long long  > cur = P[i];
         long long curp = parent[i];
	 if( cur.first )  M[ cur.first ] += M[ curp ];
	 if( cur.second ) M[ cur.second] += M[ curp ];
      }

      long long dif = qn.first % 2 == 0 ? qn.first : qn.second;
      qn = get( dif );
    }

    long long ans;
    vector< pair<long long, long long> > V ( M.begin(), M.end() );
    reverse( V.begin(), V.end() );
    long long acu = 0;
    for( auto x : V )
      acu += x.second;

    assert( n == acu );

    int pos = 0;
    while( k > 0 )
    {
         k -= V[pos].second;
	 ans = V[pos].first;
	 ++pos;
    
    }
    long long hi = ans / 2;
    long long lo = ans - hi - 1;

    cout << hi <<" "<<lo<<endl;
  }
  return 0;
}
