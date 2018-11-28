#include <bits/stdc++.h>

using namespace std;

long long T, N, K;

int main() {
  cin >> T;
  for ( int num = 1 ; num <= T ; ++num ) {
    cin >> N >> K;
    priority_queue< long long > q; 
    q.push( N );
    for ( int i = 0 ; i < K ; ++i ) {
      long long now = q.top(); q.pop();
      long long L, R;
      L = R = now / 2;
      q.push( L );
      if ( now & 1 )  
        q.push( R );
      else 
        q.push( --R );
      if ( i == K - 1 )  
        cout << "Case #" << num << ": " << max( L, R ) << " " << min( L, R ) << endl;
    }
  }
}
