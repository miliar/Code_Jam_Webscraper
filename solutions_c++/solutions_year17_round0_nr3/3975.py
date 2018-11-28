#include <iostream>
#include <utility>
#include <assert.h>

using namespace std;

static pair<int, int> solve( int n, int k ) 
{
  assert( k <= n );
  assert( k >= 1 );
  if( k == 1 ) {
    return make_pair( n / 2, ( n - 1 ) / 2 );
  }
  if( n % 2 == 1 && k % 2 == 1 ) {
    return solve( ( n - 1 ) / 2, ( k - 1 ) / 2 );
  }
  if( n % 2 == 1 && k % 2 == 0 ) {
    return solve( ( n - 1 ) / 2, k / 2 );
  }
  if( n % 2 == 0 && k % 2 == 1 ) {
    return solve( ( n - 1 ) / 2, ( k - 1 ) / 2 );
  }
  assert( n % 2 == 0 && k % 2 == 0 );
  return solve( n / 2, k / 2 );
}

int main()
{
  int t;
  cin >> t;
  for( int i = 0; i < t; ++i ) {
    int n, k;
    cin >> n >> k;
    const pair<int, int> ans = solve( n, k );
    cout << "Case #" << (i+1) << ": " << ans.first << " " << ans.second << endl;
  }

  return 0;
}